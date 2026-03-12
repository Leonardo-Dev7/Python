precos = {
    1: 0.50,
    2: 1.00,
    3: 4.00,
    4: 7.00,
    5: 8.00
}

total = 0.0

print("Bem-vindo!")
print("Digite o código do produto e a quantidade.")
print("Digite 0 como código para finalizar a compra.\n")

while True:
    try:
        codigo = int(input("Código do produto: "))
        if codigo == 0:
            break
        if codigo in precos:
            quantidade = int(input("Quantidade: "))
            if quantidade < 0:
                print("Quantidade inválida. Tente novamente.")
                continue
            total += precos[codigo] * quantidade
        else:
            print("Código inválido.")
    except ValueError:
        print("Entrada inválida. Digite números inteiros.")

print(f"\nTotal da compra: R$ {total:.2f}")