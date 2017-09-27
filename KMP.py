#Speeding up motif finding
##foreach   p[K] is the longest substring of prefix.note!prefix,starting from the start.
from Bio import SeqIO
record = SeqIO.read('/home/cyagen1/Downloads/rosalind_revp.txt', 'fasta')
sequence = list(record.seq)

F_array = [0] * len(sequence)
k = 0
for i in range(2, len(sequence) + 1):
    while k > 0 and sequence[k] != sequence[i - 1]:
        k = F_array[k - 1]
    if sequence[k] == sequence[i - 1]:
        k += 1
    F_array[i - 1] = k

print ' '.join(map(str, F_array))