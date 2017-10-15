# validate the date
temp = [
	None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]
#days = [temp, temp]  # creates aliases
# changing days[1] affects days[0] and temp

days = [temp[:], temp[:]]
days[1][2] = 29
print(days[0])
print(days[1])


line = input('enter the date dd/mm/yyyy : ')
(dd, mm, yy) = line.split('/')
dd = int(dd); mm = int(mm); yy = int(yy)
leap = 0
if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0) :
	leap = 1
if not 1 <= mm <= 12 :
	print('invalid month')
elif not 1 <= dd <= days[leap][mm] :
	print('invalid date')
else:
	print('valid')


