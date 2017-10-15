f = open("books.txt")
all = { }
line = f.readline()
while line:
	line = line.strip()
	(lang, author, title) = line.split(":")
#	print(lang)
#	print(author)
#	print(title)
	if lang not in all :
		all[lang] = {}
	if author not in all[lang] :
		all[lang][author] = []
	all[lang][author].append(title)
	line = f.readline()

f.close()
#print(all)
for lang in all:
	print(lang)
	for author in all[lang]:
		print("\t", author)
		for title in all[lang][author]:
			print("\t\t", title)




