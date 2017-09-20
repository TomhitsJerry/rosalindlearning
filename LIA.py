k=raw_input("generation:")
n=raw_input("at least number:")
k,n=int(k),int(n)
sum=0
def C(t):
    p=1
    while p:
        if t==0:
            return p
        else:
            p=p*t
            t=t-1
total=2**k
for i in range(n,2**k+1):
	#print C(total),C(i),C(total-i)

	t=float(C(total))/(C(i)*C(total-i))
	sum+=(0.25**i)*(0.75**(2**k-i))*t
print "%.3f"%sum