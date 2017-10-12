def fx(t):
    if t==0:
        return 1
    else:
      return  fx(t-1)*t
n=862
sum=0
for i in range(n+1):
    sum+=fx(n)/(fx(n-i)*fx(i))
print sum%1000000