import os
import glob
#print (glob.glob('*'))
#print (list(filter(lambda name : os.path.isfile(name) and 
#		os.path.getsize(name) == 0 , glob.glob('*'))))

# lazy; does not do anything until we force an iteration
#map(os.unlink , filter(lambda name : os.path.isfile(name) and 
#		os.path.getsize(name) == 0 , glob.glob('*')))

list(map(os.unlink , filter(lambda name : os.path.isfile(name) and 
		os.path.getsize(name) == 0 , glob.glob('*'))))

print("the end")
