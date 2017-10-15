# dict
#	has key value pairs
#	order of storing not defined
#	uses hashing
a = { 'apple' : 'fruit', 'bat' : 'cricket', 'cat' : 'mammal' }
print(a)
# value
print(a['apple'])

a['apple'] = 'turing'
print(a['apple'])

a['water'] = 'archimedes'
print(a)

del a['water']
print(a)

print(a.keys())
print(a.values())

print(list(a.keys()))
print(list(a.values()))


