# default parameters
"""
def f1(a, b, c = 10, d = 20) :
	print(a, b, c, d)
f1(1, 2, 3, 4)
f1(1, 2, 3)
f1(1, 2)
"""
"""
def f1(a, b, c = (12, 23), d = {11:22}) :
	print(a, b, c, d)
f1(1, 2, 3, 4)
f1(1, 2, 3)
f1(1, 2)
"""
# defaults are processed when the leader is processed and not
# when the fn is called
"""
x = 10
def f1(a, b, c = x):
	print(a, b, c)
x = 20
f1(1, 2, 3)
f1(1, 2)
"""

def foo(e, x = []) :
	x.append(e)
	return x

print(foo(10))
print(foo(20))
a = [12, 23]
print(foo(34, a))
print(foo(100))




















