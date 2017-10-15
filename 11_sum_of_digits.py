
"""
n = input("enter a number : ")
#print(list(map(lambda x : x , n)))
#print(list(map(int , n)))

s = 0
for i in map(int, n) :
	s += i
print(s)
"""

n = input("enter a number : ")
print(sum(map(int, n)))


