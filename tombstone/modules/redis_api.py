import redis

redis_conf = {"HOST": "localhost",
			 "PORT": 6379, 
			 "db": 0}


redis_ts = redis.StrictRedis(host=redis_conf["HOST"], port=redis_conf["PORT"], db=redis_conf["db"])

class RedisApi(object):
	""" A base api to deal with getters/setters for Redis. """
	def __init__(self):
		pass

	def get_value(self, key):
		try:
			return redis_ts.get(key)
		except:
			raise

	def set_value(self, key, value):
		try:
			return redis_ts.set(key, value)
		except:
			raise

	def get_value_from_hash(self, r_hash, field):
		try:
			return redis_ts.hget(r_hash, field)
		except:
			raise

	def set_value_from_hash(self, r_hash, field, value):
		try:
			return redis_ts.hset(r_hash, field, value)
		except:
			raise

	def get_all_value_from_hash(self, r_hash):
		return redis_ts.hgetall(r_hash)

	def delete(self, key):
		return redis_ts.delete(key)

	def get_keys(self, pattern):
		return redis_ts.keys(str(pattern))

	def key_exists(self, key):
		return redis_ts.exists(key) 