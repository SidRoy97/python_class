mycount = { }
f = open("y.txt", "r")
all = f.read()
#print(lines)
f.close()
mylist = []
i = 0
for word in all.split():
		i += 1
		if word not in mycount:
			mycount[word] = []
		mycount[word].append(i)
for w in sorted(mycount):
	print(w,  end = " : " )
	for i in mycount[w] :
		print(i, end = " ")
	print()


