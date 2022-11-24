import os
import sys
import json
def pen(x,p):
    with open(p, 'w',encoding='UTF-8') as f:
        return f.write(str(x))
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def copy_it(x,y):
	x_r = reader(x)
	x_n = x.split('/')[-1]
	if str(y)[-1] !='/':
		y =str(y) + '/'
	y = y + x_n
	pen(x_r,y)
def list_files(x):
    return os.listdir(x)
def exists(x):
    if str(x)[-1] !='/':
        y = str(x).split('/')
        y_1 = str(x).replace('/'+y[-1],'')
    z = list_files(y_1)
    if y[-1] in z:
        return True
    return False
def js_it(x):
    return json.loads(str(x).replace('[,','[').replace('{,','{').replace("'",'"'))
def exists_make(x,y):
    if exists(y) == True:
        return reader(y)
    pen(x,y)
    return x
