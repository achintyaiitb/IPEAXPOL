def make_input(coord,job,name='',charge=0,mult=1):#enter coords file and pc file
  K = ['R','U']
  s = '! '+str(K[charge])+'HF   aug-cc-pVTZ/C RIJCOSX def2/J \n\n ' 
#def2-SVP  def2/J RIJCOSX \n\n
  s+= '%maxcore 10000\n\n'
  s+= '%scf\nmaxiter 200\nend\n\n'

  s+= '%pal\nnprocs 8\nend\n\n'
  s += '! CHELPG\n\n'
#  s += '%pointcharges "'+pc+'"\n\n'
  s += '* xyz '+str(charge)+' '+str(mult)+'\n\n'
  f = open(coord,'r')
  f.readline()
  f.readline()
  line = f.readline().strip()
  while line!='':
    s += line + '\n'
    line = f.readline().strip()
    print s
  f.close()
 
  s += '\n*\n'
  L = coord.split('.')
  if name=='':
     name = L[0]+'_fullQM_'+job+'.inp'
  else:
     name = name +'_fullQM_'+job+ '.inp'
  f = open(name,'w')
  f.write(s)
  f.close()
  return

#make_input ('uracil.xyz','uracil.pc')
 
