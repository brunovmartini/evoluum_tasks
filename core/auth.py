from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import BaseModel
from pydantic import EmailStr
from pytz import timezone
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.database import Session, get_session
from core.security import verify_password
from users.exceptions import AuthenticationUnauthorized
from users.models import UserModel
from users.queries import get_user_by_email, get_user

oauth2_schema = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_URL)


class TokenData(BaseModel):
    username: Optional[str] = None


async def authenticate_user(
    email: EmailStr,
    password: str,
    db: AsyncSession
) -> Optional[UserModel]:
    user = await get_user_by_email(email, db)

    if not user:
        return

    if not verify_password(password, user.password):
        return

    return user


def _create_token(token_type: str, life_time: timedelta, sub: str) -> str:
    local_timezone = timezone(settings.LOCAL_TIME_ZONE)
    expiration = datetime.now(tz=local_timezone) + life_time

    payload = {
        'type': token_type,
        'exp': expiration,
        'iat': datetime.now(tz=local_timezone),
        'sub': str(sub)
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.ALGORITHM
    )


def create_access_token(sub: str) -> str:
    return _create_token(
        token_type=settings.TOKEN_TYPE,
        life_time=timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES)),
        sub=sub
    )


async def get_current_user(
    db: Session = Depends(get_session),
    token: str = Depends(oauth2_schema)
) -> UserModel:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={'verify_aud': False}
        )

        username: str = payload.get('sub')
        if not username:
            raise AuthenticationUnauthorized

        token_data: TokenData = TokenData(username=username)

    except JWTError:
        raise AuthenticationUnauthorized

    user = await get_user(int(token_data.username), db)

    if not user:
        raise AuthenticationUnauthorized

    return user
