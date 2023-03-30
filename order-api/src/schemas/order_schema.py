import datetime
from pydantic import BaseModel, Field


class OrderResponse(BaseModel):
    id: int
    user_id: int
    item_description: str
    item_quantity: int
    item_price: int
    total_value: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    class Config:
        orm_mode = True

class userUpdate(BaseModel):
    name: str
    email: str
    phone_number: str
    
class orderBody(BaseModel):
    item_description : str | None = Field(
        default=None, title="Descrição do pedido", max_length=300
    )
    item_quantity : int
    item_price: int
    
    class Config:
        orm_mode = True
