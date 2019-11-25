import ESP_charge
def replace_by_Q (coord,charge,scaling = 1):#enter coord to be replaced by charges
  nQ = 0
  string = ''
  f = open (coord,'r')
  n = len(f.read().strip().split('\n'))
  f.close()
  f = open (coord,'r')
  s = str(n)+'\n'
  l = f.readline()#'XPOL'
  N = coord.split('.')
  Q = ESP_charge.ESP_charge(charge,n)
  while l.strip() != '':
      
      l = l.strip()
      nQ += 1
      L = l.split()
#     print L
      L[0] =str( scaling * float(Q[nQ-1]))
      t = '  '.join (L)
      s += t + '\n'
      l = f.readline()
  f.close()
  g = open (N[0]+'_Q'+'.xyz','w')
  g.write (s)
  g.close()
  return


#replace_by_Q('Water1.xyz','Water1_pc.out',1000)



