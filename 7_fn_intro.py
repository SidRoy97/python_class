# functions:
#	definition
#	invocation
#	return mechanism
#		return a function?
#	parameter passing
#		overloading?
#	static variable?
#	nested function
#	multiple entry?
#	generator ; yield
#	jmp across fns ?
#	recursion
#	referencing environment
#	callback
#	closure
#	decorator

# define a function
# keyword : def
#	followed by the fnname
#	parentheses
#		names of parameters within parentheses
#	:

#   then the body
#	there is no type for the function
#			 no type for the parameters

# can I call the fn before defn? NO
#foo()

def foo():
	print("hello from foo")

# invoke
# fnname followed by parenthese and arguments within parentheses

foo()

def f1() :
	print("f1")
	f2()

def f2() :
	print("f2")

f1()


def f3():
	print("f3")

f4 = f3
print(f3, type(f3))
print(f4, type(f4))

del f3
f4()
print(f4, type(f4))






















