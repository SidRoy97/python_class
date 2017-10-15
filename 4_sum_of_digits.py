n = input("enter a number : ")
n = int(n)
s = 0
i = 0
while n :
	s += n % 10
	n = int(n / 10)
	i += 1
print(s)
print(i)

