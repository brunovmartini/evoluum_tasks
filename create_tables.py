from core.config import settings
from core.database import engine


async def create_tables() -> None:
    from users.models import UserModel
    from tasks.models import TaskModel
    print('Creating tables on the database')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Success on creating the database tables')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
