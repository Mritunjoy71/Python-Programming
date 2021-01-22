def min(values):
    largest=None
    print('Before: ',largest)
    for itervar in values:
        if largest is None or itervar > largest:
            largest=itervar
        print('Loop: ',itervar,largest)
    return largest


values=[3, 41, 12, 9, 74, 15]
largest=min(values)        
print('largest: ',largest)