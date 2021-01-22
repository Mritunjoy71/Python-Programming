import re
fhand = open('mbox-short.txt')
sum=0
count=0
for line in fhand:
    line = line.rstrip()
    x=re.findall('New .+: ([0-9]+)', line)
    if len(x)>0:
        count+=1
        sum+=float(x[0])        
avg=int(sum/count)
print(avg)