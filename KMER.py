with open('/home/cyagen1/Downloads/1','r')as f:
    w=''.join(f.read().split('\n')[1:])
import itertools
k=4
li=list(itertools.product(['A','T','G','C'],repeat=k))
dict={}
for i in li:
    i=''.join(i)
    dict[i]=0
for j in range(len(w)-k+1):
    if w[j:j+k] in dict.keys():
        dict[w[j:j+k]]+=1

for i in sorted(dict):
    print dict[i],
