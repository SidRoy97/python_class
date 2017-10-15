f = open("x.txt", "r")
line = f.readline()
while line:
	line = line.strip()
	print(line)
	line = f.readline()
f.close()

