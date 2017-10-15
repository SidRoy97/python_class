# operators
# arithmetic operator
#	+ - * / % ^
print(3 + 4)
print(3 . __add__(4))  # int.__add__(3, 4)
print(int.__add__(3, 4))

print (25 % 4, 25.8 % 4.2)
print ( 2 ** 3)
print ( 2 ** 3 ** 2)
# bitwise
# | & << >> ^ ~
# relational operators
# < > <= >= == != in
#	result is bool
#		True False

print (5 == 5)
print (5 == 5 == 5)  # a op1 b op2 c
# op1, op2 are relational operators
# (a op1 b) and (b op2 c)

print ("cat" == "cat")
print ( (10, 20) == (10, 20))
print ( {10 : 20} == {10 : 30} ) # False
print ( (10, 20) < (10, 30) )
print ( "car" < "cat" )
print ( "car" < "cb") #  
#print ( {10, 20} < {10, 30}) # not to be used; I DO NOT KNOW

print( "apple" < "Apple") # False

# in : membership
print( "a" in "apple")
print("l" in "apple")
print("pl" in "apple")
print(10 in (20, 10, 30))
print( (10, 20) in (10, 20, 30)) # False
print ( (10, 20) in ((10, 20), 30)) 
print (10 in { 20 : 30, 10 : 40 } )
print (30 in { 20 : 30, 10 : 40 } ) # False ; search on keys

# assignment
#	not an expression
a = 10
print(a)
a =  b  = 20
print(a, b)
#a = (b = 20) # error

# + operator
print(10 + 20)
print(2.5 + 3.6)
print((1 + 2j) + (3 + 4j))
print("abc" + "def")  #concatenation
print((10, 20) + (30, 40))  #(10, 20, 30, 40)
print([10, 20] + [30, 40, 50]) 
#print({10:20} + {30:40}) # NO

# *
print(10 * 3)
print("pes" * 3) # replication pespespes
print((10, 20) * 3)  # (10, 20, 10, 20, 10, 20)
print([10, 20] * 3)
print(3 * "pes") 

#---
# assignment
#	no ++ or --
#	no operator with side effect
#	+= -= ...  # not expressions

a = [10, 20]
b = [30, 40]
print(a, id(a))
a += b
print(a, id(a))

a = [10, 20]
b = [30, 40]
print(a, id(a))
a = a + b
print(a, id(a))

# logical operators

# not and or
a = 0
b = 10
print( a == 0 or b / a > 3) # True
print(2 and 4) # not sure

# true 
#	True non-zero-value non-empty-data-structure
# false 
#	False 0 empty-data-structure None























































