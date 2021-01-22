import string
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    line=line.strip()
    line=line.lower()
    l=len(line)
    if l > 0 :
        for i in range(l):
            if line[i]>='a' and line[i]<='z':
                if line[i] not in counts:
                    counts[line[i]]=1
                else:
                    counts[line[i]]+=1



# Sort the dictionary by value
lst=list()
for key,val in list(counts.items()):
    lst.append((key,val))
lst.sort()
for key,val in lst:
    print(key,val)