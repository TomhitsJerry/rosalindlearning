f=open('/home/cyagen1/Downloads/out.txt','w')
import itertools
string="FCVBLHTWQO"
list=[]
for i in range(len(string)):
    list.append(string[i])
n=4
l=[]
while n>=1:
    lettera=itertools.product(list, repeat=n)
    for i in lettera:
        l.append(''.join(i))
    n-=1
srt_perm = sorted(l,key=lambda word: [string.index(c) for c in word])######can't understand
for j in srt_perm:
    f.write('%s\n' % j)
f.close()