f = open("dept_emp.txt")

lines = f.read().split("\n")

f.close()

d1 = {}
d2 = {}

for i in lines:
    x = i.split(":")
    d1[x[0]] = x[1]

print(d1)

for i in lines:
    x = i.split(":")
    x[1] = x[1].split(",")
    d2[x[0]] = x[1]

print(d2)
