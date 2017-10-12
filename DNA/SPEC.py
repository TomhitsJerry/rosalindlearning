with open ('/home/cyagen1/Downloads/dict.txt','r')as f:
    w = f.read()
dict={}
for line in w.split('\n')[:-1]:
    x,y=line.split('   ')
    y=round(float(y),2)
    dict[y]=x
L=[float(line) for line in open('/home/cyagen1/Downloads/rosalind_spec.txt','r')]
aa_masses=[]
for i in range(len(L) - 1):
    aa_mass = round(L[i + 1] - L[i], 2)
    aa_masses.append(aa_mass)

aa=''
for i in aa_masses:
    aa+=dict[i]
print aa