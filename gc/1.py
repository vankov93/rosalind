f = open("1.fa")
def gc(dna):
	c = 0
	for nuc in dna:
		if nuc == "G" or nuc == "C":
			c+=1
	return(c/len(dna)*100)
	
read = "a"
maxh = ""
head = ""
maxgc = 0
for line in f:
	if ">" in line:
		hea = line[1:].strip()
		gcr = gc(read)
		if gcr > maxgc:
			maxgc = gcr
			maxh = head		
		read = ""
	else:
		read = read + line.strip()
		head = hea
gcr = gc(read)
if gcr > maxgc:
	maxgc = gcr
	maxh = head

print(maxh)
print(maxgc)
			