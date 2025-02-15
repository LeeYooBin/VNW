def contar_letras(nome):
    return f"O nome {nome} tem {len(nome)} letras."

nome = input("Digite um nme: ")
print(contar_letras(nome))