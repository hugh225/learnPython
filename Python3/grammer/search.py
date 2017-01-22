#!/usr/bin/env python
import os
import sys


def search(path, s):
	for x in os.listdir(path):
		fpath = os.path.join(path, x)
		if os.path.isfile(fpath) and s in x:
			print(fpath)
		elif os.path.isdir(fpath):
			search(fpath, s)

if len(sys.argv) == 1:
	print("Usage:Python search in current dir, please input 1 parameter: search.py [string you want to search]")
elif len(sys.argv) == 2:
	s = sys.argv[1]
	search('.', s)
else:
	print('Parameters error!')
