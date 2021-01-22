total=0
count=0
avg=0
while True:
    inp=input('enter your number: ')
    if inp =='done':
        print('total: ',total)
        print('count: ',count)
        if count!=0:
            avg=total/count
        print('avg: ',avg)
        break
    try:   
        number=float(inp)
        total=total+number
        count=count+1
    except:
        print('bad input.enter a number or write done')

print('done')

    