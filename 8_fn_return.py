def f1():
	1729 # no default return mechanism
res = f1()
print(res, type(res)) # None

def f2() :
	return 1729
res = f2()
print(res, type(res)) # int


def f3() :
	if n == 1 :
		return 1729
	else:
		return "ramanujan"
n = 1
res = f3()
print(res, type(res))  
n = 0
res = f3()
print(res, type(res))  

# return anything
def f4() :
	return { "one" : "ondu", "two" : 2, "some" : [3, 4, 5] }
res = f4()
print(res, type(res)) # 

def f5(x) :
	return x * x

res = f5(10)
print(res)

def f6(x) :
	return f5(x)

res = f6(10)
print(res)

# function returning a function back
def f7() :
	return f5

res = f7()
print(res)
print(res(11))
print(f7()(12))





















