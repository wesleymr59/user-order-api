import datetime
import pymysql
from sqlalchemy import exc
from ..entities.entity import Order
from ..config.conection import DBConnectionHandler
from sqlalchemy.orm.exc import NoResultFound


class OrderRepository():
    def insert_order(self, body: list):
        with DBConnectionHandler() as db:
            try:
                data_isert = Order(user_id=body["user_id"], item_description=body["item_description"], item_quantity=body["item_quantity"], 
                                  item_price=body["item_price"], total_value=body["total_value"], created_at=datetime.datetime.utcnow(), updated_at=datetime.datetime.utcnow())
                db.session.add(data_isert)
                db.session.commit()
                db.session.refresh(data_isert)
                return data_isert.id
            except pymysql.err.IntegrityError as e:
                db.session.rollback()
            except exc.IntegrityError as e:
                db.session.rollback()
            except Exception as e:
                db.session.rollback()
    
    def select_by_id(self, id: str):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Order.id, Order.user_id, Order.item_description, Order.item_quantity, Order.item_price,  Order.total_value,
                                        Order.created_at, Order.updated_at).filter(Order.id == id).all()
                print(data)
                if data is not None:
                    return data
                else:
                    raise "Object is Null"
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_all_orders(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Order.id, Order.user_id, Order.item_description, Order.item_quantity, Order.item_price,  Order.total_value,
                                        Order.created_at, Order.updated_at).all()
                print(data)
                if data is not None:
                    return data
                else:
                    raise "Object is Null"
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def select_orders_user(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Order.id, Order.user_id, Order.item_description, Order.item_quantity, Order.item_price,  Order.total_value,
                                        Order.created_at, Order.updated_at).filter(Order.user_id == id).all()
                print(data)
                if data is not None:
                    return data
                else:
                    raise "Object is Null"
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_orders(self, id):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Order.id, Order.user_id, Order.item_description, Order.item_quantity, Order.item_price,  Order.total_value,
                                        Order.created_at, Order.updated_at).filter(Order.id == id).all()
                if data is not None:
                    return data
                else:
                    raise "Object is Null"
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    def delete_by_userId(self, id: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Order).filter(Order.user_id == id).delete()
                db.session.commit()
            except pymysql.err.IntegrityError as e:
                db.session.rollback()
            except exc.IntegrityError as e:
                db.session.rollback()
            except Exception as e:
                db.session.rollback()
                
    def delete_order(self, id: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Order).filter(Order.id == id).delete()
                db.session.commit()
            except pymysql.err.IntegrityError as e:
                db.session.rollback()
            except exc.IntegrityError as e:
                db.session.rollback()
            except Exception as e:
                db.session.rollback()           
    
    def update(self, body: list, id: int,):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Order).filter(Order.id == id).update({"item_description":body["item_description"],
                                                                       "item_quantity":body["item_quantity"],
                                                                       "item_price":body["item_price"],
                                                                       "total_value":body["total_value"],
                                                                       "updated_at":datetime.datetime.utcnow()})
                db.session.commit()
            except pymysql.err.IntegrityError as e:
                db.session.rollback()
            except exc.IntegrityError as e:
                db.session.rollback()
            except Exception as e:
                db.session.rollback()