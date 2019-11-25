from math import *
import sys,os
from pprint import pprint
import subprocess
import shutil
def separate(inputfile,main='thymine',n=15):
 f = open (inputfile,'r')
 line = f.readline()
 line = f.readline()
 l = 1
 s = ''
 line = ''
 while l <= n:
   line = f.readline()
   s = s + line.strip() +'\n'
   l += 1
 u = open (main+'.xyz','w')
 u.write(s)
 u.close()
 line = f.readline()
 k = 0
 while line.strip() != '':
   k+=1
   s = ''
  
   for i in range(3):
    s = s + line.strip() +'\n'
    line = f.readline()
    l += 1
  
   w = open ('Water'+str(k)+'.xyz','w')
   w.write(s)
   w.close()

 f.close()
 return k


