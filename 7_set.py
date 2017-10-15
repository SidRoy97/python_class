# set
#	no duplicates; used for deduplication
a = set(range(10))
b = set(range(1, 20, 2))
print(a)
print(b)
print(a & b) #intersection
print(a | b) # union
print(a - b) # set difference
print(a ^ b) # symmetric difference

c = { 'cat', 'dog', 'ant', 'bat' }
d = { 'ant', 'dog', 'egg', 'fish' }
print(c & d)



