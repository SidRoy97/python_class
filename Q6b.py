rows = int(input("Rows : "))

p = []

for i in range(rows):
    p.append([])

for i in range(rows):
    p[i].append(1)
    
for i in range(1,rows):
    x = 0
    while(x != len(p[i-1])-1):
        p[i].append(p[i-1][x]+p[i-1][x+1])
        x += 1
    if(x == len(p[i-1])-1):
        p[i].append(1)

x = rows
for i in range(rows):
    print(" "*x,end = "")
    for j in p[i]:
        print(j,end = " ")
    print()
    x -= 1
    
        
       
        
