from math import *
import sys,os
from pprint import pprint
import subprocess
import shutil

def pointcharge (filename):#ith water molecule will be replaced by charges.
  f = open (filename,'r')
  
  s = f.read().strip()
  L = s.split('\n')
  F = filename.split('.')
  f.close()
  qO = -0.834#TIP3P charges
  qH = 0.417
  s = '3\n'
  M = L[0].split()#O atom
  s = s+str(qO)+'   '+M[1]+'   '+M[2]+'   '+M[3]+'\n'
  M = L[1].split()#H atom
  s = s+str(qH)+'   '+M[1]+'   '+M[2]+'   '+M[3]+'\n'
  M = L[2].split()#H atom
  s = s+str(qH)+'   '+M[1]+'   '+M[2]+'   '+M[3]+'\n'



  p = open(F[0]+'_Q'+'.xyz','w')
  p.write(s)
  p.close()
  return

#pointcharge('Water1.xyz')
  
   
  
    
