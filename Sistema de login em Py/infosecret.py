listacesso = ['S7']
listsenha = ['12345']
senhareset = '@senha12345#'
espaco = 70* '.'

while True:
    
    nomeacesso = str(input("Digite seu nome de usuario:"))
    senhacesso = str(input("Digite sua senha:"))
    
    if nomeacesso in listacesso and senhacesso in listsenha:
        print("Está é a informação secreta!")
        print(espaco)
        break
    
    else:
        print("Usuario desconhecido")
        print(espaco)
        createaccount = input("Você deseja criar um usuario? (S ou N)")
        
        if createaccount == "S" or createaccount == "s":
            dsenha = input("Digite a senha para criar sua conta:")
            print(espaco)
            
            if dsenha == senhareset:
                usuarionovo = input("Digite um novo usuario:")
                senhanova = input("Digite uma nova senha:")
                listacesso = listacesso + [usuarionovo]
                listsenha = listsenha + [senhanova]
                print('Usuario e Senha criado com sucesso!')
                print(espaco)
            else:
                print("Senha invalida!")
                print(espaco)
        else:
            print("Tente acessar novamente")
            print(espaco)
