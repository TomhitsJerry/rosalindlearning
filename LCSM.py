with open("/home/cyagen1/rosalind_gc.txt",'r') as f:
    w=f.read()
first=''.join(w.split('>')[1].split('\n')[1:])
content=[]
for item in w.split('>')[2:]:
    content.append(''.join(item.split('\n')[1:]))
k=2
L=[]
i=0
seed=[]
out={}
while i<=len(first)-k:#########seed
    L.append(first[i:i+2])
    i+=1
for i,item in enumerate(L):
    flag=0
    for j in content:
        if item in j:
            flag+=1
            if flag==len(content):
                seed.append(i)##########seed ji lu 2kmers de weizhi
        else:
            break
mi=min(len(l) for l in content)
min=min(len(first),mi)
while k<=min:
    k+=1########
    for i in seed :
        if (i+k)<=len(first):
            t=first[i:i+k]
            flag=0
            for j in content:
                if t in j:
                    flag+=1
                    if flag==len(content):
                        out[t]=len(t)    #  bug : ruguok==2,
                else:
                    break
max=max(out,key=out.get)
print max

