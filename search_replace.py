import os
import sys
import fileinput

for i in range (0,4,4):
 search = ['PNA L','C1','H2','C3','N4','C5','H6','C7','H8','C9','N10','C11','H12','O13','O14','H15','H16',''] 
# textToSearch2 = str('P W')
# textToSearch3 = str('Y L')
# textToSearch4 = str('C1')
 replace = ['PNA  ','C ','H ','C ','N ','C ','H ','C ','H ','C ','N  ','C  ','H  ','O  ','O  ','H  ','H  ']
# textToReplace1 = str( "TIP W" )
# textToReplace2 = str( "P  " )
# textToReplace3 = str( "Y  " )
# textToReplace4 = 'C '
 fileToSearch  = str('frame_'+str(i)+'.pdb' )

 tempFile = open( fileToSearch, 'r+' )
 count = 0
 textToSearch = search[0]
 while textToSearch != '':
  textToReplace = replace[count]
  for line in fileinput.input( fileToSearch ):
   if textToSearch in line :
    print('Match Found')
    newline=line.replace( textToSearch, textToReplace )
#   newline1=newline.replace( textToSearch2, textToReplace2 )
#   newline2=newline1.replace( textToSearch3, textToReplace3 )
    print newline
#   print newline1
#   print newline2
    tempFile.write(newline)
  count += 1
  textToSearch = search[count]
   

 tempFile.close()

