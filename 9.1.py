fhand=open('words.txt')
diction=dict()
count=0
for line in fhand:
    line=line.rstrip()
    words=line.split()
    for w in words:
        diction[w]=count
        count=count+1
print(diction)        