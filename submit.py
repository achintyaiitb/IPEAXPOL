import subprocess
import sys,os
import shutil


def submit (filename,extension='inp'):
 inp=filename+'.'+extension
 out=filename+'.out'
 run_arg='~/orca/x86_exe/orca '+ inp+' > '+out
# print run_arg
# with open(inp, 'r') as fin:
#   print fin.read()
 res = subprocess.call([run_arg],shell=True)
 return# (shell == True)

#submit ('PNA_4_5_PC_EE_fullCIS')
