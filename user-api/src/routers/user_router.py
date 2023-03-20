from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from ..services.user_service import UserService
from ..services.auth.tokenAuth import AuthHandler
from .user_schema import userBody, User, userUpdate


user_service = UserService()
router = APIRouter(tags=["user"])
_AuthHandler = AuthHandler()

@router.post("/user/create")
async def create_user(body: userBody):
    return {"token": user_service.insert_user(jsonable_encoder(body))}

@router.get("/user/get_user/{cpf}", response_model=list[User])
async def get_user(cpf: str, token = Depends(_AuthHandler.verify_token)):
    return user_service.get_user(cpf)

@router.delete("/user/dele_user")
async def delete_user(cpf: str,token = Depends(_AuthHandler.verify_token)):
    return user_service.delete_user(cpf, token)

@router.put("/user/dele_user")
async def update_user(body: userUpdate, cpf: str, token = Depends(_AuthHandler.verify_token)):
    return user_service.update_user(jsonable_encoder(body), cpf, token)