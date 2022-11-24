import os
import json
def get_name():
    return os.path.basename(__file__)
def change_path(x):
    os.path.abspath(x)
def get_curr_path():
    return os.getcwd()
def get_parent_dir():
    return str(get_curr_path()).replace('/'+str(get_curr_path()).split('/')[-1],'')
def change_parent_dir():
    return change_gears(parent_dir())
def change_gears(x):
    curr = get_curr_path()
    change_path(x)
    return curr
def home_it():
    curr = get_curr_path()
    slash = '//'
    if '//' not in str(curr):
        slash = '/'
    change_glob('slash',slash)
    change_glob('home',curr)
    return curr,slash
def check_str(x,y):
    c = ''
    if str(x) != str(y):
        c = y
    return c
def create_path(x,y):
    return str(x) + str(check_str(x[-1],slash))+str(y)
def check_dir(x):
    return os.path.isdir(x)
def check_file(x):
    return os.path.isfile(x) 
def make_dir(x):
    if check_dir(x) == False:
        os.mkdir(x)
def find_it(x,y):
    i = 0
    for i in range(0,len(x)):
        if str(x[i]) == str(y):
            return i
    return False
def reader_B(file):
    with open(file, 'r',encoding='UTF-8') as f:
        text = f.read()

        return text
def reader(file):
    with open(file, 'r') as f:
        text = f.read()
        return text
def pen_B(paper, place):
    
    with open(place, 'w',encoding='UTF-8') as f:
        f.write(str(paper))
        f.close()
        return
def pen(paper, place):
    with open(place, 'w') as f:
        f.write(str(paper))
        f.close()
        return
def list_files(x):
    return os.listdir(x)
def get_c(i):
    c = ''
    if c != 0:
        c = ',\n'
    return c
def add_many_str(x,k,z):
    y = ''
    for i in range(0,k):
        y = y + x
    return y+z
def get_words(x,y):
    if type(y) is not list:
        y = [y]
    z = ''
    while x[0] not in list_var_in_str(x[0],y):
        z = z + str(x[0])
        x = x[1:]
    return z
def del_space_in(x,y):
    if type(y) is not list:
        y = [y]
    
    for i in range(0,len(y)):
        res = list_var_in_str(x,['[','{','('])
        if y[i] in res:
            x = x.replace(y[i] + ' ',y[i])
        res = list_var_in_str(x,[']','}',')'])
        if y[i] in res:
            x = x.replace(' '+y[i],y[i])
    return x
def del_space_front(x,y):
    if type(y) is not list:
        y = [y]
    for i in range(0,len(x)):
        
        if list_var_in_str(x[0],y) in y:
            x = x[1:]
        else:
            return x
def get_words_and_junk(x,y):
    if type(y) is not list:
        y = [y]
    z = ''
    
    for i in range(0,len(y)):
        if list_var_in_str(x,z) not in y:
            z = z + str(x[0])
            x = x[1:]
    return z,x
def get_blank_bracs(x):
    n = []
    m = list()
    for i in range(0,len(x)):
        m.append(n)
    
    return m
def js_it(x):
    return json.loads(str(x).replace("'",'"'))

def line_num(x,filename):
    m = []
    with open(filename) as myFile:
        for num, line in enumerate(myFile, 1):
            if x in line:
                m.append(num-1)
    return m
def js_wrap(x):
    return js_it('{'+str(x)+'}')
def js_qu(x):
    return '"'+str(x)+'"'
def make_js(x,y):
    return js_qu(x)+':'+js_qu(y)
def add_js(x,y):
    return js_it(str(x)[:-1]+get_c(len(x))+str(y)+'}')
def do_js(x,z):
    for i in range(0,len(x)):
        y = make_js(x[i],z)
        if i == 0:
            w = js_wrap(y)
        else:
            w = add_js(w,y)
    return js_it(str(w).replace("'[]'","[]"))
def get_c_tf(i):
    if i == 0:
        return True
    return False
def new_line_it(x):
    y = ''
    for i in range(0,len(x)):
        c = ''
        if get_c_tf(i) == False:
            c = '\n'
        y =y+c+ str(x[i])
    return y
def try_it(x,y):
    try:
        n = x[y]
        return True
    except:
        return False
def find_lowest(x):
    x.sort()
    if try_it(x,0) == True:
        return x[0]
    else:
        return False
def find_highest(x):
    x.sort()
    if try_it(x,-1) == True:
        return x[-1]
    else:
        return False
def range_list(x):
    return [find_lowest(x),find_highest(x)]
def exists_make(x,y):
    if exists(y) == False:
        pen(x,y)
        return x
    else:
        return reader(y)
def exists(x):
    try:
        x = reader(x)
        return True
    except:
        return False
def count_lines(x):
    if exists(x) == False:
        pen('',x)
    count = 1
    with open(r''+str(x)+'', 'r') as fp:
        for count, line in enumerate(fp):
            pass
    return count
def fake_line(x,l,k):
    y = ''
    for i in range(l,k):
        y = y + '\n'
    return y
def read_lines(x):
    a = open(x, "r")
    rd = a.readlines()
    a.close()
    return rd
def write_lines(x,y):
    a = open(x, "w")
    a.writelines(y)
    a.close()
def add_lines(x,line):
    n = count_lines(x)
    fake = ''
    if line > n:
        fake = fake_line(x,n+1,line+1)
    pen(reader(x)+fake,x)
    add_lines(x,y+1)
    list_of_lines = read_lines(x)
    list_of_lines[y] = z
    write_lines(x,list_of_lines)
    
def split_lines(file):
    mylines = []                                # Declare an empty list.
    with open (file, 'rt') as myfile:    # Open lorem.txt for reading text.
        for myline in myfile:                   # For each line in the file,
            mylines.append(myline.rstrip('\n')) # strip newline and add to list.
    return mylines
def list_var_in_str(x,y):
    res = [ele for ele in y if(ele in x)]
    return res
def comb_ls(x,y):
    for i in range(0,len(y)):
        x.append(y[i])
    return x
def int_chk(x):
    try:
        n =int(x)
        return False
    except:
        return True
def list_check(x):
    if type(x) is str:
        return js_it(l),len_x
    if type(x) is list:
        return x,len(x)
    else:
         return x,
def ls_to_str(x):
    new = ''
    for i in range(0,len(x)):
        new = new + str(x[i])
    return new
def chop_lines(x,y):
    w = []
    for i in range(0,len(x)):
        a = x[i]
        if i+1 < len(x):
            z = x[i+1]
            n = ls_to_str(y[int(a):int(z)])
            w.append(n)
        else:
            n = ls_to_str(y[int(a):])
            w.append(n)
    return w

def list_it(x):
    x,k = list_check(x)
    n = ''
    
    for i in range(0,k):
        n = n + x[i]
    return n
def change_glob(x,v):
    globals()[x] = v
def add_it(x,y):
    return int(x) + int(y)
def add_str(x,y):
    return str(x)+str(y)
def str_kill(x,y):
    y = ''
    x,i = list_check(x)
    st = []
    for l in range(0,len(y)):
        if type(y[l]) is list:
            yy = [],[]
            for ll in range(0,len(y_a)):
                st.append(y[l][ll])
                yy[ll].append(y[l][ll])
                y = go
        else:
            st.append(y[l])
        if list_var_in_str(x,z):
            print('bo')
    z = list_var_in_str(x,y)  
    z = add_str(yy,x[i])
    i = add_it(i,1)
    return z,i
def str_go(x,y,z):
    for i in range(y):
        x.append(y[i])
    x,y = list_check(x)
    res = list_var_in_str(x,z)
    if res in y:
        return res,1
    elif res in x:
        return res,-1
    else:
        return False
def check_it(x,y):
    if type(y) is not list:
        y = [y]
    for i in range(0,len(y)):
        res=list_var_in_str(x,y)
        if len(res) != 0:
            return res
    return False

def create_ls_bracs(x,k):
    w = []
    y = '[]'
    for ii in range(0,k):
        z = []
        for i in range(0,x):
            z.append(y)
        w.append(js_it(z))
    return str(w).replace('"','').replace("'",'')
def var_str(x):
    if type(x) is not list:
        x = [x]
    for i in range(0,len(x)):
        #var = 710
        #variable_name = [k for k, v in locals().items() if v == 710][0] 
        #print("Your variable name is " + variable_name)
        
        exec("%s = %s" % (x[i],'z'))
        z = x[i]
        exec("%s = %s" % (z,x[i]))
def create_blanks(x):
    y = ''
    for i in range(0,x):
        y = y + ' '
    return y
def timer(x):
    return int(x) + 1
def remove_end(x,y):
    return str(x).replace(str(y)+str(x).split(str(y))[-1],'')
def get_end(x,y):
    return str(x).split(str(y))[-1]
def copy_it(x,y):
    pen(reader(x),y)
