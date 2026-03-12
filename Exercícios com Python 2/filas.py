fila1 = []
fila2 = []
ultimo = 0

while True:
    print(f"\nFila 1: {fila1}")
    print(f"Fila 2: {fila2}")
    print("Digite F para adicionar cliente à fila 1")
    print("Digite G para adicionar cliente à fila 2")
    print("Digite A para atender cliente da fila 1")
    print("Digite B para atender cliente da fila 2")
    print("Digite S para sair")
    
    operacao = input("Operação: ").strip().upper()
    
    if operacao == 'F':
        ultimo += 1
        fila1.append(ultimo)
        print(f"Cliente {ultimo} adicionado à fila 1.")
    elif operacao == 'G':
        ultimo += 1
        fila2.append(ultimo)
        print(f"Cliente {ultimo} adicionado à fila 2.")
    elif operacao == 'A':
        if fila1:
            atendido = fila1.pop(0)
            print(f"Cliente {atendido} atendido da fila 1.")
        else:
            print("Fila 1 vazia! Nenhum cliente para atender.")
    elif operacao == 'B':
        if fila2:
            atendido = fila2.pop(0)
            print(f"Cliente {atendido} atendido da fila 2.")
        else:
            print("Fila 2 vazia! Nenhum cliente para atender.")
    elif operacao == 'S':
        print("Saindo...")
        break
    else:
        print("Operação inválida! Tente novamente.")