dict={'G':4,'V':4,'A':4,'L':6,'I':3,'P':4,'F':2,'Y':2,'W':1,'S':6, 'T':4,'M':1,'C':2,'N':2,'Q':2,'K':2,'R':6,'H':2,'D':2,'E':2}
with open('/home/cyagen1/Downloads/rosalind_mrna.txt','r')as f:
      t=f.read().rstrip()
print t
out=1
for i in t:
    out*=dict[i]
out=3*out
print out%1000000