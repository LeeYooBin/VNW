def verificar_senha(senha):
    if senha == "Python123":
        return "Acesso permitido!"
    else:
        return "Senha incorreta."
        
senha = input("Digite a senha: ")
print(verificar_senha(senha))