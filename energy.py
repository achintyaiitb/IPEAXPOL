def energy (filename):
 f = open (filename,'r')
 s = f.read()
 i = s.find('TOTAL SCF ENERGY')
 i = i + len('TOTAL SCF ENERGY')
 j = i
 count = 0
 while True:
  if s[j] == '\n': count+=1
  if count == 3: break
  j+=1
 j+=1
 k = j
 while True:
  if s[k] == '\n':
    t = s[j:k]
    count+=1
    j=k+1
    u=t.split()
    f.close()
    return float(u[3]) #returns energy in a.u.
    break
  k+=1



