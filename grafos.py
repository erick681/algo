grafo = {}
grafo["voce"] = ["alice","bob","claire"]
grafo["inicio"] = {} 
grafo["inicio"]["a"] = 6 
grafo["inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1 
grafo["b"]={}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5 
grafo["fim"] = {}
infinito = float("inf") 
custos = {}
custos["a"] = 6 
custos["b"] = 2 
custos["fim"] = infinito   
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None
processado = []

node = acb(custos)
while node is not None:
    custo = custos[node]
    vizinhos = grafo[node]
    for n in vizihos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = node 
        processados.append(node)
        node = acb(custos) 


