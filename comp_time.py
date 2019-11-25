def comp_time (filename):
 f = open (filename,'r')
 s = f.read()
 i = s.find('TOTAL RUN TIME')
 i = i + len('TOTAL RUN TIME')
 i = i+1#excluding the ':' after 'TOTAL RUN TIME'
 t = s[i:]
 u = t.split()
 f.close()
 days = u[0]
 hrs = u[2]
 mins = u[4]
 secs = u[6]
 msecs= u[8]
 return t.strip()

print comp_time('PNA_4_1_5_pc.out')

