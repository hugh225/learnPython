import sys,bs4,requests,webbrowser
webbrowser.open('https://www.baidu.com/s?wd='+' '.join(sys.argv[1:]))
print('https://www.baidu.com/s?wd'+' '.join(sys.argv[1:]))