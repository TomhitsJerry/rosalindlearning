f=open('/home/cyagen1/Downloads/dict.txt','r')
line=f.readline().strip()
dict={}
while line:
    value=line.split('   ')[1]
    key=line.split('   ')[0]
    dict[key] = value
    line = f.readline().strip()
fs=open('/home/cyagen1/Downloads/rosalind_fibd.txt','r')
whole=fs.read().strip()
sum=0
for i in whole:
    t=  float(dict[i])
    sum +=t
print "%0.3f"%sum



    # key=line.split('   ')[0]
    #value=line.split('   ')[1]
    #dict[key]=value