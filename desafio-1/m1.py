def verificar_aprovacao(nota):
    if nota >= 6:
        return "Aluno aprovado!"
    else:
        return "Aluno reprovado."
        
nota = float(input("Digite a nota do aluno: "))
print(verificar_aprovacao(nota))