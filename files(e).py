f1 = open("file_cmp1.txt")
f2 = open("file_cmp2.txt")

lines1 = f1.read().split("\n")
lines2 = f2.read().split("\n")

f1.close()
f2.close()

if(len(lines1)>len(lines2)):
    print("file_cmp1.txt has more lines")
else:
    print("file_cmp2.txt has more lines")

sameLines = []
file1 = []
file2 = []

for i in lines1:
    if(i in lines2):
        sameLines.append(i)
    else:
        file1.append(i)

for i in lines2:
    if(i not in sameLines):
        file2.append(i)

print("Same lines : ")
for i in sameLines:
    print(i)
print("Lines exclusive in file_cmp1.txt : ")
for i in file1:
    print(i)
print("Lines exclusive in file_cmp2.txt : ")
for i in file2:
    print(i)        
