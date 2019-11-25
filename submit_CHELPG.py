import subprocess
import sys,os
import shutil


def submit (filename):
 inp=filename+'.nat'
 out=filename+'.out'
 run_arg='~/orca/x86_exe/orca_chelpg '+ inp+' > '+out
# print run_arg
# with open(inp, 'r') as fin:
#   print fin.read()
 res = subprocess.call([run_arg],shell=True)
 return# (shell == True)

submit ('PNA_0_1st_shell_EE_CIS_pc.engrad')
