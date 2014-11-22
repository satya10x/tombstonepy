import tombstone
import datetime

class HelloWorld:
	def __init__(self):
		pass

	#time isn't a necessary argument. If not provided, it takes the current time.
	# module name needs to be there
	@tombstone.logs(module_name="HelloWorld", time=datetime.datetime.now())
	def test_it(self):
		print "dance basanti"

	@tombstone.logs(module_name="HelloWorld", time=datetime.datetime.now())
	def test_it_more(self):
		print "dance basanti"

hel = HelloWorld()
hel.test_it()
hel.test_it_more()