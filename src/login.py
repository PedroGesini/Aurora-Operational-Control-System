def login():
    while True:

        insertname = input("insira seu nome para acessar o sistema:\n")
        print(f"seja bem vindo {insertname}")

        password = input(
            "para acessar o sistema operacional Aurora insira a senha de acesso:"
        )

        if password == "FIAP":
            print("------------------------------")
            print("|Login realizado com sucesso!|")
            print("------------------------------")

            return insertname

        else:
            print("---------------")
            print("|ACESSO NEGADO|")
            print("---------------")