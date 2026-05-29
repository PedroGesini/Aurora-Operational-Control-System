from tabulate import tabulate


def prever_energia_eolica(historico_vento, historico_energia, vento_atual):
    quantidade = len(historico_vento)

    soma_x = sum(historico_vento)
    soma_y = sum(historico_energia)

    soma_xy = 0
    soma_x2 = 0

    for i in range(quantidade):
        soma_xy += historico_vento[i] * historico_energia[i]
        soma_x2 += historico_vento[i] ** 2

    a = ((quantidade * soma_xy) - (soma_x * soma_y)) / (
        (quantidade * soma_x2) - (soma_x ** 2)
    )

    b = (soma_y - (a * soma_x)) / quantidade

    previsao = (a * vento_atual) + b

    return previsao, a, b


def prever_energia(banc):
    print("\nPREVISÃO DE ENERGIA GERADA\n")

    historico_vento = banc["ambiente"]["vento"]
    historico_energia = banc["energia"]["geracao_solar"]
    vento_atual = banc["ambiente"]["vento"][-1]

    previsao, a, b = prever_energia_eolica(
        historico_vento,
        historico_energia,
        vento_atual
    )

    tabela = []

    for i in range(len(historico_vento)):
        tabela.append([
            i + 1,
            historico_vento[i],
            historico_energia[i]
        ])

    print(tabulate(
        tabela,
        headers=["REGISTRO", "VENTO KM/H", "ENERGIA GERADA KW"],
        tablefmt="fancy_grid"
    ))

    tabela_previsao = [
        ["Vento atual", f"{vento_atual} km/h"],
        ["Coeficiente A", f"{a:.2f}"],
        ["Coeficiente B", f"{b:.2f}"],
        ["Previsão de energia", f"{previsao:.2f} kW"]
    ]

    print("\nRESULTADO DA REGRESSÃO\n")

    print(tabulate(
        tabela_previsao,
        headers=["DADO", "VALOR"],
        tablefmt="fancy_grid"
    ))

    if previsao < 30:
        print("\nPrevisão: geração de energia BAIXA")
    else:
        print("\nPrevisão: geração de energia ESTÁVEL")