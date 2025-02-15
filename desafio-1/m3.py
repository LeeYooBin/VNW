def classificar_nota(nota):
    if nota >= 90:
        return "Parabéns, você tirou A!"
    elif nota >= 80:
        return "Muito bem, você tirou B."
    elif nota >= 70:
        return "Bom trabalho, você tirou C."
    elif nota >= 60:
        return "Fique atento, você tirou D."
    else:
        return "Estude um pouco mais, você tirou F."
        
nota = float(input("Digite a nota do aluno: "))
print(classificar_nota(nota))