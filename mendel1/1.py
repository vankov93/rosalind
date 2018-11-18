f = open("1.txt")
import random
for line in f:
	line = line.split()
	AA = int(line[0])
	Aa = int(line[1])
	aa = int(line[2])
	s = AA+Aa+aa	
l = ["AA"] * AA + ["Aa"] * Aa + ["aa"] * aa

O = 0
sa = 10000

A = 0
for i in range (0, len(l)*sa):
	lc = l.copy()
	#print(lc)
	r1 = lc.pop(random.randrange(0, s))
	#print(lc)
	r2 = lc[random.randrange(0, s-1)]
	
	if r1 == "AA" or r2 == "AA":
		A+=1
	elif r1 == "Aa" and r2 == "Aa":
		A+=0.75
	elif (r1 == "Aa" and r2 == "aa") or (r2 == "Aa" and r1 == "aa"):
		A+=0.5
	#print(r1, r2, A)
print(A/(len(l)*sa))