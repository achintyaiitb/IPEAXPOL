import cut_xyz
s = ''
#L = ['0', '10', '25', '65', '70', '95', '110', '120', '140', '150', '155', '160', '165', '175', '245', '320', '330', '350', '415', '425', '430', '435', '525', '535', '580', '600', '685', '690', '695', '795', '815', '825', '835', '855', '875', '940', '990']
for i in  range(2,7,2):
#  cut_xyz.cut_xyz('/scratch/iit-bombay/tirthick/XPOL/thymine_shots/PNA_MD/PNA_frame_'+str(i),16,10.8)
  s += 'PNA_water_'+str(i)+'    PNA_'+str(i)+'_IP    16    1    0    1    IP    1\n'
f = open ('input_pert_n.txt','w')
f.write(s)
 
