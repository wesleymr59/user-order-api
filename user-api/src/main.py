from fastapi import Depends, FastAPI

from .routers import user_router

app = FastAPI()


app.include_router(user_router.router)
