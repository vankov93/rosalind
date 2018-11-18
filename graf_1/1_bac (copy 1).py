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






f = open("2.txt")
reads = []
for line in f:
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

while (n == 0 or lep != len(reads)):
    primer = reads[random.randrange(0, len(reads))]
    contig = primer
    print(contig[1])
    lep = len(reads)
    for read in reads:
        if read != primer:
            res = check(k, read, contig)
            if len(res) > 1:
                contig = res[::-1]
                #print(contig)
                ass = contig[0]
                if ass.find(read[0]) != 0:
                     ass = ass.split()
                     print(ass[-2], ass[-1])
                else:
                    ass = ass.split()
                    print(ass[1], ass[0])
            else:
                singles.append(read)
    reads = singles
    singles = []
print(contig[1])
		
	
		
