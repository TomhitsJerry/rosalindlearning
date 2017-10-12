data = []
with open('/home/cyagen1/Downloads/rosalind_seto.txt','r') as f:
    for line in f:
        data.append(line.strip('\n'))
U = set(str(i)for i in range(1, int(data[0])+1))
A = set([x for x in data[1].strip('{}').replace(' ','').split(',')])
B = set([x for x in data[2].strip('{}').replace(' ','').split(',')])

union = A.union(B)
intersection = A.intersection(B)
diff_AB = A-B
diff_BA = B-A
A_comp = U-A
B_comp = U-B
ff=open('/home/cyagen1/Downloads/s.txt','w')
ff.write('{'+','.join(union)+'}')
ff.write('{'+','.join(intersection)+'}')
ff.write('{'+','.join(diff_AB)+'}')
ff.write('{'+','.join(diff_BA)+'}')
ff.write('{'+','.join(A_comp)+'}')
ff.write('{'+','.join(B_comp)+'}')
#def get_sets(n, a, b):
#    return [a | b, a & b, a - b, b - a, set(range(1, n + 1)) - a, set(range(1, n + 1)) - b]


#def format_output(result):
 #   b = open('/home/cyagen1/Downloads/rosalind_setoout.txt', 'w')
  #  for r in result:
   #     print "{" + ', '.join(map(str, r)) + "}"
    #    b.write("{" + ', '.join(map(str, r)) + "}\n")


#def parse(line):
 #   return [s.strip() for s in line.strip()[1:-1].split(",")]


#if __name__ == '__main__':
 #   n, a, b = open('/home/cyagen1/Downloads/rosalind_seto.txt').readlines()

#    n = int(n.strip())
 #   a = set(map(int, parse(a)))
  #  b = set(map(int, parse(b)))

   # format_output(get_sets(n, a, b))