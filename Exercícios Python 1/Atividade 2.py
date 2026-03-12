def comparar(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
   
    comum = list(set1.intersection(set2))
    l1_comuns = list(set1.difference(set2))
    l2_comuns = list(set2.difference(set1))
    nao_repetidos = list(set1.symmetric_difference(set2))
    l1_sem_repetidos = list(set1.difference(set1.intersection(set2)))

    print("Valores em comum nas duas listas:", comum)
    print("Valores que só têm na lista 1:", l1_comuns)
    print("Valores que só têm na lista 2:", l2_comuns)
    print("Lista com os elementos não repetidos nas duas listas:", nao_repetidos)
    print("Primeira lista sem os valores repetidos na segunda:", l1_sem_repetidos)


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

comparar(list1, list2)
