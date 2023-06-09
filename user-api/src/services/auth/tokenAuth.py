import os
from fastapi import FastAPI, status, HTTPException
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from src.configs.enviroments import get_environment_variables

env = get_environment_variables()

# replace it with your 32 bit secret key
SECRET_KEY = env.ENV_TOKEN

# encryption algorithm
ALGORITHM = "HS256"

class AuthHandler(): 
    def create_access_token(self, user: int):
        data = {
            'sub': str(user),
            'from': 'app-user'
        }
        
        to_encode = data.copy()

        expire = datetime.utcnow() + timedelta(minutes=999)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

        return encoded_jwt

    async def get_token(self):
        try:

            data = {
                'sub': 'secret information',
                'from': 'app-user'
            }
            token = self.create_access_token(data=data)
            return {'token': token}
        except JWTError:
            raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=JWTError,
        )

    def verify_token(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if payload:
                return token
        except JWTError:
            raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="token inválido"
        )
