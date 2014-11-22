from controller import TombController 

class TombView(object):
	def __init__(self):
		pass

	@staticmethod
	def show_data():
		""" Shows data in tabular form in a html page"""
		tomb = TombController()
		data = tomb.get_all_data()
		tomb.compute_access_log(data)
		return "Hello world!"

	@staticmethod
	def get_json_data():
		"""Returns json data"""
		pass
