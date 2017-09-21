n=raw_input("n:")
k=raw_input("k:")
n,k=int(n),int(k)
def fx(x):
    if x==0:
        return 1
    else:
        return x*fx(x-1)
t1=fx(n)/(fx(n-k)*fx(k))
print (t1*fx(k))%1000000