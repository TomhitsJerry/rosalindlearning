from Bio import Phylo
from cStringIO import StringIO
f=open('/home/cyagen1/Downloads/rosalind_nwck.txt','r')
pairs = [i.split('\n') for i in f.read().strip().split('\n\n')]
for i,j in pairs:
    x,y=j.split(' ')
    tree = Phylo.read(StringIO(i), 'newick')
    clades = tree.find_clades()
    for clade in clades:
        clade.branch_length = 1
    print tree.distance(x,y),
