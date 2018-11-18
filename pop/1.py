f = open("1.txt")


'''

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa
'''


for line in f:
		l = line.split()
s = (2*int(l[0])+2*int(l[1])+2*int(l[2])+2*0.75*int(l[3])+1*int(l[4]))
print(s)