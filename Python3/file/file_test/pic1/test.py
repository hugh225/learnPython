#!/usr/bin/env python
import os

def search(path, s):
	for f in os.listdir(path):
		fpath = os.path.join(path, f)
		if os.path.isfile(fpath) and s in f:
			 print(fpath)
		elif os.path.isdir(fpath):
			search(fpath, s)

path = input("path:")
s = input("search string:")
search(path, s)