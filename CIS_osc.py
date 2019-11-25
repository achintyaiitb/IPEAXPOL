import osc_CIS
s = ''
for i in range (0,400,4):
  
  s+=str(osc_CIS.osc_strength('PNA_'+str(i)+'_1st_shell_EE_CIS_pc.out'))+'\n'
  
f = open ('PNA_snap_osc.txt','w')
f.write(s)

