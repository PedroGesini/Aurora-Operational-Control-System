import time
from tabulate import tabulate
from src.login import login
from src.logs_eventos import logeventos
from src.banco_dados_projeto import carregar_dados
from src.balanceamento_energetico import verificar_consumo
from src.regressao import prever_energia
from src.diagnostico import mostrar_modulos
# CARREGAR BANCO DE DADOS JSON
banc = carregar_dados()

# INTERFACE INICIAL DO PROGRAMA
print("iniciando sistema operacional da colonia...")
time.sleep(2)

insertname = login()

while True:     

    print(f"-----SEJA BEM-VINDO, {insertname}-----")

    print(f"""
    SISTEMA OPERACIONAL AURORA

    1 - VERIFICAÇÃO DO CONSUMO DA COLONIA
    2 - PREVISÃO DE ENERGIA GERADA
    3 - HISTORICO DE MODULOS DESLIGADOS
    4 - HISTORICO DA COLONIA
    5 - ENCERRAR SISTEMA
    """)

    # PROGRAMA PRINCIPAL
    try:
        opcao = int(input("DIGITE A OPÇÃO DESEJADA: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")
        continue

    match opcao:

        case 1:
            verificar_consumo(banc)
            input("\nPressione ENTER para voltar ao menu...")
        case 2:
           prever_energia(banc)
           input("\nPressione ENTER para voltar ao menu...")
        case 3:
            mostrar_modulos(banc)
            input("\nPressione ENTER para voltar ao menu...")
        case 4:
            logeventos(banc)
            input("\nPressione ENTER para voltar ao menu...")
        case 5:
            print("Encerrando o Sistema Operacional Aurora. Até logo!")
            break
        case _:
            print("Opção inválida.")
            input("\nPressione ENTER para voltar ao menu...")
