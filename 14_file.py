f = open("place.txt")
files = { }
line = f.readline()
while line:
	line = line.strip()
	(city, place) = line.split(":")
#	print(city, place)
	if city not in files:
		files[city] = open(city, "w")
	print(place, file = files[city])
	line = f.readline()

f.close()

for ff in files.values() :
	ff.close()
