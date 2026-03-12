quantidade_salas = int(input("Digite a quantidade de salas: "))

ingressos_por_sala = [0] * quantidade_salas

for i in range(quantidade_salas):
    ingressos = int(input(f"Digite a quantidade de ingressos vendidos na sala {i + 1}: "))
    ingressos_por_sala[i] = ingressos

print("\nIngressos vendidos por sala:")
for i in range(quantidade_salas):
    print(f"Sala {i + 1}: {ingressos_por_sala[i]} ingressos")

total_vendas = sum(ingressos_por_sala)
print(f"\nTotal de ingressos vendidos: {total_vendas}")