f=open('/home/cyagen1/Downloads/rosalind_orf.txt','r')
t = f.readlines()
string=""
for line in  t:
    if ">" in line:
        pass
    else:
        line=line.strip()
        string+=line
rev_com=string.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]##3->5 reverse and compliment

dict={'TTT':'F', 'CTT':'L',      'ATT': 'I',      'GTT':'V',
'TTC': 'F',     'CTC':'L',       'ATC': 'I',      'GTC': 'V',
'TTA':'L',      'CTA': 'L',      'ATA': 'I',      'GTA': 'V',
'TTG':'L',      'CTG': 'L',      'ATG': 'M',      'GTG': 'V',
'TCT':'S',      'CCT': 'P',      'ACT': 'T',      'GCT': 'A',
'TCC':'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'TCA':'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'TCG':'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'TAT':'Y',      'CAT': 'H',      'AAT': 'N',      'GAT': 'D',
'TAC':'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',   'CAG': 'Q',
'AAG': 'K',      'GAG': 'E',     'TGT':'C',      'CGT': 'R',
'AGT': 'S',      'GGT': 'G',     'TGC':'C',      'CGC': 'R',
'AGC': 'S',      'GGC': 'G',     'CGA': 'R',      'AGA': 'R',
'GGA': 'G',      'TGG':'W',      'CGG': 'R',      'AGG': 'R',
'GGG': 'G','TAG':'Stop','TGA':'Stop',
'TAA':'Stop',}
#def find_start(str):
#    = str.index('')
diction={}
for x in [rev_com,string]:
    for i in range(len(x)-2):
        if x[i:i+3]=="ATG":
            k=1
            out=""
            while k:
                if dict[x[i:i+3]]=="Stop":
                    if out not in diction.keys():
                        diction[out]=1
                    else:
                        diction[out]+=1
                    break
                else:
                    out+=dict[x[i:i+3]]
                    i+=3
                    if i>=len(x)-2:
                        break
for i in diction:
    print i

            #####################qu chong fu and orf must have start and end