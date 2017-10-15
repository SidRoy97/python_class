# value, type, id
a = 10
print(a, type(a), id(a))
b = 10
print(b, type(b), id(b))
c = 5 + 5
print(c, type(c), id(c))
d = [10, 20]
print(d[0], type(d[0]), id(d[0]))
e = 20
print(e, type(e), id(e))

b = 30
print('a : ', a) # a has not changed


x = "abcd"
y = x
print(x, y)
x = "pqr"
print(x, y)
y = "lmn"
print(x, y)
# every value is reference counted
# when a new variables is associated with the value, the reference count
# 	is incremented
# when a variable is changed, the reference count is decremented
# when the reference count becomes 0, the value is garbage collected

a = [11, 22, 33, 44]
b = a
c = a
 
print(a, id(a))
print(b, id(b))
print(c, id(c))

c = [12, 34]  # does not affect a or b
b[0] = 55 # affect a
print(a, id(a))
print(b, id(b))
print(c, id(c))

# types:
#	value types or simple types or scalar types
#		 a single value
#	ref types or structured types 
#		# of values
#		if we change the reference, others are not affected
#		if we change through the reference, others are affected

a = [[10, 20], [30, 40]]
b = a[0]
c = a[0]
d = a[0][0]
print(a)
d = 111
print(a)
c = [111, 222]
print(a)
#b = 333
#print(a)
b[0] = 300
print(a)



























