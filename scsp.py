with open('/home/cyagen1/Downloads/dict.txt','r')as f:
    t=f.readline().strip()
    s=f.readline().strip()
L=[[0 for col in range(len(t)+1)]for row in range(len(s)+1)]
for i in range(1,len(t)+1):
    L[0][i]=-i
for i in range(1,len(s)+1):
    L[i][0]=-i
for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1]==t[j-1]:
            L[i][j]=L[i-1][j-1]+1
        else:
            L[i][j]=max(L[i-1][j]-1,L[i][j-1]-1)

i,j=len(s),len(t)
#w=''
#u=''
e=''
while i!=0 or j!=0 :
    if L[i][j] == L[i][j - 1]-1:
 #       w= t[j - 1]+w
 #       u='-'+u
        e=t[j - 1]+e
        j -= 1
    elif L[i][j] == L[i - 1][j]-1:

  #      w='-'+w
  #      u=s[i-1]+u
        e=s[i-1]+e
        i -= 1

    else:
  #      w=t[j-1]+w
  #      u=s[i-1]+u
        e=t[j-1]+e
        i -= 1
        j -= 1

#print w
#print u
print e