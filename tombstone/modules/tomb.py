import datetime
import inspect
from controller import TombController

class Tombstone(object):
	def __init__(self, *args,**kwargs):
		try:
			self.func_defns = self.validate_func_defns(kwargs)
		except:
			raise("Invalid parameters!")

	def __call__(self, function_name):
		def wrapped_f(*args,**kwargs):
			try:
				
				# stores time of access of function
				self.set_access_log(function_name.__name__)
				
				start_time = datetime.datetime.now()
				result = function_name(*args, **kwargs)
				execution_time =  datetime.datetime.now() - start_time
				milliseconds = ( (execution_time.days * 24 * 60 * 60 + execution_time.seconds) * 1000 
								+ execution_time.microseconds / 1000.0)


				# stores execution time of function
				self.set_execution_time_log(function_name.__name__, milliseconds) 

				# return the control back to its caller
				return result
			except:
				raise
		return wrapped_f

	def validate_func_defns(self, kwargs):
		""" 
			A bunch of valdiations to ensure that random arguments are not sent 
			via the decorator. It has to be either name or time.
			If name isn't there, then take the function name. 
			If time isn't there, take the curent datetime.
		"""

		validated_resp = {}

		try:
			if "module_name" not in kwargs.keys():
				raise ("You have to send the module name in the decorator!")

			# if no of arguments = 1 then check if it has name or time
			if len(kwargs.keys()) == 1:
				if ("time" not in kwargs.keys() or "module_name" not in kwargs.keys()):
					raise Exception("Wrong parameters sent! Check the docs!")

			# if no of arguments = 2 then check if it has name or time
			elif len(kwargs.keys()) == 2:
				if ("time" not in kwargs.keys() and "module_name" not in kwargs.keys()):
					raise Exception("Wrong parameters sent! Check the docs!")

			# if "time" is one of the keys, then it has to be datetime.
			if "time" in kwargs.keys():
				if not (isinstance(kwargs["time"], datetime.datetime)):
					raise Exception("Time has to be a datetime parameter.")

			# create proper response
			validated_resp["time"] = (kwargs["time"] if "time" in kwargs.keys() 
											else datetime.datetime.now())
			validated_resp["module_name"] = kwargs["module_name"]
			
			return validated_resp
		except Exception, e:
			raise

	def set_access_log(self, func_name):
		try:
			TombController().store_data(self.func_defns["module_name"], func_name,
									self.func_defns["time"], "access_log")
		except:
			raise

	def set_execution_time_log(self, func_name, execution_time):
		try:
			TombController().store_data(self.func_defns["module_name"], func_name,
									execution_time, "execution_log")
		except:
			raise
