def get_long(path_to_fasta): # take fasta, return [["header", "single_string"]...]
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
	#s = 1 #uncomment to disable STOP codon checking
	if s == 1:
		return(prot.upper())




def orf(dna): #return all candidat proteins from all 6 orfs
	rnas = []
	orfs=[]
	t = transcript(dna)
	rnas.append(t)
	rnas.append(t[1:])
	rnas.append(t[2:])
	t2 = transcript(reverce_dna(dna))
	rnas.append(t2)
	rnas.append(t2[1:])
	rnas.append(t2[2:])
	for rna in rnas:
		while len(rna) >=3:
			codon = rna[0:3]
			if codon != "AUG":
				rna = rna[3:]
			else:
				orfs.append(translate(rna))
				rna = rna[3:]
	return(list(set(orfs)))
		