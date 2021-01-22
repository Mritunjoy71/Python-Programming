t=list()
while True:
    inp=input('enter a number>')
    if inp=='done':
        break
    try:
        num=float(inp)
        t.append(num)
    except:
        print('bad input')    
print('maximum %f minimum %f' %(max(t),min(t)))       