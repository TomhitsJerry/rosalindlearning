import sys

sys.setrecursionlimit(1000000)
n=1865
m=1175
def fx(t):
    if t==0:
        return 1
    else:
      return  fx(t-1)*t
sum=0
for k in range(m):
    t=fx(n)/(fx(k)*fx(n-k))
    sum+=t
print ((2**n)-sum)%1000000
##########MATH模块
##from math import factorial
##factorial是阶乘