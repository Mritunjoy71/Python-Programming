import string
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        w=words[5]
        ww=w.split(':')
        www=ww[0]
        if www not in counts:
            counts[www] = 1
        else:
            counts[www] += 1

# Sort the dictionary by value
lst=list()
for key,val in list(counts.items()):
    lst.append((key,val))
lst.sort()
for key,val in lst:
    print(key,val)
  
