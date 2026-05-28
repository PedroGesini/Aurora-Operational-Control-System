def prever_energia_eolica(
        historico_vento,
        historico_energia,
        vento_atual
):

    quantidade = len(historico_vento)

    soma_x = sum(historico_vento)
    soma_y = sum(historico_energia)

    soma_xy = 0
    soma_x2 = 0

    for i in range(quantidade):

        soma_xy += (
            historico_vento[i]
            *
            historico_energia[i]
        )

        soma_x2 += (
            historico_vento[i] ** 2
        )

    a = (
        (
            quantidade * soma_xy
        )
        -
        (
            soma_x * soma_y
        )
    ) / (
        (
            quantidade * soma_x2
        )
        -
        (
            soma_x ** 2
        )
    )

    b = (
        soma_y
        -
        (
            a * soma_x
        )
    ) / quantidade

    previsao = (
        a * vento_atual
    ) + b

    return previsao