import redis, json, os

class SessionRedis():
    def __init__(self) -> None:
        try:
            self._host = os.environ['REDIS_HOST']
            print(self._host)
            pool = redis.ConnectionPool(host=self._host, port=6379, db=1)
            self.redis = redis.Redis(connection_pool=pool)
        except redis.RedisError as re:
            raise {"Erro ao conectar com o redis", re}
        
    def addSession(self, token, data):
        try:
            return self.redis.setex(token, 15000, json.dumps(data))
        except redis.RedisError as re:
            raise re
    
    def getSession(self, token):
        try:
            dbSessionUser = self.redis.get(token)
            return json.loads(dbSessionUser)
        except redis.RedisError as re:
            raise re