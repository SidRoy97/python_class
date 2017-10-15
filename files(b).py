f1 = open("file1.txt")
f2 = open("file2.txt")
f3 = open("file3.txt","w")

contents1 = f1.read()
contents2 = f2.read()

contents1 = contents1.split("\n")
contents2 = contents2.split("\n")

i = 0; j = 0
while(i<len(contents1) and j<len(contents2)):
    if(contents1[i]<contents2[j]):
        f3.write(contents1[i]+"\n")
        i += 1
    else:
        f3.write(contents2[j]+"\n")
        j += 1

if(i == len(contents1)):
    while(j<len(contents2)):
        f3.write(contents2[j]+"\n")
        j += 1
else:
    while(i<len(contents1)):
        f3.write(contents1[i]+"\n")
        i += 1
f1.close()
f2.close()
f3.close()
