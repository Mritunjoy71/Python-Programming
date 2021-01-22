numlist=list()
while True:
    inp=input('enter a number>')
    if inp=='done':
        break
    try:
        num=float(inp)
        numlist.append(num)
    except:
        print('bad input') 
average=sum(numlist)/len(numlist)
print(average)