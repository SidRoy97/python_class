# for statement
# for <variable> in <iterable> :
#	<suite>
# for loop : to walk through something
#			
for i in [ 'kalidasa', 'bhasa', 'baana' ] :
	print(i)

print(range(5))

for i in range(5) :
	print(i)

print(list(range(5, 10)))
print(list(range(5, 10, 2)))

#for i in 1729 : # int is not iterable
#	print("fool")

# string is iterable
for i in "pes" : 
	print(i)

for i in [ "pes" ] :
	print("stupid") # once

# slicing
a = [11, 22, 33, 44, 55, 66, 77, 88]
print(a[2:4])
print(a[2:8:2])
print(a[2:]) # final : len(a)
print(a[:4]) # init : 0

a = [11, 22, 33, 44, 55, 66, 77, 88]
a[2:4] = [100, 200]
print(a)

a = [11, 22, 33, 44, 55, 66, 77, 88]
a[2:4] = [3, 4, 5, 6]
print(a)

a = [11, 22, 33, 44, 55, 66, 77, 88]
a[2:4] =  "apple"
print(a)

#
a = [11, 22, 33, 44, 55, 66, 77, 88]
a[2:3] =  "apple"
print(a)

a = [11, 22, 33, 44, 55, 66, 77, 88]
a[2] =  "apple"
print(a)


a = [11, 22, 33, 44]
for i in a :
	i = 100
print(a) # no change

a = [[11], [22], [33], [44]]
for i in a :
	i = [100]
print(a) # no change


a = [[11], [22], [33], [44]]
for i in a :
	i += [100]
print(a) #  changes

a = [[11], [22], [33], [44]]
for i in a :
	i = i + [100]
print(a) #  no change 














































