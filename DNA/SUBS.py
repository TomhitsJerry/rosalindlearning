str="CGAGGAGCGAGGAGGCGCGAGGAGCGCGAGGAGCGAGGAGATCGAGGAGCGAGGAGCGTCGAGGAGGCGAGGAGAGGCGAGGAGCGAGGAGCGAGGAGGCCGAGGAGCGAGGAGCGTCGAGGAGCGAGCGAGGAGAGCGAGGAGCGAGGAGGACGAGGAGCGAGGAGCGAGGAGTCGAGGAGATCTAACGAGGAGTTCGGCGAGGAGCGAGGAGCGAGGAGATTCGAGGAGGGGCGAGGAGAGCGAGGAGCGAGGAGAGCTCGAGGAGCCTTATACGAGGAGGACGAGGAGGGTACGAGGAGGTAGCCGAGGAGCGAGGAGATTCGAGGAGCGGCGCACGCTAATACCGAGGAGAAGTCAAAACGAGGAGCGAGGAGCGAGGAGCGAGGAGCACGAGGAGGCGAGGAGTCCACGAGGAGGCGAGGAGAAGAGCGAGGAGCGCGAGGAGGACGAGGAGTGTCCCGAGGAGCGAGGAGCCGAGGAGCTGGGCAGCGAGGAGTCCGAGGAGTCTTCCCACAACGAGGAGAGTAACGAGGAGTAACGAGGAGGCCACCGAGGAGCGAGGAGTCGAGGAGCGAGGAGGAGGCGAGGAGGACGAGGAGGTGCGAGGAGGTCGAGGAGCGAGGAGCACGAGGAGGTTCGAGGAGCGCCACCGAGGAGAAGAAGCGAGGAGGTTTACCGAGGAGCTACTGGGGACGAGGAGCCGAGGAGACGGGCGCCGAGGAGTTCGCTCGAGGAGAAGCGCGAGGAGGTCGAGGAGGGGCGAGGAGCGAGGAGCGAGGAGCGAGGAGCTAGGCGAGGAGATTCAGATTCTGGGCAGGGGTCACGAGGAGTCGAGGAGCGAGGAGGCCGAGGAGTTGCGAGGAGCGAGGAGGGTAAACCGAGGAGCGAGGAGGTCGAGGAGACACTCCGAGGAGCCGAGGAGGCGAGGAGACCCCGAGGAGACGAGGAGGCGAGGAGCGC"
motif="CGAGGAGCG"
def location(x,y):
    if len(x)>len(y):
        print "wrong orders,try to exchange their orders."
    else:
        i=0
        while i<len(y)-len(x)+1:
            if x==y[i:i+len(x)]:
                print i+1,
            i+=1
    return
#    if y[0]
location(motif,str)