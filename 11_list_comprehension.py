# list comprehension
a = [ x for x in range(5) ]
print(a, type(a))
a = [ x * x for x in range(5) ]
print(a, type(a))
a = [ x + "s" for x in ['ant', 'bat', 'cat'] ]
print(a)
a = [ (x, x * x) for x in range(5) ]
print(a, type(a))

a = [(x, y) for x in [1, 2, 3] for y in [4, 5] ]
print(a)

a = [ x * x for x in range(5) if x % 2 ]
print(a, type(a))

a = [(x, y) for x in [1, 2, 3] for y in [1, 2, 3]
	  if x < y ]
print(a)

