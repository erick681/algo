def b(items,l):
    l.sort()
    print(l,items)
    result = []
    for i in items :
        b = 0
        a = len(l) -1
        while b<=a:
            middle = (a+b)//2
            chute = l[middle]
            if chute == i :
                result.append(middle)
                break 
            if i < chute :
                a = middle -1
            else:
                b = middle + 1 
        else:
            result.append(None)
    return result
a = b([7,5],[1,2,3,4,7,8,5]) 
print(a)
    
