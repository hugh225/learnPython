#！/usr/bin/env python
#change name
import os

def rename(path, newname):
	path = '.'
	count = 1
	for x in os.listdir(path):
		fpath = os.path.join(path, x)
		if os.path.isfile(fpath) and os.path.splitext(x)[1] not in ['.py', '.db'] :
			oldpath = fpath
			newpath = os.path.join(path, newname + str(count) + os.path.splitext(x)[1])
			os.rename(oldpath, newpath)
			count += 1
		else:
			continue
			
path = input("path:")
newname = input("newname:")
rename(path, newname)