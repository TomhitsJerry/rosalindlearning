f=open('/home/cyagen1/Downloads/rosalind_lia.txt','r')
w=f.read()
L=[]
for i in w.split('>')[1:]:
   L.append(''.join(i.split("\n")[1:]))
trans=0
tranv=0
print L[1]
for i in range(len(L[0])):
    if L[0][i]!=L[1][i]:

        if L[0][i]=='A'and L[1][i]=='G'or L[0][i]=='G' and L[1][i]=='A':
            trans+=1
        elif L[0][i]=='T'and L[1][i]=='C'or L[0][i]=='C' and L[1][i]=='T':
            trans+=1
        else:
            tranv+=1
print float(trans)/tranv