def make_DLPNO_input(coord,pc,job=''):#enter coords file and pc file
  s = '! RHF 6-311++G(d,p) aug-cc-pVTZ/C RIJCOSX def2/J\n\n%maxcore 10000\n\n%pal\nnprocs 8\nend\n'
#  s += '%maxcore 10000\n\n'
  s += '! CHELPG\n\n'
  s += '! Engrad Keepdens\n\n'
#  f = open('DLPNO_temp1.inp','r')
#  s += f.read()+'\n'
#  f.close()
  s += '%pointcharges "'+pc+'"\n\n'
  f = open('CIS_temp2.inp','r')
  s += f.read()+'\n\n'
  f.close()
  f = open(coord,'r')
  s += f.read()
  f.close()
  s += '\n*\n'
  f = open('CIS_temp3.inp','r')
  s += f.read()
  L = coord.split('.')
  name = L[0]+'_'+job+'_CIS_pc.inp'
  print name
  f = open(name,'w')
  f.write(s)
  f.close()
  return

