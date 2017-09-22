with open ('/home/cyagen1/Downloads/rosalind_perm.txt','r')as f:
    w=f.read()
L=[]
for i in w.split('>')[1:]:
    L.append(''.join(i.split('\n')[1:]))
loca=0
for i in L[1]:
    loca=L[0].find(i,loca)
    print loca+1,
    loca+=1


