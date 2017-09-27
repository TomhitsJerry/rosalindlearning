with open("/home/cyagen1/Downloads/rosalind_kmer.txt")as f:
    f.readline()
    w=f.readline().strip()
    l=""
    while w:
        l+=w
        w = f.readline().strip()
for j,k in enumerate(range(4,13,2)):
    L=[]
    for i in range(len(l)):
        if len(l[i:i+k])==k:
            L.append(l[i:i+k])

            i+=1
        else:
            break
    for hh,i in enumerate(L):
        t=i[:j + 1:-1].replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
        if i[0:j+2]==t:
            print hh+1, len(i)
