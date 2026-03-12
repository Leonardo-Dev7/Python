def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))

if primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

print(f"Os números primos antes de {numero} são:", end=" ")

for i in range(2, numero):
    if primo(i):
        print(i, end=" ")