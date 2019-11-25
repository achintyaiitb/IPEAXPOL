from math import *
import sys,os
from pprint import pprint
import subprocess
import shutil
started = False
array1=[2149,2299,3049,3099,3149,3199,3299]
array2=[2549,2649,2699,3849,3899]
array3=[2149,2399,2599,2749,3599]
array4=[2449]
array5=[2249,2899,2949,3599]
array7=[2849,2999,3899]
array8=[2149,2299,2349,3199]
array9=[2549,2799,3249,3399,3499,3549,3599,3699,3899]
array10=[3149,3199]
for i in array9:
   collected_lines = []
   inputfile =''
#input file name
   orca_input= 'after_VDE_9ns_'+str(i)+'.pdb'
#output file
   orca_output='1st_shell_9ns_'+str(i)+'.xyz'
   with open(orca_input, "r") as fp:
     for i, line in enumerate(fp.readlines()):
         linecontent=(line.rstrip()).split()
         if linecontent[0] == "AUTHOR":
             started = True
#             print "started at line", i+1 # counts from zero !
             continue
         if started and linecontent[0]=="CONECT":
 #            print "end at line", i+1
             started =False
             break
          # process line 
         if started:
          collected_lines.append(line.rstrip())
   k = 1
   l = 12
   cut = 2.7
   P=[]
   Q=[]
   R=[]
   
  # print len(collected_lines)
   for i in range(len( collected_lines)):
    variable=collected_lines[i].split()
    #print variable
    x=float(variable[5])
    y=float(variable[6])
    z=float(variable[7])
    p= (x,y,z)
    P.append(p)
    if variable[3]=='HOH':
     Q.append(p)
    
   S=''
#   S='!EA-EOM-DLPNO-CCSD TightSCF RIJK aug-cc-pVDZ aug-cc-pVDZ/C def2/J NORMALPNO pal16'+'\n'
#   S=S+'%maxcore 5000'+'\n'
#   S=S+'#QM/MM input'+'\n'
#   S=S+' %mdci'+'\n'                       
#   S=S+' printlevel 3'+'\n'
#   S=S+' nroots 5'+'\n'
#   S=S+' TCutPNOSingles 1e-12'+'\n'
#   S=S+' FollowCIS true'+'\n'
#   S=S+' NDAV 30'
#   S=S+'DoROOTWISE false'+'\n'
#   S=S+' Maxiter 2000'+'\n'
#   S=S+' DTOl 1e-5'+'\n'
#   S=S+'NormalPNOFragInter    {1 1}'+'\n'
#   S=S+'HFFRAGMENTINTERACTION {2 2} {1 2}'+'\n'
#   S=S+' end'+'\n'
#   S=S+'* xyz 0 1'+'\n'


   for c in range(len( collected_lines)):
    variable=collected_lines[c].split()
    #print variable
    if (k-1 <= c <= l-1):
     variable2list=list(variable[2])
     variable[2]=variable2list[0]
     S=S+ variable[2]+'   '+ variable[5]+'   '+variable[6]+'   '+variable[7]+'\n'
#     S=S+'newgto "aug-cc-pVDZ" end'+'\n'
#     S=S+'NewAuxGTO "aug-cc-pVDZ/C" end'+'\n'


#     if c == 4:
#      S=S+'newgto'+'\n'
#      S=S+'S   8'+'\n'
#      S=S+'  1   9046.0000000              0.0007000'+'\n'
#      S=S+'  2   1357.0000000              0.0053890'+'\n'
#      S=S+'  3    309.3000000              0.0274060'+'\n'
#      S=S+'  4     87.7300000              0.1032070'+'\n'
#      S=S+'  5     28.5600000              0.2787230'+'\n'
#      S=S+'  6     10.2100000              0.4485400'+'\n'
#      S=S+'  7      3.8380000              0.2782380'+'\n'
#      S=S+'  8      0.7466000              0.0154400'+'\n'
#      S=S+'S   8'+'\n'
#      S=S+'  1   9046.0000000             -0.0001530'+'\n'
#      S=S+'  2   1357.0000000             -0.0012080'+'\n'
#      S=S+'  3    309.3000000             -0.0059920'+'\n'
#      S=S+'  4     87.7300000             -0.0245440'+'\n'
#      S=S+'  5     28.5600000             -0.0674590'+'\n'
#      S=S+'  6     10.2100000             -0.1580780'+'\n'
#      S=S+'  7      3.8380000             -0.1218310'+'\n'
#      S=S+'  8      0.7466000              0.5490030'+'\n'
#     S=S+'S   1'+'\n'
#      S=S+'  1      0.2248000              1.0000000'+'\n'
#      S=S+'S   1'+'\n'
#      S=S+'  1      0.0612400              1.0000000'+'\n'
#      S=S+'S   1'+'\n'
#      S=S+'  1      0.0191375              1.0000000'+'\n'
#      S=S+'S   1'+'\n'
#      S=S+'  1      0.0059805              1.0000000'+'\n'
#      S=S+'S   1'+'\n'
#      S=S+'  1      0.0018689              1.0000000'+'\n'
#      S=S+'S   1'+'\n'
#      S=S+'  1      0.0005840              1.0000000'+'\n'
#      S=S+'S   1'+'\n'
#      S=S+'  1      0.0001825              1.0000000'+'\n'
#      S=S+'P   3'+'\n'
#      S=S+'  1     13.5500000              0.0399190'+'\n'
#      S=S+'  2      2.9170000              0.2171690'+'\n'
#      S=S+'  3      0.7973000              0.5103190'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.2185000              1.0000000'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.0561100              1.0000000'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.0175344              1.0000000'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.0054795              1.0000000'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.0017123              1.0000000'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.0005351              1.0000000'+'\n'
#      S=S+'P   1'+'\n'
#      S=S+'  1      0.0001672              1.0000000'+'\n'
#      S=S+'D   1'+'\n'
#      S=S+'  1      0.8170000              1.0000000'+'\n'
#      S=S+'D   1'+'\n'
#      S=S+'  1      0.2300000              1.0000000'+'\n'
#      S=S+'D   1'+'\n'
#      S=S+'  1      0.0719750              1.0000000'+'\n'
#     S=S+'D   1'+'\n'
#      S=S+'  1      0.0224609              1.0000000'+'\n'
#      S=S+'D   1'+'\n'
#      S=S+'  1      0.0070190              1.0000000'+'\n'
#      S=S+'D   1'+'\n'
#      S=S+'  1      0.0021934              1.0000000'+'\n'
#      S=S+'end'+'\n'
#      S=S+'NewAuxGTO "AutoAux" end'+'\n'
      

   for a in range (0,l):
    for b in range (l,len(collected_lines)):
     x_dist=(P[a][0]-P[b][0])**2   
     
     y_dist=(P[a][1]-P[b][1])**2
     
     z_dist=(P[a][2]-P[b][2])**2
    
     dist = (x_dist+y_dist+z_dist)**0.5
    
#    print dist, a, b

   chunks=[]
   for j in range(len(Q)):
    chunks = [Q[x:x+3] for x in range(0, len(Q), 3)]
#  print chunks

#  print len(chunks)
   n_atom = 12
   for n in range(0,len(chunks)):
    count = 0   
    for m in range(0,l):
     OW_x_sq=(P[m][0]-chunks[n][0][0])**2
     OW_y_sq=(P[m][1]-chunks[n][0][1])**2
     OW_z_sq=(P[m][2]-chunks[n][0][2])**2

     OW_dist=( OW_x_sq +  OW_y_sq +  OW_z_sq )**0.5

     HW1_x_sq=(P[m][0]-chunks[n][1][0])**2
     HW1_y_sq=(P[m][1]-chunks[n][1][1])**2
     HW1_z_sq=(P[m][2]-chunks[n][1][2])**2
   
     HW1_dist=( HW1_x_sq +  HW1_y_sq +  HW1_z_sq )**0.5

     HW2_x_sq=(P[m][0]-chunks[n][2][0])**2
     HW2_y_sq=(P[m][1]-chunks[n][2][1])**2
     HW2_z_sq=(P[m][2]-chunks[n][2][2])**2

     HW2_dist=( HW2_x_sq +  HW2_y_sq +  HW2_z_sq )**0.5

   #  print OW_dist, HW1_dist, HW2_dist, m,n
     
     
     if ((OW_dist < cut) or (HW1_dist< cut) or (HW2_dist< cut)) :
      count = 1
     
    if count == 1:
     S=S+'O  '+str(chunks[n][0][0])+ '  '+str(chunks[n][0][1])+'   '+str(chunks[n][0][2])+'\n'
     S=S+'H  '+str(chunks[n][1][0])+ '  '+str(chunks[n][1][1])+'   '+str(chunks[n][1][2])+'\n'
     S=S+'H  '+str(chunks[n][2][0])+ '  '+str(chunks[n][2][1])+'   '+str(chunks[n][2][2])+'\n'
     n_atom += 3
    # print OW_dist, HW1_dist, HW2_dist, m, n, 'include'
#    else:
#     S=S+'Q(2) -0.834  '+str(chunks[n][0][0])+ '  '+str(chunks[n][0][1])+'   '+str(chunks[n][0][2])+'\n'
#     S=S+'Q(2)  0.417  '+str(chunks[n][1][0])+ '  '+str(chunks[n][1][1])+'   '+str(chunks[n][1][2])+'\n'
#     S=S+'Q(2)  0.417  '+str(chunks[n][2][0])+ '  '+str(chunks[n][2][1])+'   '+str(chunks[n][2][2])+'\n'



#   S=S+'*'+'\n'
#   S=S+'%basis'+'\n'
#   S=S+'AuxJK "AutoAux"'+'\n'
#   S=S+'end'+'\n'

 #  print S
#   print 'output file is written into',orca_output
   string = str(n_atom)+'\n\n'+S
   f=open(orca_output,"w")
   f.write(string)
   f.close()
   f = open ('input_pert_n.txt','a')
   K = orca_output.split('.')
   J = K[0].split('_')
   inp_line = K[0]+'    uracil_'+J[2]+'_'+J[3]+'   12    1    0    1    EA    2\n'
   f.write(inp_line)
   f.close()

   

