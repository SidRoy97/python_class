import os
import glob
#print([name for name in glob.glob('*')])
#print([name for name in glob.glob('*') if os.path.isfile(name)])
#print([os.path.getsize(name) for name in glob.glob('*') if os.path.isfile(name)])
#print([(name, os.path.getsize(name)) for name in glob.glob('*') if os.path.isfile(name)])
# dict comprehension
res = {name : os.path.getsize(name) for name in glob.glob('*') if os.path.isfile(name)}
#print(res, type(res))
for name in sorted(res, key = lambda name : res[name], reverse = True) :
	print(name, res[name])
