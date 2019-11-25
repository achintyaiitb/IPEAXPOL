def make_DLPNO_input(coord,pc,job=''):#enter coords file and pc file
  s = '! RHF bt-PNO-'+job+'-EOM-CCSD TIGHTPNO  6-311++G(d,p) autoaux\n'
  s += '%maxcore 10000\n\n'
  s += '! CHELPG\n\n'
#  f = open('DLPNO_temp1.inp','r')
#  s += f.read()+'\n'
#  f.close()
  s += '%pointcharges "'+pc+'"\n\n'
  f = open('DLPNO_temp2.inp','r')
  s += f.read()+'\n\n'
  f.close()
  f = open(coord,'r')
  s += f.read()
  f.close()
  s += '\n*\n'
  f = open('DLPNO_temp3.inp','r')
  s += f.read()
  L = coord.split('.')
  name = L[0]+'_'+job+'_EOM_pc.inp'
  print name
  f = open(name,'w')
  f.write(s)
  f.close()
  return

