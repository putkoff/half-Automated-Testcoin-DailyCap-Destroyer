import functions as f
import random
import os
import webbrowser
import time
import subprocess
import func as func
import clipboard
from random import randint
import pathlib
all = func.js_it(func.exists_make('{"adds":[],"priv":[]}',os.getcwd()+'/'+'all.json'))
def find_it(x,y):
    if str(x[i]) == str(y):
        x[i]
def shuffle_list():
    k = len(places)
    zint = random.randint(0,k)
    badbad.append(places[zint])
    return places[zint], k
def bash_it(x):
    sh_str = f.reader('sample_whole_sh.txt')
    f.pen(sh_str.replace('^^killme^^',x),'script.sh')
    os.popen("gnome-terminal -x ./script.sh").read()

off = 'expressvpn disconnect'
on = 'expressvpn connect '
inp = ''
path = str(pathlib.Path().resolve())+'/doit.txt'


global places,badbad,k
places = f.js_it(f.reader('places.json'))
badbad = []
k = len(places) 
for i in range(0,k):
    place,k = shuffle_list()
    clipboard.copy(all["adds"][i])
    f.pen('','doit.txt')
    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    bash_it(off)
    cmd = off + ';'+ on +place +' >> '+path+'; firefox https://faucet.avax.network >> '+path;
    print(cmd)
    bash_it(cmd)
    while 'Connected to '+place not in f.reader(path):
        time.sleep(1)
    #p = subprocess.Popen(["firefox", "https://faucet.avax.network/"])
    
    #bash_it('firefox https://faucet.avax.network >> '+path)
    input('press enter')
    #p.kill()
    bash_it('kill -9 $(ps -x | grep firefox)')

