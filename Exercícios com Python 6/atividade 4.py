meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

temperaturas = []

for i in range(12):
    temp = float(input(f"Digite a temperatura média de {meses[i]}: "))
    temperaturas.append(temp)

print("\nTemperaturas médias mensais:")
print("-" * 35)
print(f"{'Mês':<15}{'Temperatura (°C)':>20}")
print("-" * 35)
for i in range(12):
    print(f"{meses[i]:<15}{temperaturas[i]:>20.2f}")

menor_temp = min(temperaturas)
maior_temp = max(temperaturas)
media_anual = sum(temperaturas) / len(temperaturas)
meses_abaixo_media = sum(1 for temp in temperaturas if temp < media_anual)

print("\nInformações:")
print(f"a) Menor temperatura do ano: {menor_temp:.2f} °C")
print(f"b) Maior temperatura do ano: {maior_temp:.2f} °C")
print(f"c) Temperatura média anual: {media_anual:.2f} °C")
print(f"d) Número de meses com temperatura abaixo da média anual: {meses_abaixo_media}")
