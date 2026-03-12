litros = float(input("Digite o número de litros: "))
tipo = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

preco_alcool = 1.90
preco_gasolina = 2.50

if tipo == 'A':
    if litros <= 20:
        desconto = 3
    else:
        desconto = 5
    preco = preco_alcool
else: # tipo == 'G'
    if litros <= 20:
        desconto = 4
    else:
        desconto = 6
    preco = preco_gasolina

valor_sem_desconto = litros * preco
valor_do_desconto = valor_sem_desconto * (desconto / 100)
valor_a_pagar = valor_sem_desconto - valor_do_desconto

print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")