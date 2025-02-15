def pode_votar(idade):
    if idade >= 16:
        return "Você pode votar!"
    else:
        return "Você não pode votar."
        
idade = int(input("Digite sua idade: "))
print(pode_votar(idade))