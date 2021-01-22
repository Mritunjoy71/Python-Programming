file=open('romeo.txt')
t=list()
for line in file:
    words=line.split()
    for w in words:
        if not t.__contains__(w):
            t.append(w)
t.sort()
print(t)    

