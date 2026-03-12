def comparar_listas(lista_og, lista_mod):
    set_inicial = set(lista_og)
    set_alterada = set(lista_mod)
   
    nao_mudaram = set_inicial & set_alterada
    novos_elementos = set_alterada - set_inicial
    elementos_removidos = set_inicial - set_alterada
   
    print("Lista Original:", set_inicial)
    print("Lista Modificada:", set_alterada)
    print("Elementos que não mudaram:", nao_mudaram)
    print("Novos elementos:", novos_elementos)
    print("Elementos removidos:", elementos_removidos)


lista_og = [1, 2, 3, 4, 5, 6]
lista_mod = [1, 3, 6, 7, 8, 9]

comparar_listas(lista_og, lista_mod)
