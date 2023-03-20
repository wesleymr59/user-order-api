from fastapi import Depends, FastAPI
from src.routers.v1 import user_router
from src.configs.enviroments import get_environment_variables

env = get_environment_variables()

app = FastAPI(title=env.APP_NAME,
    version=env.API_VERSION)


app.include_router(user_router.router)
