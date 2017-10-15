def mymap(f, seq) :
	res = []
	for e in seq :
		res.append(f(e))
	return res

print(mymap(lambda x : x *  x, range(5)))

def myfilter(f, seq) :
	res = []
	for e in seq :
		if f(e) :
			res.append(e)
	return res

print(myfilter(lambda x : x % 2, range(5)))



def f(x) : return x * x
def g(x) : return x * x * x

def apply(x, *fn) :
	for op in fn :
		x = op(x)
	return x

print(apply(2, f, g))









