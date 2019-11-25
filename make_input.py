def make_input(coord,pc,charge=0,mult=1):#enter coords file and pc file
  K = ['R','U']
  s = '! '+str(K[charge])+'HF   aug-cc-pVTZ/C RIJCOSX def2/J \n\n ' 
#def2-SVP  def2/J RIJCOSX \n\n
  s+= '%maxcore 10000\n\n'
  s+= '%pal\nnprocs 8\nend\n\n'
  s += '! CHELPG\n\n'
  s += '%pointcharges "'+pc+'"\n\n'
  s += '* xyz '+str(charge)+' '+str(mult)+'\n\n'
  f = open(coord,'r')
  s += f.read()
  f.close()
  s += '\n*\n'
  L = coord.split('.')
  name = L[0]+'_pc.inp'
  f = open(name,'w')
  f.write(s)
  f.close()
  return

#make_input ('uracil.xyz','uracil.pc')
 
