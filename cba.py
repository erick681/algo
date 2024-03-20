def l(arr):
    max_ = arr[0]
    nl = []
    for i in range(1,len(arr)):
        c = arr[i]
        if c > max_:
            max_ = c
            nl.append(max)
            print(max_)
    return max_
a = l([1,2,3,4,5])
print(a)
