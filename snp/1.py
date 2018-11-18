f = open("1.txt")
c=0
for line in f:
	if c == 0:
		string = line.strip()
		c+=1
	else:
		sub = line.strip()

#print(string.find(sub))

c = 0
for i in range(0,len(string)):
	if string[i] != sub[i]:
		c+=1
print(c)