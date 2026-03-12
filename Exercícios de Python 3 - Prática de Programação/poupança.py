dep_inicial = (float(input("Deposito Incial: ")))
juros = (float(input("Taxa de Juros da Poupança: ")))
valor_mensal = (float(input("Valor depositado: ")))

meses = 1
saldo = dep_inicial

while meses <= 24:
    saldo = saldo * (1 + (juros / 100)) + valor_mensal
    print(f"mes: {meses}  valor: {saldo:.2f}")
    meses += 1

ganho = saldo - dep_inicial
print(f"\nTotal ganho com juros após 24 meses: R$ {ganho:.2f}")