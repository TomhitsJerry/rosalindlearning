with open('/home/cyagen1/rosalind_gc.txt','r')as f:
    w=f.read()
zhizhen={}
for i in w.split(">")[1:]:
    whole=i.split('\n')
    title=whole[0]
    content=''.join(whole[1:])
    gc=(content.count('G')+content.count('C'))/float(len(content))*100
    zhizhen[gc]=title
print zhizhen[max(zhizhen)],max(zhizhen)