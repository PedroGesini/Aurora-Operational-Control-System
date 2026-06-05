from tabulate import tabulate

def verificar_consumo(banc):
    print("\nINICIANDO VERIFICAÇÃO DA COLONIA\n")

    geracao = banc["energia"]["geracao_solar"]
    consumo = banc["energia"]["consumo"]
    bateria = banc["energia"]["bateria"]

    tabela = []

    for i in range(len(geracao)):
        if consumo[i] > geracao[i] and bateria[i] < 40:
            status = "CRÍTICO MAX"
        elif consumo[i] > geracao[i] or bateria[i] <= 60:
            status = "CRÍTICO"
        else:
            status = "ESTÁVEL"

        tabela.append([
            i + 1,
            geracao[i],
            consumo[i],
            bateria[i],
            status
        ])

    print(tabulate(
        tabela,
        headers=["MINUTO", "GERAÇÃO SOLAR", "CONSUMO", "BATERIA %", "STATUS"],
        tablefmt="fancy_grid"
    ))
