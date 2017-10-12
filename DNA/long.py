with open ('/home/cyagen1/Downloads/rosalind_long.txt','r')as f:
    w=f.readline().strip()
    L=[]
    while w:
        if '>' not in w:
            L.append(w)
        w = f.readline().strip()
k=len(L[0])
kmer=(k/2)+1
while kmer <k-1:#=total equal
    for j in range(1,len(L)):         ####len(L)cannot change
        if L[0][:kmer]==L[j][-kmer:]:
            t=L[j]+L[0][kmer:]
            L.remove(L[j])
            break
        elif L[j][:kmer]==L[0][-kmer:]:
            t = L[0] + L[j][kmer:]
            L.remove(L[j])
            break
    kmer+=1
print L[0]