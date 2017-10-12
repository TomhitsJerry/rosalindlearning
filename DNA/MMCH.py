from Bio import SeqIO
from math import factorial
sequence = ''
with open('sampledata.fasta', 'r') as f:
    for record in SeqIO.parse(f, 'fasta'):
        sequence = str(record.seq)

A, U, G, C = 0, 0, 0, 0
for nt in sequence:
    if nt == 'A':
        A += 1
    elif nt == 'U':
        U += 1
    elif nt == 'G':
        G += 1
    elif nt == 'C':
        C += 1

AU = factorial(max(A, U)) / factorial(max(A, U) - min(A, U))
GC = factorial(max(G, C)) / factorial(max(G, C) - min(G, C))
print(int(AU * GC))
