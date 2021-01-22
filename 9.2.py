import string

try:
    fhand=open('mbox-short.txt')
except:
    print('can not open the file' )

diction=dict()
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        w=words[1].split('@')
        w1=w[1]
        if w1 not in diction: 
            diction[w1]=1
        else:
            diction[w1]+=1
print(diction)