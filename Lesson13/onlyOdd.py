def onlyOdd(l):
    newList = []
    for item in l:
        if item % 2 == 1:
            print(f'item is {item} and item % 2 is {item % 2}')
            newList.append(item)
    
    return newList

