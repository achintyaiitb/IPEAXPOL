def ESP_charge (filename,n):
 f = open (filename,'r')
 s = f.read()
 i = s.find('CHELPG Charges')
 i = i + len('CHELPG Charges')
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

