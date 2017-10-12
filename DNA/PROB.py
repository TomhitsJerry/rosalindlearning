import math
with open('/home/cyagen1/Downloads/rosalind_iev.txt','r')as f:
    string=f.readline()
    A=f.readline()
at=string.count('A')+string.count('T')
gc=string.count('G')+string.count('C')
for i in A.split(' '):
    i=float(i)
    t=math.log10((i/2)**gc)+math.log10(((1-i)/2)**at)
    print  "%.3f"%t,