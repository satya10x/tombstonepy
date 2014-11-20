from redis_api import RedisApi

class TombController:
	def __init__(self):
		pass

	def store_data(self, module_name, func_name, data, data_type):
		
		# create key based upon data type
		key = self.create_key(module_name, func_name, data_type)

		# store data in redis
		try:
			RedisApi().set_value(key, data)
		except:
			raise

	def get_data(self, module_name, func_name):
		pass

	def get_all_data(self):
		pass

	def create_key(self, module_name, func_name, data_type):
		if data_type == "access_log":
			return module_name + ":" + func_name + ":" + data_type
		elif data_type == "execution_log":
						return (module_name + ":" + func_name 
								+ ":" + data_type)

	def compute_access_log(self, data):
		pass

	def compute_execution_time(self, data):
		pass



