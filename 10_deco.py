#
"""
def foo() :
	print('foo called')

foo()
"""
"""
def what(f) :
	f()

def foo() :
	print('foo called')

what(foo)
"""
"""
def what(f) :
	print("this is f")
	f()

def foo() :
	print('foo called')

what(foo)
"""

"""
def what(f) :
	def another() :
		print("this is f")
		f()
	another()

def foo() :
	print('foo called')

what(foo)
"""
"""
def what(f) :
	def another() :
		print("this is f")
		f()
	return another

def foo() :
	print('foo called')

what(foo)()
"""
"""
def what(f) :
	def another() :
		print("this is f")
		f()
	return another

def foo() :
	print('foo called')

bar = what(foo) 
bar()
"""
#Decorator
"""
def what(f) :
	def another() :
		print("this is f")
		f()
	return another

def foo() :
	print('foo called')

foo = what(foo) 
foo()
"""
"""
def what(f) :
	def another() :
		print("this is f")
		f()
	return another
def what1(f) :
	def test() :
		print("this is another fn")
		f()
	return test

def foo() :
	print('foo called')

foo = what1(what(foo)) 
foo()

"""

def what(f) :
	def another() :
		print("this is f")
		f()
	return another
def what1(f) :
	def test() :
		print("this is another fn")
		f()
	return test
@what1
@what
def foo() :
	print('foo called')


foo()






