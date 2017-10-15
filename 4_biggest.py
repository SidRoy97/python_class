import os
import glob
# all names
#print(glob.glob('*'))
# pick files
#print(list(filter(os.path.isfile, glob.glob('*'))))
# sizes
#print(list(map(os.path.getsize, filter(os.path.isfile, glob.glob('*')))))

# filename and size
#print(list(map(lambda name : (name, os.path.getsize(name)), filter(os.path.isfile, glob.glob('*')))))

# find biggest
#print(max(map(lambda name : (name, os.path.getsize(name)), filter(os.path.isfile, glob.glob('*'))), key = lambda pair : pair[1]))

# just the name
print(max(map(lambda name : (name, os.path.getsize(name)), filter(os.path.isfile, glob.glob('*'))), key = lambda pair : pair[1])[0])
















