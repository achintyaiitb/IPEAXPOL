from math import *
import sys,os
from pprint import pprint
import subprocess
import shutil

def pc_water (i,n):#n is total no. of water mol. 
           #ith water is to be replaced by charges
  nQ = 0
  string = ''
  for j in range (n):
    if (j+1) != i:
      f = open ('Water'+str(j+1)+'_Q.xyz','r')
      s = ''
      l = f.readline()
      nQ += int(l.strip())
      while l.strip() != '':
        l = f.readline()
        s += l.strip()+'\n'
      string += s
      f.close()
  g = open ('pc_water'+str(i)+'.pc','w')
  string = str(nQ)+'\n'+string
  g.write (string)
  g.close()
  return

#pc_water (2,2)
   
