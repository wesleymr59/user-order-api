from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.services.user_service import UserService
from src.services.auth.tokenAuth import AuthHandler
from src.schemas.user_schema import userBody, User, userUpdate
from src.configs.enviroments import get_environment_variables

router = APIRouter(prefix="/v1/users",tags=["user"])
user_service = UserService()
authHandler = AuthHandler()
env = get_environment_variables()

@router.post("/create")
async def create_user(body: userBody):
    return {"token": user_service.insert_user(jsonable_encoder(body))}
    

@router.get("/get_user/{cpf}", response_model=User)
async def get_user(cpf: str, token = Depends(authHandler.verify_token)) -> (list[tuple] | None):
    user =  user_service.get_user(cpf)
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado")
    return user

@router.delete("/dele_user")
async def delete_user(cpf: str,token = Depends(authHandler.verify_token)):
    try:
        return user_service.delete_user(cpf, token)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível deletar o usuario")

@router.put("/dele_user")
async def update_user(body: userUpdate, cpf: str, token = Depends(authHandler.verify_token)):
    try:
        return user_service.update_user(jsonable_encoder(body), cpf, token)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Não foi possível atualizar o usuario")