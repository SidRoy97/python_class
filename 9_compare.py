f1 = open("x.txt")
f2 = open("y.txt")

#for w in f1:
#	print(w)
# common words
#for w in set(f1) & set(f2) :
#	w = w.strip()
#	print(w)
print(list(map(str.strip, set(f1) & set(f2))))
f1.close()
f2.close()
