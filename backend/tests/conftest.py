import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.base import Base
from app.models.user import User

os.environ.setdefault(
    "TELEGRAM_BOT_TOKEN",
    "8823138444:AAFNwE-5GSUxd5ZEY65V7ygsMC_errQ_k74",
)
os.environ.setdefault("TELEGRAM_BOT_USERNAME", "CryptoBoard_Dev_bot")


class FakeRedis:
    def __init__(self) -> None:
        self.data: dict[str, str] = {}

    def set(self, key: str, value: str, *, ex: int | None = None) -> None:
        self.data[key] = value

    def get(self, key: str) -> str | None:
        return self.data.get(key)

    def delete(self, key: str) -> None:
        self.data.pop(key, None)

    def eval(self, script: str, num_keys: int, key: str, value: str) -> int:
        stored = self.data.get(key)
        if stored == value:
            self.data.pop(key, None)
            return 1
        return 0


@pytest.fixture
def fake_cache() -> FakeRedis:
    return FakeRedis()


@pytest.fixture
def sqlite_session() -> Session:
    engine = create_engine("sqlite:///:memory:", future=True)
    Base.metadata.create_all(engine, tables=[User.__table__])
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
