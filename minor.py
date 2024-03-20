import time 

def p(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1,len(arr)):
        if arr[i] < menor :
            menor = arr[i]
            menor_indice = i
    return menor

def ordenação(arr):
    narr= []
    arrcopy = arr[:]
    for i in range(len(arrcopy)):
        menor = p(arrcopy)
        narr.append(arrcopy.pop(arrcopy.index(menor)))
    return narr
i = time.time()
fim = time.time()

r = ordenação([1,2,3,4,5,6,7,8,-1])
print(r)
print(f"tempo executado  {round((fim-i)*1000,3)} : milisegundos ")
