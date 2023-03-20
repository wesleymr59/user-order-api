from ..models.mySql.repository.user_repository import UserRepository
from .functions import FunctionsAux
from fastapi import FastAPI, HTTPException
from ..services.auth.tokenAuth import AuthHandler
from fastapi.encoders import jsonable_encoder
from ..models.redis.redisdb import SessionRedis

_AuthHandler = AuthHandler()
_functionsAux = FunctionsAux()
_user_repository = UserRepository()
_session = SessionRedis()
class UserService():
    
    def validate_dados(self, body):
        if not _functionsAux.validar_email(body["email"]):
            raise HTTPException(status_code=400, detail="Email invalido")
        
        if "cpf" in body:
            if not _functionsAux.validar_cpf(body["cpf"]):
                raise HTTPException(status_code=400, detail="cpf invalido")
        
        if not _functionsAux.validar_telefone(body["phone_number"]):
            raise HTTPException(status_code=400, detail="Telefone invalido")
        
    def insert_user(self, body: list):
        self.validate_dados(body)
        user_created = _user_repository.insert(body)
        body["id"]=user_created
        access_token = _AuthHandler.create_access_token(user_created)
        _session.addSession(access_token, body)
        return access_token
    
    def get_user(self, cpf: str):
        return _user_repository.select(cpf)
        
    def delete_user(self, cpf: str, token: str ):
            user_session = _session.getSession(token)
            _user_repository.delete(cpf, user_session["id"])
            return user_session
        
    def update_user(self, body: list, cpf: str, token:str):
        
        self.validate_dados(body)
        user_session = _session.getSession(token)
        _user_repository.update(body, cpf)
        return user_session