from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from tasks.models import TaskModel
from tasks.schemas import TaskRequest
from core.database import get_session
from tasks.exceptions import TaskNotFound, UnauthorizedUser


async def get_tasks(
    logged_user_id: int,
    session: AsyncSession = Depends(get_session)
):
    query = select(TaskModel).filter(TaskModel.user_id == logged_user_id)
    result = await session.execute(query)
    tasks = result.scalars().unique().all()

    return tasks


async def get_task(
    task_id: int,
    session: AsyncSession = Depends(get_session)
):
    query = select(TaskModel).filter(TaskModel.id == task_id)
    result = await session.execute(query)
    task = result.scalars().unique().one_or_none()

    if not task:
        raise TaskNotFound

    return task


async def create_task(
    task: TaskRequest,
    logged_user_id: int,
    db: AsyncSession = Depends(get_session)
):
    new_task = TaskModel(
        title=task.title,
        description=task.description,
        user_id=logged_user_id
    )
    db.add(new_task)
    await db.commit()

    return new_task


async def update_task(
    task_id: int,
    task: TaskRequest,
    logged_user_id: int,
    session: AsyncSession = Depends(get_session)
):
    task_up = await get_task(task_id, session)

    if not task_up:
        raise TaskNotFound

    if logged_user_id != task_up.user_id:
        raise UnauthorizedUser

    if task.title:
        task_up.title = task.title
    if task.description:
        task_up.description = task.description

    await session.commit()

    return task_up


async def delete_task(
    task_id: int,
    logged_user_id: int,
    session: AsyncSession = Depends(get_session)
):
    task = await get_task(task_id, session)

    if logged_user_id != task.user_id:
        raise UnauthorizedUser

    await session.delete(task)
    await session.commit()
