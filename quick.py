def quicksort(arr,left,right):
    if left < right :
        pi = partition(arr,left,right)
        quicksort(arr,left,pi-1)
        quicksort(arr,pi+1,right)
def partition(arr,left,right):
    pivot = arr[right]
    i = left-1 
    for j in range(left,right):
        if arr[j] <= pivot:
            i = i+1 
            arr[j],arr[i] = arr[i],arr[j]
    arr[i+1],arr[right] = arr[right],arr[i+1]
    return i + 1 
a = [1,4,3,7,6,8,4,9]
quicksort(a,0,len(a)-1)
print(a)

