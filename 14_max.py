print(max(20, 10, 40, 30))
a = [20, 10, 40, 30]
print(max(a))
print(max('rama', 'krishna', 'govinda', 'balarama'))
print(max('rama', 'krishna', 'govinda', 'balarama', key = len))

a = [
	[ 'gavaskar', 10000 ],
	[ 'vishwanath', 9000 ],
	[ 'mohindar', 6000 ],
	[ 'azar', 8000 ]
]
print(max(a))
print(max(a, key = lambda pair : pair[1]))

