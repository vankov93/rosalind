f = open("1.txt")
for line in f:
	line = line.split()
n=int(line[0])
m=int(line[1])
m = m 
poc = 1
print(n, m)
rabbits = [0]*m
rabbits[0] = 1
print(poc, rabbits)
for i in range(0,n-1):
	poc +=1
	new = 0
	for i  in range(1,m):
		
		new = new + rabbits[i]*1
	rabbits.insert(0, new)
	print(poc, rabbits[:m])
	
		

c=0
for i in range(0,m):
	c = c+rabbits[i]
print(c)
	
