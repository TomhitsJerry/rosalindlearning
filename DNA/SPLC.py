with open('/home/cyagen1/Downloads/rosalind_orf.txt','r' )as f:
    t=f.read()
DNA=''.join(t.split(">")[1].split('\n')[1:])###DNA
for i in t.split(">")[2:]:
    t=i.split('\n')[1]
    DNA=DNA.replace(t,'')

RNA=DNA.replace('T','U')

print RNA






















