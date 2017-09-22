N=97029
p=0.401082
str="CCGCGTTA"
gc=str.count('G')+str.count('C')
at=str.count('A')+str.count('T')
t=(1-p)/2
p=p/2

print  "%.3f"% (1- (1-(t**at)*(p**gc))**N)