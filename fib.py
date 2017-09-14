n=raw_input()#month
k=raw_input()#k pairs each productedage
n=int (n)
k=int(k)
def fib(n,k):
    if n<=2:
        return 1
    else:
        return fib(n-1,k)+fib(n-2,k)*k
out=fib(n,k)
print out

