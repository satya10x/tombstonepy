class Tombstone(object):
	def __init__(self, *args,**kwargs):
		#print args
		self.functions = args

	def __call__(self, f):
		
		def wrapped_f(*args,**kwargs):
			for function in self.functions:
				if hasattr(function, '__call__'):

					resp = function()
					if resp == None:
						return f(*args,**kwargs)
					else:
						return resp()
		return wrapped_f