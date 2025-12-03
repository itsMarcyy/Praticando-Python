'''
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.

'''

while True:
    usuario = input("Insira um usuário com no mínimo 5 caracteres: ")
    senha = input("Insira uma senha com no mínimo 8 caracteres: ")

    if len(usuario) < 5:
        print("Usuário inválido, mínimo de 5 caracteres.")
        continue

    if len(senha) < 8:
        print("Senha inválida, mínimo de 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break
