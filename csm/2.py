import random
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

def longestSubstringFinder(string1, string2):
    answer = []
    if string1 != string2:
        len1, len2 = len(string1), len(string2)
        for i in range(len1):
            match = ""
            for j in range(len2):
                if (i + j < len1 and string1[i + j] == string2[j]):
                    match += string2[j]
                else:
                    if len(match) > 2:
                        answer.append(match)
                    match = ""
    return answer

data = get_long("/home/avito_chatun/Downloads/rosalind_lcsm(5).txt")[::-1]



maxs = []

m = 0
ans = ""
for i in range(0,100):
	print(i)

	canditats = []

	r = random.randrange(0, len(data))

	first = data[r][1]
	c=0



	canditats = canditats + longestSubstringFinder(first, data[r-1][1])
	canditats = list(set(canditats))
	canditats2=[]


	for i in canditats:
		for j in range(2,len(i)-1):
			n = 0
			while n + j < len(i):
				new = i[n:n+j]
				canditats2.append(new)
				n+=1



	canditats = list(set(canditats2))
	cand = []



	for i in canditats:
		for j in data:
			c = c+1
			if i not in j[1]:
				break
			else:
				if c == len(data):
					cand.append(i)
					
					c=0



	cand = list(set(cand))


	d = {}
	for i in cand: 
		if len(i) not in d:
			d[len(i)] = []
			d[len(i)].append(i)
		else:
			d[len(i)].append(i)
	k = list(d.keys())
	k.sort()
	k = k[::-1]
	maxs.append([k[0], d[k[0]]])
	if k[0] > m:
		m = k[0]
		a = open("ans.txt", 'w')
		print(m, i[1])
		a.write(d[k[0]][0])




# ['ATACGGATGG', 'GAGGTGACAA', 'CACAGAGGAG'] ['CACAGAGGAG', 'GAGGTGACAA']
		























































