# q1
for i in range(5) :
	print("one", end = " ") # five times
print()

for i in [range(5)] :
	print("two", end = " ")   # once
print()

for i in (range(5)) :
	print("three", end = " ") # five times
print()

print((3, 4) * 5) # (3, 4, 3, 4, 3, 4, 3, 4, 3, 4)
print( (3) * 5) # 15

a = (3)
b = (3,)
print(a, type(a)) # int
print(b, type(b)) # tuple
c = ()
print(c, type(c)) # tuple

d = { }
print(d, type(d)) # dict
e = set()
print(e, type(e)) # set

















