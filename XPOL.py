import separate
import ESP_charge
import charge_water
import pc_water
import sys,os
import subprocess
import shutil
import make_input
import replace_by_Q
import replace_by_Q_EOM
import charge_EOM
import gen_water_pc
import gen_main_pc
import charge_water
import submit
import submit_CHELPG
import energy
import make_DLPNO_input




def XPOL (L):

 coord  = L[0] + '.xyz'
 main = L[1]# name of main fragment
 N = int( L[2]) #no. of atoms in main fragment
 scaling = float(L[3])
 main_charge = int(L[4])
 main_mult = int(L[5])
 job = L[6]
 root = L[7]

 
 n = separate.separate(coord,main,N)# n is no. of water molecules

 #replace_by_Q.replace_by_Q('uracil.xyz')

 for i in range (n):
   charge_water.pointcharge('Water'+str(i+1)+'.xyz')

 for i in range (n):
   pc_water.pc_water(i+1,n)

 gen_main_pc.gen_main_pc(main,n)

 #for i in range (n):
 #  gen_water_pc.gen_water_pc(i+1)

 make_input.make_input(main+'.xyz',main+'.pc',main_charge,main_mult)

 #for i in range (n):
 #  make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')

 submit.submit(main+'_pc')


 #for i in range (n):
 #  submit.submit('Water'+str(i+1)+'_pc')


 En = energy.energy(main+'_pc.out')

 print En

 replace_by_Q.replace_by_Q(main+'.xyz',main+'_pc.out')#update uracil charges from 1st iter

 for i in range (n):
   gen_water_pc.gen_water_pc(i+1,main,N)#gen. pc files for water using updated uracil charges

 for i in range (n):
   make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')

 for i in range (n):
   submit.submit('Water'+str(i+1)+'_pc')



 Eo = 0

 j = 0

 epsilon = 0.000001
 while (abs(Eo-En) >= epsilon):
   j += 1
   #print abs(Eo-En)
   print 'Starting iteration no. '+str(j)
   Eo = En
   replace_by_Q.replace_by_Q(main+'.xyz',main+'_pc.out')#update uracil charges
   for i in range(n):
     replace_by_Q.replace_by_Q('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'_pc.out')#update water charges
   for i in range (n):
     pc_water.pc_water(i+1,n)
   gen_main_pc.gen_main_pc(main,n)#gen. uracil pc file
   for i in range (n):
     gen_water_pc.gen_water_pc(i+1,main,N)#gen. water pc file

   make_input.make_input(main+'.xyz',main+'.pc',main_charge,main_mult)#make input files with updated charges
   for i in range (n):
     make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')
  
   submit.submit(main+'_pc')#submit input files
   for i in range (n):
     submit.submit('Water'+str(i+1)+'_pc')

   En = energy.energy(main+'_pc.out')
   print "Energy of "+main+" after iteration  "+str(j)+" is "+str(En) 
   print "delta E = " + str(abs(Eo-En))

# print 'Converged energy = '+str(En)+'\n\n'

# print 'Scaling the water point charges'
# for i in range(n):
#   replace_by_Q.replace_by_Q('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'_pc.out',scaling)
# for i in range (n):
#   pc_water.pc_water(i+1,n)
# gen_main_pc.gen_main_pc(main,n)#gen. main fragment pc file

 print 'Submitting EOM file'
 make_DLPNO_input.make_DLPNO_input(main+'.xyz',main+'.pc',job)
 submit.submit(main+'_'+job+'_EOM_pc')
 submit_CHELPG.submit(main+'_'+job+'_EOM_pc.root'+str(root)+'.'+job)

#Regenerating water charges from EE/IP/EA calc. of main frag.
 replace_by_Q_EOM.replace_by_Q_EOM(main+'.xyz',main+'_'+job+'_EOM_pc.root'+str(root)+'.'+job+'.out')
 for i in range (n):
   gen_water_pc.gen_water_pc(i+1,main,N)#gen. pc files for water using updated uracil charges

 for i in range (n):
   make_input.make_input('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'.pc')

 for i in range (n):
   submit.submit('Water'+str(i+1)+'_pc')
 for i in range(n):
   replace_by_Q.replace_by_Q('Water'+str(i+1)+'.xyz','Water'+str(i+1)+'_pc.out')#update water charges
#Now we have final water charges

 gen_main_pc.gen_main_pc(main,n)#gen. main fragment pc file
 print 'Final files generated'


 print 'Submitting '+job+' file'
# make_DLPNO_input.make_DLPNO_input(main+'.xyz',main+'.pc')
# submit.submit(main+'_IP_DLPNO_pc')

# print 'IP values obtained'


 make_DLPNO_input.make_DLPNO_input(main+'.xyz',main+'.pc',job)
 submit.submit(main+'_'+job+'_EOM_pc')

 return



f = open('input_data_new.txt','r')
l = f.readline().strip()
while l != '':
 L = l.split()
 XPOL (L)
 l = f.readline().strip()


