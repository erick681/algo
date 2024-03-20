def quicksort(arr):
    if len(arr) < 2 :
        return arr
    else:
        p = arr[0]
        menor = [i for i in arr[1:] if i <= p]
        maior = [i for i in arr[1:] if i > p]
        return quicksort(menor)+[p]+quicksort(maior)
    print(quicksort(arr))
print(quicksort([1,5,4,7,8,9,4,4,3,2,90,1,6,2,9,5,7,3,12,34,21]))
