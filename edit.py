from Bio import SeqIO   ##求edit距离。gap\mismatch。
seq=[]
for i in SeqIO.parse('/home/cyagen1/Downloads/dict.txt','fasta'):
    seq.append(i.seq)
##init初始化，gap+1
L= [[0 for j in range(len(seq[0]) + 1)] for i in range(len(seq[1]) + 1)]
for i in range(1,len(seq[0])+1):
    L[0][i]=i
for i in range(1,len(seq[1])+1):
    L[i][0]=i
###

for i in range(1,len(seq[1])+1):
    for j in range(1,len(seq[0])+1):
        if seq[1][i-1]==seq[0][j-1]:#match不是要求的
            L[i][j]=L[i-1][j-1]
        else:
            L[i][j] =min(L[i - 1][j - 1]+1, L[i - 1][j]+1, L[i][j - 1] +1)##gap+1\mismatch+1.求算使edit最少的min
print L[len(seq[1])][len(seq[0])]
