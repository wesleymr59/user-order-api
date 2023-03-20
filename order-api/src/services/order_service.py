from fastapi import HTTPException
from ..models.redis.redisdb import SessionRedis
from ..models.mySql.repository.order_repository import OrderRepository


_user_repository = OrderRepository()
_session = SessionRedis()

class OrderService():
    def crete_value_total(self, body: list):
            total_value =  body["item_price"] * body["item_quantity"]
            body["total_value"] = total_value
            return body
            
    def create_order(self, bodyRequest: list, token:str):
            body = self.crete_value_total(bodyRequest)
            id_user = _session.getSession(token)
            body["user_id"] = id_user["id"]
            order_id = _user_repository.insert_order(body)
            return _user_repository.select_by_id(order_id)
            
    def get_order_user(self, token:str):
            user_session = _session.getSession(token)
            return _user_repository.select_orders_user(user_session["id"])
    
    def get_all_orders(self):
            return _user_repository.select_all_orders()
    
    def delete_all_order_user(self, token: str ):
            user_session = _session.getSession(token)
            all_order = _user_repository.select_orders_user(user_session["id"])
            _user_repository.delete(user_session["id"])
            return all_order
    
    def delete_order(self, id_order: int):
            order = _user_repository.select_orders(id_order)
            _user_repository.delete_order(id_order)
            return order
    
    def update_order(self, bodyRequest: list, id: str):
        body = self.crete_value_total(bodyRequest)
        _user_repository.update(body, id)
        return _user_repository.select_by_id(id)