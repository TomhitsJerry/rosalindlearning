with open('/home/cyagen1/Downloads/rosalind_kmer.txt','r')as f:
    t=f.read()
    L=[]
    [L.append(''.join(i.split('\n')[1:]))for i in t.split('>')[1:]]
matrix=[[0 for col in range(len(L))]for row in range(len(L))]
for i in range(len(L)):
    for j in range(len(L)):
        count=0
        for k in range(len(L[0])):
            if L[i][k]!=L[j][k]:
                count+=1
        matrix[i][j]=float(count)/len(L[0])

for i in matrix:
    for j in i:
        print  "%.5f"%j,
    print ""