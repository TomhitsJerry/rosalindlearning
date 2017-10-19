#used for learning update commit push
#used for clone pull
ff=open('/home/cyagen1/rat_g.fa','w')
with open('/home/cyagen1/rat_g.csv','r')as f:
    i=1
    while i<=119614862:
        title='>'+str(i)+'\n'
        w = f.readline().strip().split(',')[0]
        ff.write(title)
        ff.write(w)
        ff.write('\n')
        i+=1
