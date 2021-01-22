import string
fhand = open('mbox-short.txt')
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        if words[1] not in counts:
            counts[words[1]] = 1
        else:
            counts[words[1]] += 1

# Sort the dictionary by value
lst=list()
for key,val in list(counts.items()):
    lst.append((val,key))
lst.sort(reverse=True)
key,val=lst[0]
print(val,key)    
