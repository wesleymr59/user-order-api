from ..config.conection import DBConnectionHandler
from ..entities.entity import User
from sqlalchemy.orm.exc import NoResultFound, ObjectDereferencedError
import datetime
import pymysql
from sqlalchemy import exc
from fastapi.encoders import jsonable_encoder

class UserRepository():
    def insert(self, body: list):
        with DBConnectionHandler() as db:
            try:
                data_isert = User(name=body["name"], cpf=body["cpf"], email=body["email"], 
                                  phone_number=body["phone_number"], created_at=datetime.datetime.utcnow(),updated_at=datetime.datetime.utcnow())
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
    
    def select(self, cpf: str):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(User.id, User.name, User.email, User.phone_number,
                                        User.created_at, User.updated_at).filter(User.cpf == cpf).one_or_none()
                if data is not None:
                    return data
                else:
                    return None
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback()
                raise exception

    def delete(self, cpf: str, id: int):
        with DBConnectionHandler() as db:
            try:
                db.session.query(User).filter(User.id == id, User.cpf == cpf).delete()
                db.session.commit()
            except pymysql.err.IntegrityError as e:
                db.session.rollback()
            except exc.IntegrityError as e:
                db.session.rollback()
            except Exception as e:
                db.session.rollback()
    
    def update(self, body: list, cpf: str,):
        with DBConnectionHandler() as db:
            try:
                print("doasdpas")
                db.session.query(User).filter(User.cpf == cpf).update({"name":body["name"],
                                                                       "email":body["email"],
                                                                       "phone_number":body["phone_number"],
                                                                       "updated_at":datetime.datetime.utcnow()})
                db.session.commit()
            except pymysql.err.IntegrityError as e:
                db.session.rollback()
            except exc.IntegrityError as e:
                db.session.rollback()
            except Exception as e:
                db.session.rollback()