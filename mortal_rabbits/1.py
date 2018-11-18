f = open("1.txt")
for line in f:
	line = line.split()
n=int(line[0])
m=int(line[1])
p = 0
#rabbits[i]
rabbits = [0]
print(m,n)
for i in range(0,n-1):
	for i  in range(0,len(rabbits)):
		new = []
		if rabbits[i] >1 and rabbits[i] <= m:
			new.append(0)
			new.append(0)
			rabbits[i]+=1
		elif rabbits[i] <= m:
			rabbits[i]+=1
		rabbits = rabbits + new
	print(rabbits[0:5])
c=0
for i in rabbits:
	if i <m:
		c+=1
print(c)
	
