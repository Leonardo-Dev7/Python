estoque = {
    "Mochila": 100,
    "Estojo": 90,
    "Garrafa": 57,
    "Caderno": 80
}

def vendas():
    while True:
        produto = input("Nome do Produto (ou 'sair' para finalizar): ").title()
       
        if produto == "Sair":
            print("Finalizando o sistema de vendas...")
            break
       
        if produto in estoque:
            quantidade = int(input("Quantidade de Produtos Vendidos: "))
           
            if quantidade <= estoque[produto]:
                estoque[produto] -= quantidade
                print(f"Venda efetuada com sucesso. Estoque atual de {produto}: {estoque[produto]}")
            else:
                print("Não há quantidade suficiente no estoque.")
        else:
            print("Produto não encontrado no estoque.")

vendas()
