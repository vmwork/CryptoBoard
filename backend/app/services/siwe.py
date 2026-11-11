import re
from binascii import Error as HexError
from dataclasses import dataclass
from datetime import datetime, timezone

from eth_account import Account
from eth_account.messages import encode_defunct
from eth_keys.exceptions import BadSignature
from eth_utils.exceptions import ValidationError

from app.core.config import settings

_ADDRESS_PATTERN = r"0x[0-9a-fA-F]{40}"
_NONCE_PATTERN = r"[a-zA-Z0-9]{8,}"
_CHAIN_ID_PATTERN = r"[1-9][0-9]*"
_RFC3339_PATTERN = (
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]+)?(?:Z|[+-][0-9]{2}:[0-9]{2})"
)
_MESSAGE_PATTERN = re.compile(
    rf"^(?P<domain>[^\r\n]+) wants you to sign in with your Ethereum account:\n"
    rf"(?P<address>{_ADDRESS_PATTERN})\n"
    rf"(?:\n(?P<statement>[^\r\n]*(?:\n[^\r\n]+)*)\n)?"
    rf"\nURI: (?P<uri>\S+)\n"
    rf"Version: (?P<version>1)\n"
    rf"Chain ID: (?P<chain_id>{_CHAIN_ID_PATTERN})\n"
    rf"Nonce: (?P<nonce>{_NONCE_PATTERN})\n"
    rf"Issued At: (?P<issued_at>{_RFC3339_PATTERN})"
    rf"(?:\nExpiration Time: (?P<expiration_time>{_RFC3339_PATTERN}))?"
    rf"(?:\nNot Before: (?P<not_before>{_RFC3339_PATTERN}))?"
    rf"(?:\nRequest ID: (?P<request_id>\S*))?"
    rf"(?:\nResources:\n(?P<resources>- \S+(?:\n- \S+)*))?$"
)


class SiweValidationError(ValueError):
    pass


@dataclass(frozen=True)
class SiweMessage:
    address: str
    nonce: str


def _parse_timestamp(value: str, field_name: str) -> datetime:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SiweValidationError(f"Invalid {field_name}") from exc
    if parsed.utcoffset() is None:
        raise SiweValidationError(f"Invalid {field_name}")
    return parsed.astimezone(timezone.utc)


def parse_and_verify_siwe_message(
    message: str,
    signature: str,
    wallet_address: str | None = None,
    *,
    now: datetime | None = None,
) -> SiweMessage:
    match = _MESSAGE_PATTERN.fullmatch(message)
    if match is None:
        raise SiweValidationError("Invalid EIP-4361 message format")

    fields = match.groupdict()
    if fields["domain"] != settings.siwe_domain:
        raise SiweValidationError("Invalid SIWE domain")
    if fields["uri"] != settings.siwe_uri:
        raise SiweValidationError("Invalid SIWE URI")
    if int(fields["chain_id"]) != settings.evm_chain_id:
        raise SiweValidationError("Invalid SIWE chain ID")
    message_address = fields["address"].lower()
    if wallet_address is not None:
        if not re.fullmatch(_ADDRESS_PATTERN, wallet_address):
            raise SiweValidationError("Invalid wallet address")
        if wallet_address.lower() != message_address:
            raise SiweValidationError("Wallet address does not match the message")

    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=timezone.utc)
    issued_at = _parse_timestamp(fields["issued_at"], "Issued At")
    if issued_at > current_time:
        raise SiweValidationError("SIWE message was issued in the future")
    if fields["expiration_time"] is not None:
        expiration_time = _parse_timestamp(
            fields["expiration_time"], "Expiration Time"
        )
        if current_time >= expiration_time:
            raise SiweValidationError("SIWE message has expired")
    if fields["not_before"] is not None:
        not_before = _parse_timestamp(fields["not_before"], "Not Before")
        if current_time < not_before:
            raise SiweValidationError("SIWE message is not active yet")

    try:
        recovered_address = Account.recover_message(
            encode_defunct(text=message),
            signature=signature,
        )
    except (BadSignature, ValidationError, ValueError, TypeError, HexError) as exc:
        raise SiweValidationError("Invalid wallet signature") from exc
    if recovered_address.lower() != message_address:
        raise SiweValidationError("Wallet signature does not match the address")

    return SiweMessage(address=message_address, nonce=fields["nonce"])
