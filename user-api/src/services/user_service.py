from ..models.mySql.repository.user_repository import UserRepository
from .functions import FunctionsAux
from fastapi import FastAPI, HTTPException
from ..services.auth.tokenAuth import AuthHandler
from fastapi.encoders import jsonable_encoder
from ..models.redis.redisdb import SessionRedis

authHandler = AuthHandler()
functionsAux = FunctionsAux()
user_repository = UserRepository()
session = SessionRedis()

class UserService():
    
    def validate_dados(self, body):
        if not functionsAux.validar_email(body["email"]):
            raise HTTPException(status_code=400, detail="Email invalido")
        
        if "cpf" in body:
            if not functionsAux.validar_cpf(body["cpf"]):
                raise HTTPException(status_code=400, detail="cpf invalido")
        
        if not functionsAux.validar_telefone(body["phone_number"]):
            raise HTTPException(status_code=400, detail="Telefone invalido")
        
        return True
        
    def insert_user(self, body: list):
        self.validate_dados(body)
        print("adasdasdsads")
        user_created = user_repository.insert(body)
        body["id"]=user_created
        access_token = authHandler.create_access_token(user_created)
        session.addSession(access_token, body)
        return access_token
         
    def get_user(self, cpf: str):
        return user_repository.select(cpf)
        
    def delete_user(self, cpf: str, token: str ):
        user_session = session.getSession(token)
        user_repository.delete(cpf, user_session["id"])
        return user_session
        
    def update_user(self, body: list, cpf: str, token:str):
        self.validate_dados(body)
        user_session = session.getSession(token)
        user_repository.update(body, cpf)
        return user_session