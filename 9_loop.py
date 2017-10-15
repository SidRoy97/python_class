# loop
# 'C'
# i = 1
# n = 5
# while(i <= n)
# {
#		printf("%d", i);
#		i++;
# }

# while stat :
#	while <expr> 
#		<body>
#	use indentation to indicate the body belongs to the while

# leader:
#	suite

i = 1
n = 5
while i <= n :
	print(i, end = " ")
	i += 1
print()

i = 1
n = 5
while i <= n :
 print(i, end = " ")
 i += 1
print()

# not ok in 3.x
"""
i = 1
n = 5
while i <= n :
	print(i, end = " ")# tab
    i += 1 # 4 spaces
print()

"""
"""
i = 1
n = 5
while i <= n :
	print(i, end = " ")
		i += 1 # cannot increase indentation unless the earlier
		# statement is a leader
print()
"""

i = 1
n = 5
while i <= n :
	j = 1
	while j <= i :
		print(j, end = " ")
		j += 1
	i += 1 
	print()










