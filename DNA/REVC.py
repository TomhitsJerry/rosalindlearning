str="AAAACCCGGT"
str=str[::-1]
for i in str:
    if i =='A':
        print 'T',
    elif i=='T':
        print 'A',
    elif i=='G':
        print 'C',
    else:
        print 'C',
