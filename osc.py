def osc_strength (filename,root = 1):
 f = open (filename,'r')
 s = f.read()
 i = s.find('ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS')
 i = i + len('ABSORPTION SPECTRUM VIA TRANSITION ELECTRIC DIPOLE MOMENTS')
 j = i
 count = 0
 while True:
  if s[j] == '\n': count+=1
  if count == (4+root): break
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
    return float(u[3]) #returns oscillator strength
    break
  k+=1

#print osc_strength('form_pert1_2_EE_EOM_pc.out',1)



