convidados = []

print("Digite o nome de 10 pessoas para a lista de convidados:")
for i in range(10):
    nome = input(f"Nome {i + 1}: ")
    convidados.append(nome.strip())

print("\nDigite os nomes que deseja verificar (ou 'sair' para encerrar):")
while True:
    nome_verificar = input("Verificar nome: ").strip()
   
    if nome_verificar.lower() == 'sair':
        print("Encerrando verificação.")
        break

    if nome_verificar in convidados:
        print("ESTÁ NA LISTA")
    else:
        print("NÃO ESTÁ NA LISTA")
