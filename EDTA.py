from Bio import SeqIO
w=SeqIO.parse('/home/cyagen1/Downloads/dict.txt','fasta')
l=[i.seq for i in w]
L=[[0 for col in range(len(l[0])+1)]for row in range(len(l[1])+1)]
for i in range(1,len(l[0])+1):
    L[0][i]=i
for i in range(1,len(l[1])+1):
    L[i][0]=i
for i in range(1,len(l[1])+1):
    for j in range(1,len(l[0])+1):
        if l[1][i-1]==l[0][j-1]:
            L[i][j]=L[i-1][j-1]
        else:
            L[i][j] =min(L[i-1][j-1]+1,L[i-1][j]+1,L[i][j-1]+1)
i,j=len(l[1]),len(l[0])
w=''
u=''
while i!=0 or j!=0:
    if L[i][j]==L[i-1][j]+1:
        w='-'+w
        u=l[1][i-1]+u
        i-=1
    elif L[i][j]==L[i][j-1]+1:
        w=l[0][j-1]+w
        u='-'+u
        j-=1
    elif L[i][j]==L[i-1][j-1]:
        w=l[0][j-1]+w
        u=l[1][i-1]+u
        i-=1
        j-=1
    else:
        w = l[0][j - 1]+w
        u = l[1][i - 1]+u
        i-=1
        j-=1
print L[len(l[1])][len(l[0])]
print w
print u