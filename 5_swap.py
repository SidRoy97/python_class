a = 10; b = 20
a, b = b, a
print(a, b)
a = [10, 20]; b = [30, 40]
a, b = b, a
print(a, b)

def myswap(x, y) :
	(x, y) = (y, x)

a = 10; b = 20
myswap(a, b)
print(a, b)

a = [10, 20]; b = [30, 40]
myswap(a, b)
print(a, b)

def f() : print("one")
def g() : print("two")
f, g =  g, f
f()
g()



















