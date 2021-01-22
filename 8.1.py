fhand=open('mbox-short.txt')
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From '):
        continue
    word=line.split()
    if word[2]!=None:
        print(word[2])
