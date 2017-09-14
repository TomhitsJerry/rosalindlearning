import numpy as np
def unique(lst):
    return dict(zip(*np.unique(lst, return_counts=True)))
with open("/home/cyagen1/rosalind_gc.txt",'r') as f:
    w=f.read()
whole=w.split('>')[1]
content=whole.split('\n')[1:]
content=''.join(content)
lie=len(content)

hang=len(w.split('>')[1:])
L=[[0 for col in range(lie)]for row in range(hang)]
for i ,both in enumerate( w.split('>')[1:]):
    title =both.split('\n')[0]
    content=''.join(both.split('\n')[1:])
    for j in range(lie):
        L[i][j]=content[j]
l=[[0 for col in range(hang)]for row in range(lie)]
for i in range(lie):
    for j in range(hang):
        l[i][j]=L[j][i]
for i in l:
    d=unique(i)
    print max(d,key=d.get),

print '\nA:',
for i in l:
    print i.count('A'),
print '\nC:',
for i in l:
    print i.count('C'),
print '\nG:',
for i in l:
    print i.count('G'),
print '\nT:',
for i in l:
    print i.count('T'),