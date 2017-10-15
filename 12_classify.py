all = input("enter 3 sides of a triangle separated by space : ")
#print(all.split())
(a, b, c) = all.split()
a = int(a); b = int(b); c = int(c)

equi = a == b == c
iso = (a == b || b == c || c == a) and not equi
scalene = not equi and not iso
if equi :
	print ('equi')
if iso :
	print('iso')
if scalene:
	print('scalene')

	
