import tombstone
import datetime

class HelloWorld:
	def __init__(self):
		pass

	@tombstone.logs(module_name="hi", time=datetime.datetime.now())
	def test_crap(self):
		print "why"


hel = HelloWorld()
hel.test_crap()