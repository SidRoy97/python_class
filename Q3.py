a = []
n=10

while(n>0):
    a.append(int(input()))
    n -= 1

n = 1

b = []
while(n<10):
    b.append(a[n] - a[n-1])
    n += 1

print("Fall of wickets : ",a)
print("Partnerships : ",b)
print("Max partnership : ",max(b))
