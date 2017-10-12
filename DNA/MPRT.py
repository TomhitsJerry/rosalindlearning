import urllib
f=open('/home/cyagen1/Downloads/rosalind_lia.txt','r')
L=f.readlines()
list=[]
import re
for i in L:
    i=i.strip()
    url = "http://www.uniprot.org/uniprot/" + i + ".fasta"
    content = urllib.urlopen(url).read()
    content = ''.join(content.split("\n")[1:])
    if re.search(r'(\w)?(N[^P][ST][^P])(\w)?', content):
        print i
        pattern = re.compile(r'N[^P][ST][^P]')
        k = 0
        while k <= len(content) - 4:

            if pattern.search(content, k):
                print pattern.search(content, k).start() + 1,
                k = pattern.search(content, k).start() + 1
            else:
                break
    else:
        continue
    print ""