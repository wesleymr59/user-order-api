from pydantic import BaseModel, Field
import datetime

class userBody(BaseModel):
    name: str
    cpf: str | None = Field(
        default=None, title="123.123.123-12", max_length=15
    )
    email: str | None = Field(
        default=None, title="email@email.com", max_length=100
    )
    phone_number: str | None = Field(
        default=None, title="14123456789", max_length=15
    )

class userUpdate(BaseModel):
    name: str
    email: str
    phone_number: str
class User(BaseModel):
    id: int
    name : str
    email : str
    phone_number: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    
    class Config:
        orm_mode = True
