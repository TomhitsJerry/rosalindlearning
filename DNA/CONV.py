with open ('/home/cyagen1/Downloads/rosalind_conv.txt','r')as f:
    l1=[float(line.strip()) for line in f.readline().strip().split(' ')]
    l2=[float(line.strip()) for line in f.readline().strip().split(' ')]
t=[]
for i in l1:
    for j in l2:
        t.append(round(i-j,5))

from collections import Counter
c=Counter(t)
print c.most_common(1)[0][1],'\n',c.most_common(1)[0][0]