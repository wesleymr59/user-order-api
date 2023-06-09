from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from src.services.user_service import UserService
from src.services.auth.tokenAuth import AuthHandler
from src.schemas.user_schema import userBody, User, userUpdate


router = APIRouter(prefix="/v1/users",tags=["user"])
user_service = UserService()
authHandler = AuthHandler()


@router.post("/create", status_code=201)
async def create_user(body: userBody):
    """Criação do usuário"""
    return {"token": user_service.insert_user(jsonable_encoder(body))}
    

@router.get("/get_user/{cpf}", response_model=User,status_code=201)
async def get_user(cpf: str, token = Depends(authHandler.verify_token)):
    """Busca usuario pelo numero do CPF"""
    user =  user_service.get_user(cpf)
    if user == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Usuario não encontrado")
    return user

@router.delete("/delete_user")
async def delete_user(cpf: str,token = Depends(authHandler.verify_token)):
    """Delete o usuário pelo numero do CPF"""
    try:
        return user_service.delete_user(cpf, token)
    except:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Não foi possível deletar o usuario")

@router.put("/put_user")
async def update_user(body: userUpdate, cpf: str, token = Depends(authHandler.verify_token)):
    """Atualiza as informações do usuário"""
    try:
        return user_service.update_user(jsonable_encoder(body), cpf, token)
    except:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Não foi possível atualizar o usuario")