def foo(**kw):
	print(kw, type(kw))

foo(poet = 'valmiki', title = 'ramayana', hero = 'rama',
	father = 'dasharatha', mothers = [ 'kousalya', 'kaikeyi', 'sumitra'])

def foo(a, b, *c, **d) :
	print(a, b, c, d)

foo(1, 2, 3, 4, 5, six = 6, seven = 7)
foo(1, 2)
foo(1, 2, 3, 4, 5)
foo(1, 2, six = 6, seven = 7)

#----------------

def divide(a, b = 1) :
	return a / b
print(divide(10, 2))
print(divide(10))

# ----------

def mybutton(**kw) :
	attr = {
		'font' : 'times new roman',
		'size' : 10,
		'bgcolor' : 'white',
		'fgcolor' : 'green',
		'style' : 'normal'
	}
	attr.update(kw)
	print(attr)

mybutton(font = 'calibra', size = 12, style = 'bold', 
	bgcolor = 'blue', fgcolor = 'black')
mybutton()
mybutton(size = 18, bgcolor = 'red')




















