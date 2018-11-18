k = 3 

import random


def reverce(read):
    return [read[0], read[1][::-1]]

def check(k, read1, read2):
  #print(read1[1][0:k], read2[1][-k:])
  if read1[1][0:k] == read2[1][-k:]:
    return [read2[1][:-k] + read1[1], read2[0] + " " +read1[0]]
  else:
    read = read1
    read1 = read2
    read2 = read
    #print(read1[1][0:k], read2[1][-k:])
    if read1[1][0:k] == read2[1][-k:]:
      return [read2[1][:-k] + read1[1], read2[0] + " " +read1[0]]
    else:
      read2 = reverce(read2)
      #print(read1[1][0:k], read2[1][-k:])
      if read1[1][0:k] == read2[1][-k:]:
        return [read2[1][:-k] + read1[1], read2[0] + " " +read1[0]]
      else:
        read = read1
        read1 = read2
        read2 = read
        #print(read1[1][0:k], read2[1][-k:])
        if read1[1][0:k] == read2[1][-k:]:
          return [read2[1][:-k] + read1[1], read2[0] + " " +read1[0]]
        else:
          return ["nope"]






f3 = open("3.txt", "w")
f = open("1.txt")
for line in f:
    line = line.strip()
    if ">" in line:
        f3.write("\n" + line + "\n")
    else:
        f3.write(line)


f = open("3.txt")
reads = []
for line in f:
    if len(line) > 2:
        line = line.strip()
        if ">" in line:
            read = []
            read.append(line[1:])
        else:
            read.append(line)
            reads.append(read)





singles = []
lep = len(reads)

n = 0
ma = []
for i in range (0, 10000):
    li = []
    primer = reads[random.randrange(0, len(reads))]
    contig = primer
    #print("primer", primer)
    lep = len(reads)
    for read in reads:
        if read != primer:
            res = check(k, read, contig)
            if len(res) > 1:
                contig = res[::-1]
                #print(contig)
                ass = contig[0]
                ass = ass.split()
                li.append(ass[0] + " " + ass[1])
    #print(len(li))
    if len(li) > len(ma):
        ma = li
    print(len(contig[1]))


for i in ma:
    print(i)



		
		
	
		
