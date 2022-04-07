#!/usr/bin/env python3

import string    
import random
import threading

def my_function():
    f= open("seeds.txt","w+")
    for i in range(99999):
        S = 15    
        ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k = S))  
        #print(str(ran))
        f.write(str(ran) + "\n")
    
my_function()

x = threading.Thread(target=my_function)
x.start()

#Seed.gen made for MediaFire fishing with wfuzz by greyhound, S is for how many letters/numbers will be generated.
#Range is for how many seeds will be generated.
#wfuzz -c -w seeds.txt --hc=404 https://www.mediafire.com/file/FUZZ
