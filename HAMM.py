s1 = 'GAGCCTACTAACGGGAT'
s2 = 'CATCGTAATGACGGCCT'
point=0
i=0
for i in range(len(s1)):
    if s1[i]==s2[i]:
        continue

    else:
        point += 1
        
print point