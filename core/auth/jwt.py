from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt

from core.auth.schemas import Claims
from core.settings import settings

BEARER: str = "bearer"


def create_access_token(data: Claims) -> str:
    claims = {
        "sub": data.email,
        "exp": datetime.utcnow() + timedelta(minutes=settings.JWT_TOKEN_EXPIRE_MINUTES),
    }

    return jwt.encode(
        claims=claims, key=settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM
    )


def verify_token(token: str) -> Optional[Claims]:
    try:
        payload = jwt.decode(
            token=token, key=settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM]
        )
        email = payload.get("sub", None)
        return None if email is None else Claims(email=email)
    except JWTError:
        return None
