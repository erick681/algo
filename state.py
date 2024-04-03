def cobertura_conjuntos(conjuntos,elementos):
    elementos_nao_cobertos = set(elementos)
    conjuntos_selecionados = []
    while elementos_nao_cobertos:
        melhor_conjunto = None 
        maximo_cobertura = set()
        for conjunto in conjuntos:
            cobertura = conjunto.intersection(elementos_nao_cobertos) 
            if len(cobertura) > len(maximo_cobertura):
                melhor_conjunto = conjunto 
                melhor_cobertura = cobertura 
        conjuntos_selecionados.append(melhor_conjunto)
        elementos_nao_cobertos -= maximo_cobertura 

    return conjuntos_selecionados 

conjuntos = [{'CA', 'NV', 'UT'}, {'WA', 'ID', 'MT'}, {'OR', 'ID', 'NV'}, {'WA', 'MT', 'ID'}, {'OR', 'CA', 'NV'}]

elementos = ['WA', 'OR', 'ID', 'MT', 'NV', 'UT', 'CA']

conjuntos_selecionados = cobertura_conjuntos(conjuntos, elementos)
print("Conjuntos selecionados:", conjuntos_selecionados)                                
