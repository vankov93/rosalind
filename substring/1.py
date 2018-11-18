f = open("1.txt")
c=0
for line in f:
	if c == 0:
		string = line.strip()
		c+=1
	else:
		sub = line.strip()

#print(string.find(sub))

f = 1
c = [0]
while True:
	f = string.find(sub)
	if f == -1:
		break
	c.append(f+1+c[-1])
	string = string[string.find(sub)+1:]
s = ""
c.pop(0)
for i in c:
	s = s + str(i) + " "
print(s)
