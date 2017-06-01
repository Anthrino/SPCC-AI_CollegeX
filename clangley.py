
file = open('save.log','r')
s = file.read()
# print s

s = s.replace(';',"'")
s = s.replace('l',';')
s = s.replace('k','l')
s = s.replace('j','k')
s = s.replace('h','j')
s = s.replace('g','h')
s = s.replace('f','g')
s = s.replace('d','f')
s = s.replace('s','d')
s = s.replace('a','s')
s = s.replace('.','a')

s = s.replace(':','"')
s = s.replace('L',':')
s = s.replace('K','L')
s = s.replace('J','K')
s = s.replace('H','J')
s = s.replace('G','H')
s = s.replace('F','G')
s = s.replace('D','F')
s = s.replace('S','D')
s = s.replace('A','S')
s = s.replace('>','A')

s = s.replace('m',',')
s = s.replace('n','m')
s = s.replace('b','n')
s = s.replace('v','b')
s = s.replace('c','v')
s = s.replace('x','c')
s = s.replace('z','x')
s = s.replace('/','z')
s = s.replace(',','/')

s = s.replace('M','<')
s = s.replace('N','M')
s = s.replace('B','N')
s = s.replace('V','B')
s = s.replace('C','V')
s = s.replace('X','C')
s = s.replace('Z','X')
s = s.replace('?','Z')

s = s.replace('<:Vtr;A','<LCtrl>')
s = s.replace('<:DjgtA','<LShft>')
s = s.replace('<NvlDpA','<BckSp>')
s = s.replace('<FowmA','<Down>')
s = s.replace('<UpA','<Up>')
s = s.replace('<Fe;A','<Del>')
s = s.replace('<TsnA','<Tab>')
s = s.replace('<RihjtA','<Right>')
s = s.replace('<:egtA','<Left>')
s = s.replace('<RDjgtA','<RShft>')
s = s.replace('<Vpd:lA','<CpsLk>')
s += "\n"

file.close()
# print s

with open('out.txt','w') as op:
	op.write(s)
	op.close()

