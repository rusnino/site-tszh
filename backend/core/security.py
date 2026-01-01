from datetime import datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(subject: dict[str, Any]) -> str:
    expires_delta = timedelta(minutes=settings.access_token_exp_minutes)
    return _create_token(subject, expires_delta, token_type="access")


def create_refresh_token(subject: dict[str, Any]) -> str:
    expires_delta = timedelta(days=settings.refresh_token_exp_days)
    return _create_token(subject, expires_delta, token_type="refresh")


def _create_token(subject: dict[str, Any], expires_delta: timedelta, token_type: str) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "type": token_type, **subject}
    return jwt.encode(to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm)
