def roubar_melhor_combinacao_itens(items, limite_peso):
    n = len(items)
    # Inicializando uma matriz para armazenar os valores máximos alcançados
    # para diferentes capacidades de peso e diferentes números de itens.
    # Cada célula dp[i][j] representa o valor máximo alcançado com os primeiros i itens
    # e a capacidade de peso j.
    dp = [[0] * (limite_peso + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, limite_peso + 1):
            # Se o peso do item for menor ou igual à capacidade de peso atual
            if items[i - 1][2] <= j:
                # Verificando se é benéfico adicionar o item atual
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][2]] + items[i - 1][1])
            else:
                # Se o peso do item for maior que a capacidade de peso atual
                # então não podemos adicionar o item na mochila
                dp[i][j] = dp[i - 1][j]

    # Reconstruindo a combinação de itens selecionados
    combinacao_itens = []
    i, j = n, limite_peso
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            combinacao_itens.append(items[i - 1])
            j -= items[i - 1][2]
        i -= 1

    return combinacao_itens

# Definindo os itens
items = [("violao", 1500, 6), ("notebook", 2000, 9), ("radio", 3000, 13)]
limite_peso = 16

# Chamando a função para calcular a melhor combinação de itens
melhor_combinacao = roubar_melhor_combinacao_itens(items, limite_peso)

# Imprimindo a melhor combinação de itens
print("Melhor combinação de itens para roubar:")
for item in melhor_combinacao:
    print(f"{item[0]} - R${item[1]} - {item[2]}kg")
def roubar_melhor_combinacao_itens(items, limite_peso):
    n = len(items)
    # Inicializando uma matriz para armazenar os valores máximos alcançados
    # para diferentes capacidades de peso e diferentes números de itens.
    # Cada célula dp[i][j] representa o valor máximo alcançado com os primeiros i itens
    # e a capacidade de peso j.
    dp = [[0] * (limite_peso + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, limite_peso + 1):
            # Se o peso do item for menor ou igual à capacidade de peso atual
            if items[i - 1][2] <= j:
                # Verificando se é benéfico adicionar o item atual
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][2]] + items[i - 1][1])
            else:
                # Se o peso do item for maior que a capacidade de peso atual
                # então não podemos adicionar o item na mochila
                dp[i][j] = dp[i - 1][j]

    # Reconstruindo a combinação de itens selecionados
    combinacao_itens = []
    i, j = n, limite_peso
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            combinacao_itens.append(items[i - 1])
            j -= items[i - 1][2]
        i -= 1

    return combinacao_itens

# Definindo os itens
items = [("violao", 1500, 6), ("notebook", 2000, 9), ("radio", 3000, 13)]
limite_peso = 16

# Chamando a função para calcular a melhor combinação de itens
melhor_combinacao = roubar_melhor_combinacao_itens(items, limite_peso)

# Imprimindo a melhor combinação de itens
print("Melhor combinação de itens para roubar:")
for item in melhor_combinacao:
    print(f"{item[0]} - R${item[1]} - {item[2]}kg")
def roubar_melhor_combinacao_itens(items, limite_peso):
    n = len(items)
    # Inicializando uma matriz para armazenar os valores máximos alcançados
    # para diferentes capacidades de peso e diferentes números de itens.
    # Cada célula dp[i][j] representa o valor máximo alcançado com os primeiros i itens
    # e a capacidade de peso j.
    dp = [[0] * (limite_peso + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, limite_peso + 1):
            # Se o peso do item for menor ou igual à capacidade de peso atual
            if items[i - 1][2] <= j:
                # Verificando se é benéfico adicionar o item atual
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][2]] + items[i - 1][1])
            else:
                # Se o peso do item for maior que a capacidade de peso atual
                # então não podemos adicionar o item na mochila
                dp[i][j] = dp[i - 1][j]

    # Reconstruindo a combinação de itens selecionados
    combinacao_itens = []
    i, j = n, limite_peso
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            combinacao_itens.append(items[i - 1])
            j -= items[i - 1][2]
        i -= 1

    return combinacao_itens

# Definindo os itens
items = [("violao", 1500, 6), ("notebook", 2000, 9), ("radio", 3000, 13)]
limite_peso = 16

# Chamando a função para calcular a melhor combinação de itens
melhor_combinacao = roubar_melhor_combinacao_itens(items, limite_peso)

# Imprimindo a melhor combinação de itens
print("Melhor combinação de itens para roubar:")
for item in melhor_combinacao:
    print(f"{item[0]} - R${item[1]} - {item[2]}kg")
def roubar_melhor_combinacao_itens(items, limite_peso):
    n = len(items)
    # Inicializando uma matriz para armazenar os valores máximos alcançados
    # para diferentes capacidades de peso e diferentes números de itens.
    # Cada célula dp[i][j] representa o valor máximo alcançado com os primeiros i itens
    # e a capacidade de peso j.
    dp = [[0] * (limite_peso + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, limite_peso + 1):
            # Se o peso do item for menor ou igual à capacidade de peso atual
            if items[i - 1][2] <= j:
                # Verificando se é benéfico adicionar o item atual
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i - 1][2]] + items[i - 1][1])
            else:
                # Se o peso do item for maior que a capacidade de peso atual
                # então não podemos adicionar o item na mochila
                dp[i][j] = dp[i - 1][j]

    # Reconstruindo a combinação de itens selecionados
    combinacao_itens = []
    i, j = n, limite_peso
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            combinacao_itens.append(items[i - 1])
            j -= items[i - 1][2]
        i -= 1

    return combinacao_itens

# Definindo os itens
items = [("violao", 1500, 6), ("notebook", 2000, 9), ("radio", 3000, 13)]
limite_peso = 16

# Chamando a função para calcular a melhor combinação de itens
melhor_combinacao = roubar_melhor_combinacao_itens(items, limite_peso)

# Imprimindo a melhor combinação de itens
print("Melhor combinação de itens para roubar:")
for item in melhor_combinacao:
    print(f"{item[0]} - R${item[1]} - {item[2]}kg")

