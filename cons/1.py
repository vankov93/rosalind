f = open("/home/avito_chatun/Downloads/rosalind_cons(1).txt")
dna = []
d = {"A": [], "C" : [], "G": [], "T": []}
lines = []
s = ""
for line in f:
	if ">" in line:
		lines.append(s)
		s = ""
	if ">" not in line:
		s = s + line.strip()
lines.append(s)
#lines.pop(0)

for line in lines:
	line = line.strip()
	l = len(line)
	for i in range(0,l):
		if len(d[line[i]]) < l:
			d[line[i]] = [0] * l
		d[line[i]][i] = d[line[i]][i]+1

con = ""
c=0
for i in range(0,l):
	c=c+1
	max = 0
	for n in ["A", "C", "G", "T"]:
		if d[n][i] >= max:
			max = d[n][i]
	for k in ["A", "C", "G", "T"]:
		if d[k][i] == max:
			con = con + k
			break

print(con.strip())
#print("con", len(con.strip()))


for n in ["A", "C", "G", "T"]:
	s = n + ": " 
	for j in d[n]:
		s = s + str(j) + " "
	
	#print("matrix", len(s)/2)
	print(s.strip())

	