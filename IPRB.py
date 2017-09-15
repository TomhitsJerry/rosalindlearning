k=raw_input("AA number:")
m=raw_input("Aa number:")
n=raw_input("aa number:")
k=int(k)
m=int(m)
n=int(n)
total=k+m+n
Ptotal=total*(total-1)/2.0
Paa=1/8.0*m*(m-1)+n*(n-1)/2.0+m*n/2.0
out=1-(Paa/Ptotal)
print round(out,5)