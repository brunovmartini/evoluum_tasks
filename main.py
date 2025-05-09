from fastapi import FastAPI

from users.views import users_router
from tasks.views import tasks_router


app = FastAPI(title='Evoluum Tasks')
app.include_router(users_router)
app.include_router(tasks_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
