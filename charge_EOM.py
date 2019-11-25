def charge_EOM (filename,n):
 f = open (filename,'r')
 s = f.read()
 a = s.find('Excited State Population Analysis')

 i = s.find('MULLIKEN ATOMIC CHARGES',a)
 i = i + len('MULLIKEN ATOMIC CHARGES')
 j = i
 count = 0
 Q = []
 while True:
  if s[j] == '\n': count+=1
  if count == 2: break
  j+=1
 j+=1
 k = j
 while True:
  if s[k] == '\n':
    t = s[j:k]
    count+=1
    j = k+1
    u = t.split()
    Q.append(u[3])#Check ORCA output file to understand u[3]
  k+=1
  if count == 2 + n: break#n is no. of atoms #Value of count has to be set depending on output file
 return Q

#print charge_EOM ('formaldehyde__EOM_pc.out',4)
