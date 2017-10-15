# nested function definition
"""
def outer() :
	def inner() :
		print("inner")
	print("outer")

#inner() # NO

#outer()
#inner() # NO
"""
"""
def outer() :
	def inner() :
		print("inner")
	print("outer")
	return inner

f = outer()
f()
"""

def outer(n) :
	def inner() :
		print("inner", n)
	return inner

f1 = outer(10)
f2 = outer(20)

f1()
f2()













