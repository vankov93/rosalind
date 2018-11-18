f = open("1.txt")
for line in f:
	line = line.split()
n=int(line[0])
k=int(line[1])
p = 0
new = [0, 1]
for i in range(0,n):
	new.append(p*3)
	p = p + new[-2]
	print(p, new)
print(p)