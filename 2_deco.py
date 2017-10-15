# decorate open so that the function opens the file in write mode

def deco(fn) :
	def what(name) :
		retrn fn(name, "w")
	return what

open = deco(open)
