from controller import TombController 
import json

class TombView(object):
	def __init__(self):
		pass

	@staticmethod
	def get_data(type=None):
		""" Shows data in tabular form in a html page"""
		tomb = TombController()
		data = tomb.get_all_data()
		return json.dumps(tomb.compute_access_log(data))
