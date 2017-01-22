#！/usr/bin/env python
# newname: New filename you want to change
# filetype: The filetype which you want to change (remember to add '.'')
# rename files by filetype order by creattime in current dir

import os
import time
import glob

def rename(newname, filetype):
	name_time_list = []
	for fliename in glob.glob('*'+filetype):
		name_time_list.append((time.ctime(os.path.getctime(fliename)), fliename))
	name_time_list.sort()
	#tuple：name_time_list里是((time1, name1),(time2, name2),(time3,name3),...),sort()方法以第一个参数进行升序排序
	#sort(reverse=True)降序排序

	for i in range(len(name_time_list)):
		os.rename(name_time_list[i][1], newname+str(i+1)+filetype)

newname = input("请输入想要修改成的文件名:")
filetype = input("请输入后缀名，输入格式：（.xxx）:")
rename(newname, filetype)