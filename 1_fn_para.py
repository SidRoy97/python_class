# parameter passing
def f(a, b, c, d) :
	print(a, b, c, d)

# positional parameters
f(1, 2, 3, 4)
#keyword parameter
f(b = 2, d = 4, c = 3, a = 1)
# combine
f(1, 2, d = 4, c = 3)  #these are not assignment operators
# assignment is not an expr
#print(d)


def foo(a, b, c = 11, d = 22) :
	print(a, b, c, d)

foo(1, 2, 3, 4)
foo(1, 2, d = 4)
foo(1, 2, 3, d = 5)
foo(1, 2)

print("-" * 50)
def myrange(init, final = None, step = 1):
	if final == None:
		final = init
		init = 0

	res = []
	i = init
	if step >= 0:
		while i < final :
			res.append(i)
			i += step
	else:
		while i > final:
			res.append(i)
			i += step

	return res

print(myrange(5))
print(myrange(5, 10))
print(myrange(5, 10, 2))
#print(myrange())

"""
range = myrange
print(range(5))
print(range(5, 10))
print(range(5, 10, 2))
"""
print(myrange(10, 5, -1))














