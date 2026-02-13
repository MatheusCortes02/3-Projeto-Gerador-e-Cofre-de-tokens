def abrir_cofre(usuario):
    while True:
        print("\n===== COFRE =====")
        print("1 - Ver Tokens")
        print("2 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            if usuario["tokens"]:
                print("\nSeus tokens:")
                for t in usuario["tokens"]:
                    print("-", t)
            else:
                print("Nenhum token gerado ainda!")

        elif opcao == "2":
            break

        else:
            print("Opção inválida!")