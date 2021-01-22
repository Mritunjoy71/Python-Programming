try:
    fhand=open('mbox-short.txt')
    count=0
    total=0
    for line in fhand:
        #line=line.rstrip()
        if line.find('X-DSPAM-Confidence:')!=-1:
            count=count+1
            line=line.split(':')
            total=total+float(line[1])
           # print(total)
    average=total/count 
    print('Average spam confidence %f' %average)  
    print(count)     
except:
    print('bad name')    