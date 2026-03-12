valores = []

for i in range(10):
    numero = float(input(f"Digite o {i+1}º valor: "))
    valores.append(numero)

x = float(input("Digite o valor de x: "))

print("\nResultado da multiplicação dos valores por x:")
for i, valor in enumerate(valores):
    resultado = valor * x
    print(f"Valor {i+1}: {valor} * {x} = {resultado}")
