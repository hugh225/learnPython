#!/usr/bin/env python
from datetime import datetime
import os

# pwd = os.path.abspath('.')

print('       Size  Last Modified      Name')
print('----------------------------------------------------')

for f in os.listdir('.'):
	fsize = os.path.getsize(f)
	mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
	flag = '/' if os.path.isdir(f) else ''#目录标志位
	print('%10d %s    %s%s' %(fsize,mtime,f,flag))