data = []
with open('/home/cyagen1/Downloads/rosalind_rstr.txt', 'r') as f:
    for line in f:
        split_data = [int(x) for x in line.split()]
        data.append(split_data)

n = data[0][0]
edges = data[1:]
print(n - len(edges) - 1)