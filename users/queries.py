from fastapi import Depends
from pydantic import EmailStr

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from users.models import UserModel
from users.schemas import UserRequest
from core.database import get_session
from core.security import generate_hash_password
from users.exceptions import InvalidEmail


async def get_user(user_id: int, session: AsyncSession = Depends(get_session)):
    query = select(UserModel).filter(UserModel.id == user_id)
    result = await session.execute(query)
    user = result.scalars().unique().one_or_none()

    return user


async def create_user(user: UserRequest, session: AsyncSession = Depends(get_session)):
    new_user = UserModel(
        email=user.email,
        password=generate_hash_password(user.password),
        name=user.name,
        last_name=user.last_name,
    )
    try:
        session.add(new_user)
        await session.commit()

        return new_user
    except IntegrityError:
        raise InvalidEmail


async def get_user_by_email(email: EmailStr, session: AsyncSession):
    query = select(UserModel).filter(UserModel.email == email)
    result = await session.execute(query)
    user = result.scalars().unique().one_or_none()

    return user
