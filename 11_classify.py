all = input("enter 3 sides of a triangle separated by space : ")
#print(all.split())
(a, b, c) = all.split()
a = int(a); b = int(b); c = int(c)

if a == b : 
	if b == c :
		print("Equi")
	else:
		print("iso")
elif b == c :
	print("iso")
elif c == a :
	print("iso")

else:
	print("scalene")

