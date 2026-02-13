import secrets
import json
import os
import cofre

ARQUIVO = "contas.json"


def carregarcontas():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def salvarcontas(contas):
    with open(ARQUIVO, "w") as f:
        json.dump(contas, f, indent=4)


contas = carregarcontas()
usuariologado = None

while True:
    print("\n===== GERADOR E COFRE =====")
    print("1 - Criar Conta")
    print("2 - Entrar na conta")
    print("3 - Gerar Token")
    print("4 - Abrir Cofre")
    print("0 - Sair")
    print("___________________________")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        nome = input("Escolha seu nome de usuario: ")
        gmail = input("Coloque seu Gmail: ")
        senha = input("Digite sua senha: ")


        for conta in contas:
            if conta["nome"] == nome:
                print("Usuário já existe!")
                break
        else:
            novaconta = {
                "nome": nome,
                "gmail": gmail,
                "senha": senha,
                "tokens": []
            }

            contas.append(novaconta)
            salvarcontas(contas)
            print("Conta criada com sucesso!")


    elif opcao == "2":
        nome = input("Nome: ")
        senha = input("Senha: ")

        for conta in contas:
            if conta["nome"] == nome and conta["senha"] == senha:
                usuariologado = conta
                print("Login realizado com sucesso!")
                break
        else:
            print("Usuário ou senha incorretos!")


    elif opcao == "3":
        if usuariologado:
            token = secrets.token_urlsafe(8)
            usuariologado["tokens"].append(token)
            salvarcontas(contas)
            print("Token gerado:", token)
        else:
            print("Faça login primeiro!")


    elif opcao == "4":
        if usuariologado:
            senha_confirm = input("Digite sua senha para abrir o cofre: ")

            if senha_confirm == usuariologado["senha"]:
                cofre.abrir_cofre(usuariologado)
            else:
                print("Senha incorreta!")
        else:
            print("Faça login primeiro!")


    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
