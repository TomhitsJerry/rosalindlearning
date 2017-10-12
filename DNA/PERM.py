def f(n):
    if n == 1:
        return 1
    else:
        return f(n-1)*n
n=raw_input("print a num:")
n=int(n)
t=f(n)
print t
list=[i for i in range(1,n+1)]

import itertools
L=[]
for i in itertools.permutations(list):
    for e in i:
        print e,
    print ""