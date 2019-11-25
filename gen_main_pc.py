import subprocess
def gen_main_pc (main,n): #n is no. of water molecules
  s = ''
  string = ''
  count = 0
  for i in range (n):
    f = open ('Water'+str(i+1)+'_Q.xyz','r')
    l = f.readline().strip()
    count += int(l)
    string += f.read().strip()+'\n'
    f.close()
  s = str(count)+'\n'+string
  f = open(main+'.pc','w')
  f.write(s)
  return

#gen_uracil_pc (2)

