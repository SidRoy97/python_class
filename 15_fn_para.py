#matching based on # of args
# no checking based on type and/or order
def foo(a, b) :
	pass

#foo(10, 20, 30)
#foo(40)

foo(10, 2.5)
foo("sdfdf", {})

a = 0
if a :
	def f(x, y):
		pass
else:
	def f(p, q, r):
		pass

print(f)
#print(f(11, 22))

# no overloading
"""
def ff(x):
	print("one")
ff(1)

def ff(y, z):
	print("two")
ff(2)
"""

# what does this function do?
# polymorphic based on type at runtime
def bar(x, y):
	return x + y

print(bar(3, 4))
print(bar([11, 22], [33, 44, 55]))
print(bar("ssfddf", "r434"))































