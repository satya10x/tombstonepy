import datetime
import calendar
from redis_api import RedisApi

class TombController:
	def __init__(self):
		pass

	def store_data(self, module_name, func_name, data, data_type):
		"""I am so bored wondering about the structure of
			redis cache that I'm staring at Shradhha Kapoor
			dance around to Dance Basanti. Save me! 
		"""
		# create key based upon data type
		key = self.create_key(module_name, func_name, data_type)
		# store data in redis
		try:
			RedisApi().set_value_from_hash("ts", key, str(data))
		except:
			raise

	def get_data(self, module_name, func_name):
		pass

	def get_all_data(self):
		return RedisApi().get_all_values_from_hash("ts")

	def create_key(self, module_name, func_name, data_type):
		""" Creates key to store data in cache(redis or otherwise.
			Keys are created based upon the data type and a unix 
			timestamp is added to it.

			Edit 1: I've decided to go with HMSET and store both the
					execution time and access time log with the same 
					hash because Gori tera thumka bada kinky 
					kinky type da!

			Edit 2: HMSET is not helping me much when it comes to
					data retrieval because Gori tera jhumka
					bada funky funky type da!

					I am not doing Redis data type jokes here! 

			Edit 3: Okay, I'm going to use Hash. 
					HSET ts module_name:func_name:data_type:time_stamp 
					So, I can retrieve the data doing HGETALL ts. 

		"""

		if data_type == "access_log":
			# create key for access log
			return (module_name + ":" + func_name + ":" 
				+ data_type + ":" + str(self.get_unix_time_stamp()))

		elif data_type == "execution_log":
			# create key for execution log
			return (module_name + ":" + func_name 
					+ ":" + data_type + ":" + str(self.get_unix_time_stamp()))
	
	def get_unix_time_stamp(self):
		return calendar.timegm(datetime.datetime.utcnow().timetuple())
	
	def compute_access_log(self, data):
		""" Computes from cached data and returns
			* Average execution time. 
			* Total count of usage
			* Last usage. 
			* function name 
			* module name 
		"""
		for datum in data:
			print datum

	def compute_execution_time(self, data):
		pass



