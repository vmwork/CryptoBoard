from functools import lru_cache

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    postgres_user: str = "postgres"
    postgres_password: str = "postgres"
    postgres_server: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "classifyd_db"

    redis_url: str
    evm_rpc_url: str
    evm_chain_id: int = Field(default=42161, gt=0)
    secret_key: str
    internal_bff_secret: str

    siwe_domain: str = "localhost"
    siwe_uri: str = "http://localhost"
    session_cookie_name: str = "session_id"
    nonce_ttl_seconds: int = Field(default=300, gt=0)
    session_ttl_seconds: int = Field(default=604800, gt=0)

    @field_validator("secret_key", "internal_bff_secret")
    @classmethod
    def validate_secret_length(cls, value: str) -> str:
        if len(value) < 32:
            raise ValueError("must contain at least 32 characters")
        return value

    @field_validator("redis_url", "evm_rpc_url", "siwe_domain", "siwe_uri")
    @classmethod
    def validate_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("must not be empty")
        return value.strip()

    @property
    def database_url(self) -> URL:
        return URL.create(
            "postgresql+psycopg2",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_server,
            port=self.postgres_port,
            database=self.postgres_db,
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
