from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession

from users.models import UserModel
from users.schemas import UserResponse, UserRequest
from core.database import get_session
from core.auth import get_current_user
from core.auth import authenticate_user, create_access_token
from users.exceptions import IncorrectAccessData, UserNotFound
from users import queries


users_router = APIRouter(prefix='/users', tags=['users'])


@users_router.get('/logged', response_model=UserResponse)
def get_logged(logged: UserModel = Depends(get_current_user)):
    return logged


@users_router.get('/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await queries.get_user(user_id, db)

    if not user:
        raise UserNotFound

    return user


@users_router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserRequest, db: AsyncSession = Depends(get_session)):
    return await queries.create_user(user, db)


@users_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate_user(email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise IncorrectAccessData

    return JSONResponse(
        content={'access_token': create_access_token(sub=user.id), 'token_type': 'bearer'},
        status_code=status.HTTP_200_OK
    )
