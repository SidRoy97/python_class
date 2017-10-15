with open("x.txt") as f :
	for w in f :
		w = w.strip()
		print(w)

class Ex:
	def __enter__(self) :
		return Ex()
	def close(self) :
		print("close called")
	def __exit__(self, *arg) :
		print("exit called")
		self.close()

with Ex() as ex:
	print("in with")
#	raise NameError
	print("still in with")

