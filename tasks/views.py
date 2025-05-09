from typing import List

from fastapi import APIRouter, status, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.auth import get_current_user
from core.database import get_session
from tasks import queries
from tasks.schemas import TaskResponse, TaskRequest
from users.models import UserModel

tasks_router = APIRouter(prefix='/tasks', tags=['tasks'])


@tasks_router.get('/', response_model=List[TaskResponse])
async def get_tasks(
    db: AsyncSession = Depends(get_session),
    logged_user: UserModel = Depends(get_current_user)
):
    return await queries.get_tasks(logged_user.id, db)


@tasks_router.get(
    '/{task_id}',
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)
async def get_task(task_id: int, db: AsyncSession = Depends(get_session)):
    return await queries.get_task(task_id, db)


@tasks_router.post(
    '/',
    status_code=status.HTTP_201_CREATED,
    response_model=TaskResponse
)
async def create_task(
    task: TaskRequest,
    logged_user: UserModel = Depends(get_current_user),
    db: AsyncSession = Depends(get_session)
):
    return await queries.create_task(task, logged_user.id, db)


@tasks_router.put(
    '/{task_id}',
    response_model=TaskResponse,
    status_code=status.HTTP_200_OK
)
async def update_task(
    task_id: int,
    task: TaskRequest,
    db: AsyncSession = Depends(get_session),
    logged_user: UserModel = Depends(get_current_user)
):
    return await queries.update_task(task_id, task, logged_user.id, db)


@tasks_router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_session),
    logged_user: UserModel = Depends(get_current_user)
):
    await queries.delete_task(task_id, logged_user.id, db)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
