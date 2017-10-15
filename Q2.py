n = int(input("Rows : "))

print()
print()

for i in range(n):
    for j in range(n):
        if(i == j):
            print("1", end = " ")
        else:
            print("0", end = " ")
    print()

print()
print()

for i in range(n):
    sum = 0
    for j in range(i+1):
        if(i == j):
            sum += j + 1
            print(j+1,end = " = ")
        else:
            sum += j + 1
            print(j+1,end = " + ")
    print(sum)

print()
print()

x=n*3
for i in range(n):
    sum = 0    
    print(" "*x,end = "")
    for j in range(i+1):
        if(i == j):
            sum += j + 1
            print(j+1,end = " = ")
        else:
            sum += j + 1
            print(j+1,end = " + ")
    x -= 4
    print(sum)
