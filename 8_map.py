# find the length
a = [ 'kalidasa', 'kuvempu', 'bendre', 'karanta', 'maasti' ]
b = []
for i in a :
	b.append(len(i))
print(b)

# convert to uppercase
a = [ 'kalidasa', 'kuvempu', 'bendre', 'karanta', 'maasti' ]
b = []
for i in a :
	b.append(i.upper())
print(b)

# square each number
a = [ 11, 22, 33, 44]
b = []
for i in a :
	b.append(i * i)
print(b)

# find the length
a = [ 'kalidasa', 'kuvempu', 'bendre', 'karanta', 'maasti' ]
#b = list(map(len  , a))
#print(b)
b = map(len, a)
for i in b :
	print(i)


# convert to uppercase
a = [ 'kalidasa', 'kuvempu', 'bendre', 'karanta', 'maasti' ]
b = list(map(str.upper, a))
print(b)


# square each number
a = [ 11, 22, 33, 44]
b = list(map(lambda y: y * y, a))
print(b)









