f = open("y.txt", "r")
lines = f.readlines()
#print(lines)
unique = []
for line in lines:
    for words in line.split():
        if(words not in unique):
            unique.append(words)
print("unique_words : ",unique)


lines2 = "".join(lines)

print(list(map(lambda x : (x,lines2.count(x)),unique)))

print("TO CHECK IF A WORD EXISTS IN THE FILE")

w = input("Enter a word : ")

if(w in lines2):
    print(w,"exists in the file")
else:
    print(w,"DOESN'T exists in the file")
f.close()
    
        
