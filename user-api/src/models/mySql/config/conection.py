from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.configs.enviroments import get_environment_variables

env = get_environment_variables()
class DBConnectionHandler:

    def __init__(self) -> None:
        try:
            self._host = env.MYSQL_HOST
            self._port = env.MYSQL_PORT
            self._user = env.MYSQL_USER
            self._pass = env.MYSQL_PASSWORD
            self._db = env.MYSQL_DATABASE
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