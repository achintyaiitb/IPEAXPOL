import datetime
import get_IROOT
import osc
def append_IROOT(filename,mf_water,root):
 f = open ('/scratch/iit-bombay/tirthick/XPOL/thymine_shots/MODULES/IROOTs.txt','a')
 IROOTval = get_IROOT.get_IROOT(filename,root)
 osc_str = osc.osc_strength (filename,root)
 s = mf_water + '\n'
 s += 'IROOT = '+str(root)+' : '+str(IROOTval)+' eV\n'
 s += 'Oscillator strength = '+str(osc_str)+'\n'
 s += str(datetime.datetime.now()) + '\n\n'
 f.write(s)
 f.close()
 return

#append_IROOT('PNA_TIP3P_6_EE_EOM_pc.out','PNA_TIP3P_6',1)

 

