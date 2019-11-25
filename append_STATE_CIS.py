import datetime
import get_STATE_CIS
import osc_CIS
def append_IROOT(filename,mf_water,root):
 f = open ('/scratch/iit-bombay/tirthick/XPOL/thymine_shots/MODULES/IROOTs.txt','a')
 IROOTval = get_STATE_CIS.get_IROOT(filename,root)
 osc_str = osc_CIS.osc_strength (filename,root)
 s = mf_water + '\n'
 s += 'STATE = '+str(root)+' : '+str(IROOTval)+' eV\n'
 s += 'Oscillator strength = '+str(osc_str)+'\n'
 s += str(datetime.datetime.now()) + '\n\n'
 f.write(s)
 f.close()
 return

#append_IROOT('PNA_0_CIS_PC_EE_EOM_pc.out','PNA_0_CIS_PC',1)

 

