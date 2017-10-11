
with open ('/home/cyagen1/Downloads/rosalind_lcsq.txt','r')as f:
    w=f.read()
s=''.join(w.split('>')[1].split('\n')[1:])
t=''.join(w.split('>')[2].split('\n')[1:])

lengths = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

for i, x in enumerate(s):
    for j, y in enumerate(t):
        if x == y:
            lengths[i + 1][j + 1] = lengths[i][j] + 1
        else:
            lengths[i + 1][j + 1] = max(lengths[i + 1][j], lengths[i][j + 1])


e= ''
i, j = len(s), len(t)
while i * j != 0:
    if lengths[i][j] == lengths[i][j - 1]:
        j -= 1
    elif lengths[i][j] == lengths[i - 1][j]:           #cannot if
        i -= 1
    else:
        e = s[i - 1] + e
        i -= 1
        j -= 1
print e