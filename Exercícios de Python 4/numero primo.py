numero = int(input("Digite um número: "))
primo = True

if numero <= 1:
    primo = False
    print(f" {numero} não é primo.")
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            print(f"{numero} não é primo. É divisível por {i}.")
            break

if primo:
    print(f"{numero} é primo.")