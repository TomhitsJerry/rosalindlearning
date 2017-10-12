with open ('/home/cyagen1/rosalind_gc.txt','r')as f:
    w=f.read()
Dhead={}
Dtail={}
for i in w.split('>')[1:]:
    title=i.split('\n')[0]
    content=''.join(i.split('\n')[1:])
    head=content[:3]
    tail=content[-3:]
    Dhead[title]=head
    Dtail[title]=tail
for i in Dhead:
    for j in Dtail:
        if i!=j and Dhead[i]==Dtail[j]:
            print j,i




