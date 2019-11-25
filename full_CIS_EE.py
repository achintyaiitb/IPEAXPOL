import shutil
import subprocess
import submit


def make_fullCIS_input(coord,job='EE'):#enter coords file and pc file
  s = '! RHF  6-311++G(d,p) aug-cc-pVTZ/C RIJCOSX def2/J\n'
  s += '%maxcore 15000\n\n'
  s += '%pal\nnprocs 8 \nend\n\n'
# s += '!\n'
#  s += '%scf\n'
#  s += 'sthresh 1e-6\n'
#  s += 'end\n\n'
#  f = open('DLPNO_temp1.inp','r')
#  s += f.read()+'\n'
#  f.close()
#  s += '%pointcharges "'+pc+'"\n\n'
  f = open('CIS_temp2.inp','r')
  s += f.read()+'\n\n'
  f.close()
  f = open(coord+'.xyz','r')
  f.readline()
  f.readline()
  line = f.readline().strip()
  while line!='':
    s += line + '\n'
    line = f.readline().strip()
    print s
  f.close()
  s += '\n*\n'
  f = open('CIS_temp3.inp','r')
  s += f.read()
  f.close()
# L = coord.split('.')
  name = coord+'_'+job+'_fullCIS.inp'
  print name
  f = open(name,'w')
  f.write(s)
  f.close()
  return

f = open('input_fullCIS.txt','r')
l = f.readline().strip()
while l != '':
 print l
 make_fullCIS_input(l,'EE')
#submit.submit(l+'_EE_fullCIS')
 l = f.readline().strip()

