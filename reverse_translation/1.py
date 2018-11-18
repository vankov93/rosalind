f = open("1.txt")
for line in f:
	prot = line.strip()


table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


ak = {}

for i in table:
	if table[i] not in ak:
		ak[table[i]] = [i]
	else:
		ak[table[i]].append(i)
'''
ak  = {'F': ['UUC', "UUU"], 'L': ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"], 'S': ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"], 
    'Y': ['UAC', "UAU"], 'STOP': ['UGA', "UAA", "UAG"], 'C': ['UGC', "UGU", "UGG"], 'W': ['UGG'], 'P': ['CCG', "CCA", "CCC", "CCU"],
    'H': ['CAC', "CAU"], 'Q': ['CAG', "CAA"], 'R': ['AGG', "AGA", "CGU", "CGC", "CGA", "CGG", "AGA"],
    'I': ['AUA', "AUU", "AUC"], 'M': ['AUG'], 'T': ['ACG', "ACA", "ACC", "ACU"], 'N': ['AAC', "AAU"], 'K': ['AAG', "AAA"], 
    'V': ['GUG', "GUU", "GUC", "GUA"], 'A': ['GCG', "GCA", "GCC", "GCU"], 'D': ['GAC', "GAU"], 'E': ['GAG', "GAA"], 'G': ['GGG', "GGA", "GGC", "GGU"]}




print(len(table))

lak = 0
for i in ak:
	lak = lac + len(d[i])
prnt(lak)



for i in ak:
	print(i, len(ak[i]))

'''

n = 1
for i in prot:
	n=n*len(ak[i])
	#print(i, str(n)[-5:], "*" , len(ak[i]))
	#print(n, len(ak[i]))
print(n*3%1000000)