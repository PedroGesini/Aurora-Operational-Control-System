from tabulate import tabulate

def mostrar_modulos(banc):
    print("\nHISTÓRICO DE MÓDULOS DESLIGADOS\n")

    modulos = banc["modulos"]
    tabela_modulos = []

    for nome, status in modulos.items():
        if not status == 1:
            situacao = "DESLIGADO"
        else:
            situacao = "LIGADO"

        tabela_modulos.append([
            nome,
            situacao
        ])

    print(tabulate(
        tabela_modulos,
        headers=["MODULO", "STATUS"],
        tablefmt="fancy_grid"
    ))
