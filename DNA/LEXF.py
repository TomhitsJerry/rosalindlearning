f=open('/home/cyagen1/Downloads/rosalind_lia.txt','r')
w=f.readline().replace(' ','').strip()
num=int(f.readline().strip())
f.close()
from itertools import product
print '\n'.join( [''.join(item) for item in sorted (product(w,repeat=num))])
