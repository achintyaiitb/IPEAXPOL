import shutil
import subprocess
import submit
import make_fullQM_input
import energy

def fullQM(L,suffix=''):
 coord  = L[0] 
 # main = L[1]# name of main fragment
 #N = int( L[2]) #no. of atoms in main fragment
 #scaling = float(L[3])
 main_charge = int(L[1])
 main_mult = int(L[2])
 job = L[3]
 root = int(L[4])
 name = coord+suffix
 make_fullQM_input.make_input(coord+'.xyz',job,name,main_charge,main_mult)
#pc file not reqd.

 submit.submit(name+'_fullQM_'+job)
#change inp filename as per make_input

 En = energy.energy(name+'_fullQM_'+job+'.out')
#change inp filename as per make_input
 return En

f = open('input_fullQM_IP.txt','r')
l = f.readline().strip()
while l != '':
 L = l.split()
 Eneutral=fullQM (L)
 if L[3]=='IP':
   L[1]=1
   L[2]=2
   print L
 if L[3]=='EA':
   L[1]=-1
   L[2]=2
   print L
 Eion=fullQM (L,'_cat')
 h=open(L[0]+'_fullQM_'+L[3]+'.txt','w')
 S=L[0]+'\n'+'E neutral = '+str(Eneutral)+'\n'
 S+='E ion = '+str(Eion)+'\n'
 EIP = Eion-Eneutral
 S+=L[3]+' = '+str(EIP)+' Hartree\n'
 S+='   = '+str(EIP*27.2114)+' eV\n'
 h.write(S)

 l = f.readline().strip()

