# output:
#	print
#	is a built in function
#	? how many arguments
#	? what about expressions
#	? what types of expressions
#	? field separator
#	? record separator
#	? flushing ?
#	?  device ?
# supports variable # of arguments; all are significant
# default field separator : space
# default rec separator : newline
print(3, 4, 5)
print(6, 7)

# sep and end : are parameters of print
# keyword parameter
# in a fn call, we give the parameter name and a value for it
# this is not assignment
# assignment is not an expr
# argument to a fn should be an expr
print(3, 4, 5, sep = " ----- ",  end = "\n-----pes-----\n")
print(6, 7)
print(8, 9)

# evalautes the expr
print(2 + 3)

# any expr

print(3.14)
print(2 + 3j)
print((111,222))
print([1, 2, 3, 4])
print({1:2, 3:4})
print({1, 2, 3, 4})
















