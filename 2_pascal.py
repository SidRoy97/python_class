# pascal triangle
n = 5

pt = []
i = 0
while i <= n :
	pt.append([])
	pt[i].append(1)
	j = 1
	while j < i:
		pt[i].append(pt[i-1][j-1] + pt[i-1][j])
		j += 1
	if i != 0 :
		pt[i].append(1)
	i += 1

#print(pt)
i = 0
while i <= n:
	j = 0
	while j <= i :
		print(pt[i][j], end = " ")
		j += 1
	print()
	i += 1

