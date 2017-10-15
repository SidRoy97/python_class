f = open("y.txt", "r")
lines = f.readlines()
print(lines)
f.close()
mylist = []
for line in lines:
	for word in line.split() :
		if word not in mylist: 
			mylist.append(word)
print(mylist)

