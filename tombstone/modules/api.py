from controller import TombController 
import json

class TombView(object):
	def __init__(self):
		pass

	@staticmethod
	def get_data(type=None):
		""" Gets data in json form"""
		tomb = TombController()
		data = tomb.get_all_data()
		return json.dumps(tomb.compute_access_log(data))

	@staticmethod
	def remove_data(key):
		"""Removes data of a key from cache"""

		tomb = TombController()
		if tomb.remove_data(key):
			return True
		else:
			return False

	@staticmethod
	def remove_all_data():
		""" Cleans up redis cache"""

		tomb = TombController()
		if tomb.remove_all_data():
			return True
		else:
			return False