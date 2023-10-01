
listacesso = ['S7']
senha = '@senha12345#'

espaco = 70* '.'

while True:
    
    nomeacesso = str(input("Digite seu nome de usuario:"))
    
    if nomeacesso in listacesso:
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
            
            if dsenha == senha:
                usuarionovo = input("Digite um novo usuario:")
                listacesso = listacesso + [usuarionovo]
                print('Usuario Criado com sucesso!')
                print(espaco)
            else:
                print("Senha invalida!")
                print(espaco)
        else:
            print("Tente acessar novamente")
            print(espaco)