f = open ('input_CIS_PC.txt','w')
s = ''
for i in range (208,400,4):
  s += 'PNA_frame_'+str(i)+'    '+'PNA_'+str(i)+'_CIS_PC    16    1    0    1    EE    1\n'

f.write(s)
f.close()


