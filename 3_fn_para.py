# variable # of args; corresponding parameter is a tuple
def foo(*x):
	print(type(x))
	for i in x :
		print(i, end = " ")
	print()

foo("we", "love", "python", "very", "much")
foo("we", "are", "the", "world")

"""
def bar(*p, *q) :
	pass
bar(1, 2, 3, 4, 5, 6)
"""

def bar(a, b, *c):
	print(a, b, c, end = " ")
	print()

bar(1, 2)
bar(1, 2, 3)
bar(1, 2, 3, 4)

def bar(*c, a, b):
	print(a, b, c, end = " ")
	print()

# variable # of parameter cannot be keyword
#bar(c = (11, 22), a = 1, b = 2)
bar(11, 22, a = 1, b = 2)







