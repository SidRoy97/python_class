# decorator
def pre_process(f) :
	def what() :
		print("pre processing")
		f()
	return what

def post_process(f) :
	def what() :
		f()
		print("post processing")
	return what

def foo() :
	print("processing ...")

foo = post_process(pre_process(foo))
foo()

