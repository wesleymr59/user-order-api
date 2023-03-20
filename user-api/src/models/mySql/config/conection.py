from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DBConnectionHandler:

    def __init__(self) -> None:
        try:

            self._host = os.environ['MYSQL_HOST']
            self._port = os.environ['MYSQL_PORT']
            self._user = os.environ['MYSQL_USER']
            self._pass = os.environ['MYSQL_PASSWORD']
            self._db = os.environ['MYSQL_DATABASE']
        except KeyError as error:
            print(f"Error in database environment variables: {error}", flush = True)

        self.__connection_string = f'mysql+pymysql://{self._user}:{self._pass}@{self._host}:{self._port}/{self._db}'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()