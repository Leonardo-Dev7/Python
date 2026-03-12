# média, moda e mediana

import statistics

# Lista de salários (valores repetidos permitidos)
salario = [5800, 7250, 9322, 5800, 7250]

# Média
media = statistics.mean(salario)
print("Médio: ", media)

# Mediana
mediana = statistics.median(salario)
print("Mediana: ", mediana)

# Moda (usando multimode para trazer mais de um valor, se houver empate)
moda = statistics.multimode(salario)
print("Moda: ", moda)
