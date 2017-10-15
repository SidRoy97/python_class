
def add_list(mylist, key) :
	temp = {
		'key' : key,
		'next' : None
	}
	if mylist['head'] == None :
		mylist['head'] = temp
	else:
		mylist['tail']['next'] = temp
	mylist['tail'] = temp;

def disp_list(mylist):
	temp = mylist['head']
	while temp :
		print(temp['key'])
		temp = temp['next']

mylist = {
	'head' : None,
	'tail' : None
}

for i in range(5) :
	add_list(mylist, i * i)
disp_list(mylist)

