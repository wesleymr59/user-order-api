import redis, json, os
from src.configs.enviroments import get_environment_variables

env = get_environment_variables()

class SessionRedis():
    def __init__(self) -> None:
        try:
            self._host = env.REDIS_HOST
            pool = redis.ConnectionPool(host=self._host, port=6379, db=1)
            self.redis = redis.Redis(connection_pool=pool)
        except redis.RedisError as execptRedis:
            raise {"Erro ao conectar com o redis", execptRedis}
        
    def addSession(self, token, data):
        try:
            return self.redis.setex(token, 15000, json.dumps(data))
        except redis.RedisError as execptRedis:
            raise {"Erro ao adicionar sessao ao redis", execptRedis}
    
    def getSession(self, token):
        try:
            dbSessionUser = self.redis.get(token)
            return json.loads(dbSessionUser)
        except redis.RedisError as execptRedis:
            raise {"Erro ao buscar a sessao no redis", execptRedis}