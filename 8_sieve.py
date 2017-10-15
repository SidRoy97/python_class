# sieve of Eratosthenes
#	fastet method of generating prime numbers
#	no division
#	time space trade off
#	uses more space to gain in time

# get n
# initialize sieve with numbers from 2 to n
# while the sieve is not empty
#		get the smallest number
#		that is a prime
#		remove that number and its multiples

n = 100000
sieve = set(range(2, n + 1))
#print(sieve)
while sieve :
	prime = min(sieve)
	print(prime, end = "\t")
	sieve -= set(range(prime, n + 1, prime))













