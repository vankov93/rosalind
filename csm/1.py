
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
    answer = ""
    if string1 == string2:
        return(string1)
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer


data = get_long("/home/avito_chatun/Downloads/rosalind_lcsm.txt")[::-1]


pool = []

for i in range(len(data)):
	for j in range(len(data)):
		if i != j:
			ans = longestSubstringFinder(data[i][1], data[j][1])
			if ans != "":
				pool.append(ans)
		print(len(pool))
pool = list(set(pool))


candodats = []

for i in pool:
	for j in range(len(data)):
		if i not in data[j][1]:
			break
		if j == len(data)-1:
			candodats.append(i)
max = 0
for i in candodats:
	if len(i) > max:
		max = len(i)
		ans = i
print(ans)
	



	