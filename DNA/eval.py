f=open('/home/cyagen1/Downloads/dict.txt')
w=f.readlines()
f.close()
n=int(w[0].strip())
tar=w[1].strip()
AT=tar.count('A')+tar.count('T')
GC=tar.count('G')+tar.count('C')
for i in w[2].split():
    i=float(i)
    result = ((i / 2) ** GC) * (((1 - i) / 2) ** AT) * (n - len(tar) + 1)
    print round(result,3)

