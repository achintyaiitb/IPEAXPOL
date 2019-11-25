for i in range (0,400,4):
  f = open('/scratch/achintya/santosh/PNA/MD_Initial/Production/snapshots/100snaps/frame_'+str(i)+'.pdb')
  f.readline()
  l = f.readline().strip()
  s = ''
  count = 0
  while l!='END':
    line = l[13]
    t = l[26:] 
    L = t.split()
    x = L[0]
    y = L[1]
    z = L[2]
    n_space_x = 9-len(x)
    n_space_y = 9-len(y)
    n_space_z = 9-len(z)
    line = line+n_space_x*' '+x+n_space_y*' '+y+n_space_z*' '+z
    s = s+line+'\n'
    count += 1
    l = f.readline().strip()
  f.close()
  s = str(count)+'\n\n'+s
  f = open('PNA_frame_'+str(i)+'.xyz','w')
  f.write(s)
  f.close()


