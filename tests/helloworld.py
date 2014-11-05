import tombstone

def print_Wal():
	print "wal"
	return None

class HelloWorld:
	def __init__(self):
		pass

	@tombstone.logs(print_Wal)
	def test_crap(self):
		print "why"


hel = HelloWorld()
hel.test_crap()