alunos = []

for i in range(10):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")
    frequencia = float(input("Frequência (%): "))
    nota = float(input("Nota: "))
   
    if nota > 5 and frequencia >= 75:
        status = "Aprovado"
    else:
        status = "Reprovado"
   
    aluno = {
        "Nome": nome,
        "Frequência (%)": frequencia,
        "Nota": nota,
        "Status": status
    }
    alunos.append(aluno)

print("\nResultado Final:")
print(f"{'Nome':<15} {'Frequência (%)':<15} {'Nota':<10} {'Status':<10}")
print("-" * 55)
for aluno in alunos:
    print(f"{aluno['Nome']:<15} {aluno['Frequência (%)']:<15.1f} {aluno['Nota']:<10.1f} {aluno['Status']:<10}")
