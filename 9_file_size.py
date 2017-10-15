import os
import glob
#print(glob.glob('*'))
#res = list(map(os.path.getsize , glob.glob('*')))
#print(res)


#res = list(map(lambda name : (name, os.path.getsize(name)) , glob.glob('*')))
#print(res)

# find the size of files alone and not directories
print(list(map( lambda name :  (name, os.path.getsize(name)) , filter(os.path.isfile , glob.glob('*')))))


