from tabulate import tabulate
def logeventos(banc):
                        
            print("\nEVENTOS RECENTES\n")

            tabela_relatorio = []

            for nome, status in banc["modulos"].items():

                if status == 1:
                    situacao = "LIGADO"
                else:
                    situacao = "DESLIGADO"

                tabela_relatorio.append([
                    nome,
                    situacao
                ])
            print(tabulate(
                tabela_relatorio,
                headers=["MODULO", "STATUS"],
                tablefmt="fancy_grid"
            ))

            ambiente = [
                ["Temperatura Atual", f"{banc['ambiente']['temperatura'][-1]} °C"],
                ["Radiação Atual", banc['ambiente']['radiacao'][-1]],
                ["Qualidade do Sinal", banc['ambiente']['qualidade_sinal']],
                ["Velocidade do Vento", f"{banc['ambiente']['vento'][-1]} km/h"]
            ]

            print("\nDADOS AMBIENTAIS\n")

            print(tabulate(
                ambiente,
                headers=["DADO", "VALOR"],
                tablefmt="fancy_grid"
            ))

            eventos = []

            for evento in banc["eventos"]:
                eventos.append([evento])

            print("\nEVENTOS RECENTES\n")

            print(tabulate(
                eventos,
                headers=["EVENTOS"],
                tablefmt="fancy_grid"
            ))
            print("\n--- ANÁLISE ESTRUTURAL (FILA E PILHA) ---")
    
            evento_antigo = eventos.pop(0)
            print(f"Tratando o evento mais antigo da Fila: {evento_antigo[0]}")
    
            evento_recente = eventos.pop()
            print(f"Analisando o evento mais recente da Pilha: {evento_recente[0]}\n")
  
            return logeventos
