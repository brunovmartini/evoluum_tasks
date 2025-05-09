from decouple import config
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Setttings(BaseSettings):
    DB_URL = 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}'.format(
        user=config('POSTGRES_USER', 'postgres'),
        password=config('POSTGRES_PASSWORD', 'password'),
        host=config('POSTGRES_HOST', 'localhost'),
        port=config('POSTGRES_PORT', 5433),
        db=config('POSTGRES_DB', 'database'),
    )
    DBBaseModel = declarative_base()
    JWT_SECRET = config('JWT_SECRET', 'secret')
    ALGORITHM = config('ALGORITHM', 'HS000')
    ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', 1000)
    LOCAL_TIME_ZONE = config('LOCAL_TIME_ZONE', 'United States')
    TOKEN_URL = config('TOKEN_URL', '/url')
    TOKEN_TYPE = config('TOKEN_TYPE', 'type')

    class Config:
        case_sensitive = True


settings = Setttings()
