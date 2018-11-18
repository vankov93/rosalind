def transcript(dna):
	d={"A" : "U", "T" : "A", "G": "C", "C": "G"}
	dna = dna.strip().upper()
	rev = ""
	for n in dna:
		rev = rev + d[n]
	return(rev[::-1])

def translate(rna): # check presense of STOP codon, return None if there is no STOP
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
	s = 0
	#ak = inv_map = {v: k for k, v in table()}
	rna = rna[rna.find("AUG"):]
	i=0
	prot = ""
	while i < len(rna)-3:
		codon = rna[i:i+3]
		if table[codon]=="STOP":
			s = 1
			break
		prot = prot + table[codon]
		#print(rna[i:i+3], table[rna[i:i+3]])
		i+=3
	s = 1 #uncomment to disable STOP codon checking
	if s == 1:
		return(prot.upper())



def get_long(path_to_fasta): # take fasta, return {"header": "single_string"}
	f = open(path_to_fasta)
	s = "" 
	d = []
	head = ""
	s=""
	for line in f:
		if ">" in line:
			d.append([head, s])
			s = ""
			head = line[1:].strip()
		if ">" not in line:
			s = s + line.strip()
	d.append([head, s])
	d.pop(0)
	return(d)


def reverce_dna(dna):
	d={"A" : "T", "T" : "A", "G": "C", "C": "G"}
	dna = dna.strip().upper()
	rev = ""
	for n in dna:
		rev = rev + d[n]
	return(rev[::-1])


seq = get_long("/home/avito_chatun/Downloads/rosalind_splc.txt")
dna = seq.pop(0)[1]
introns = []
for i in seq:
	introns.append(i[1])
for i in introns:
	dna = dna[:dna.find(i)] + dna[dna.find(i)+len(i):]
print(translate(transcript(reverce_dna(dna))))















