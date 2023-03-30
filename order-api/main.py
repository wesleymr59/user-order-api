from fastapi import FastAPI
from src.routers.v1 import order_router
from src.configs.enviroments import get_environment_variables

env = get_environment_variables()

app = FastAPI(title=env.APP_NAME,
    version=env.API_VERSION)


app.include_router(order_router.router)
