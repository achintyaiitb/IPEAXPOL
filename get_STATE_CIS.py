def get_IROOT (filename,nroot):
 f = open (filename,'r')
 s = f.read()
 i = s.find('STATE  '+str(nroot))
 f.close()
 j = i
# count = 0
# while count != 3:
#  j += 1
 while s[j] != '\n':
   j+=1
# count += 1
# j+=1
# k = j
# while s[k]!='\n':
#   k += 1
 t = s[i:j]
 L = t.split()
 
# count+=1
 #j=k+1
 return float(L[5]) #returns IROOT = nroot in eV



