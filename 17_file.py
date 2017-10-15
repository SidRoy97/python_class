mycount = { }
f = open("y.txt", "r")
all = f.read()
#print(lines)
f.close()
mylist = []
for word in all.split():
		if word not in mycount:
			mycount[word] = 0
		mycount[word] += 1
for w in mycount:
	print(w, " : ", mycount[w])

