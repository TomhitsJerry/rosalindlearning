def fibonacciRabbits(n, m):
    F = [0, 1, 1]
    for i in range(3, n + 1):
        if i <= m:
            total = F[i - 1] + F[i - 2]
        elif i == m + 1:
            total = F[i - 1] + F[i - 2] - 1
        else:
            total = F[i - 1] + F[i - 2] - F[i - m - 1]##whole number -old number
        F.append(total)
    return (F[n])
print  fibonacciRabbits(98,20)
####def fib(n,k=1):
####ages = [1] + [0]*(k-1)

####  for i in xrange(n-1):

####    ages = [sum(ages[1:])] + ages[:-1]

####  return sum(ages)
####print fib(6,3)
#[new-bornt,grown-up,old]
#in each generation,N:grown-up number =N-1:new-bornt number
#N:old number =N-1:grown-up number
#N:new-bront number=N-1:grown-up+old
