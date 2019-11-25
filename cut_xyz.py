import dist
def cut_xyz(filename,natoms,radius=2.7):
  f = open(filename+'.xyz','r')
  l = f.readline().strip()
  n = int(l)
  f.readline()
  l = ''
  s = ''
  K = []
  L = []
  M = []#matrix containing all selected atoms
  for i in range (0,natoms):
   l = f.readline().strip()
#   s = s + l + '\n'
   L = l.split()
   K = [L[0],(float(L[1]),float(L[2]),float(L[3]))]#contains symbol and coord. of atoms of mf
   M.append(K)
  K = []
  for i in range (0,(n - natoms)/3):
    for j in range (0,3):
      l = f.readline().strip()
      L = l.split()
      K.append ([L[0],(float(L[1]),float(L[2]),float(L[3]))])#contains symbol and coord. of atoms of waters
     # print K
    for k in range (0,natoms):
       for m in range (0,3):
        # print K[i]
         if dist.dist(M[k][1],K[3*i+m][1]) <= radius :
          # print K[3*i],K[3*i+m] 
           M.append(K[3*i])
           #print M
           M.append(K[3*i+1])
           #print M 
           M.append(K[3*i+2])#adds ith water molecule 
           break
       else: continue
       break
  f.close()
#  print K
#  print len(K)
#  print M
  s = str(len(M))+'\n\n'
  for I in M:
     line = I[0]+'    '+str(I[1][0])+'    '+str(I[1][1])+'    '+str(I[1][2])+'\n'
     s = s + line
  g = open (filename.split('/')[-1]+'_'+str(int(radius*10))+'.xyz','w')
  g.write(s)
  g.close()
  return


cut_xyz('thy_frame_999',15)

