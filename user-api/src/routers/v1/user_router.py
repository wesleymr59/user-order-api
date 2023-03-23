from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.services.user_service import UserService
from src.services.auth.tokenAuth import AuthHandler
from src.schemas.user_schema import userBody, User, userUpdate
from src.configs.enviroments import get_environment_variables

router = APIRouter(prefix="/v1/users",tags=["user"])
__user_service = UserService()
__AuthHandler = AuthHandler()
env = get_environment_variables()

@router.post("/create")
async def create_user(body: userBody):
    try:
        return {"token": __user_service.insert_user(jsonable_encoder(body))}
    except:
        raise HTTPException(status_code=400, detail="Não foi possível Criar o usuario")

@router.get("/get_user/{cpf}", response_model=User)
async def get_user(cpf: str, token = Depends(__AuthHandler.verify_token)) -> (list[tuple] | None):
    user =  __user_service.get_user(cpf)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    return user

@router.delete("/dele_user")
async def delete_user(cpf: str,token = Depends(__AuthHandler.verify_token)):
    try:
        return __user_service.delete_user(cpf, token)
    except:
        raise HTTPException(status_code=404, detail="Não foi possível deletar o usuario")

@router.put("/dele_user")
async def update_user(body: userUpdate, cpf: str, token = Depends(__AuthHandler.verify_token)):
    try:
        return __user_service.update_user(jsonable_encoder(body), cpf, token)
    except:
        raise HTTPException(status_code=404, detail="Não foi possível atualizar o usuario")