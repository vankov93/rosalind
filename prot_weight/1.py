f = open("table.txt")
d = {}
for line in f:
	line = line.split()
	d[line[0]] = float(line[1])
f = open("1.txt")
for line in f:
	prot = line.strip()
w = 0
for aa in prot:
	w = w + d[aa]
print(w)