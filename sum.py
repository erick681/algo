def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else :
        return arr[0] + sum(arr[1:])
n = sum([1,2,3,4])
print(n)
