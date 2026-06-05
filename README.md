# Sistema Operacional Aurora – Monitoramento Energético da Colônia Espacial
Sistema inteligente de monitoramento espacial desenvolvido em Python para análise de telemetria, identificação de situações críticas, geração de alertas automáticos e previsão energética, auxiliando a segurança operacional e a tomada de decisões em missões espaciais experimentais.

## Integrantes da Equipe

Eduardo Ventura Rocha Soares	RM 570795

Diego Ramos dos Santos	RM 570889

José Rodrigues da Silva Júnior  RM 572300

Pedro Ribeiro Gesini  RM 469421

Heitor Assis Duenhas  RM 570472

## Resumo do Problema e Cenário Analisado

As missões espaciais modernas dependem de sistemas inteligentes capazes de monitorar continuamente equipamentos, recursos e condições ambientais para garantir a segurança da operação e a sobrevivência da tripulação. Em ambientes remotos, os dados gerados pelos sensores e módulos da missão tornam-se a principal fonte de informação para a tomada de decisões.

Neste contexto, foi desenvolvido o Sistema Operacional Aurora, um sistema inteligente de monitoramento para uma colônia espacial experimental. A solução recebe e interpreta dados operacionais armazenados em um banco de dados JSON, analisando informações sobre geração e consumo de energia, nível das baterias, condições ambientais, status dos módulos da base e eventos registrados durante a operação.

O sistema foi projetado para identificar situações críticas, emitir alertas automáticos e fornecer informações que auxiliem os operadores na tomada de decisões. Além disso, utiliza uma técnica de regressão linear para realizar previsões de geração energética com base em dados históricos, permitindo antecipar possíveis problemas relacionados ao abastecimento de energia.

O sistema utiliza dados armazenados em um arquivo JSON que simulam informações reais da colônia, incluindo:

- Estado dos módulos operacionais;
- Produção e consumo de energia;
- Nível das baterias;
- Temperatura e radiação ambiente;
- Histórico de eventos críticos.

O objetivo é fornecer diagnósticos rápidos que dão suporte na tomada de decisão e aumentem a segurança da missão.

## Estrutura de dados utilizada
### Dicionários

Foram utilizados para armazenar informações organizadas em categorias:

banc["energia"]

banc["ambiente"]

banc["modulos"]

Motivo:

- Permitem acesso rápido aos dados.
- Organizam informações por contexto.
- Facilitam manutenção e expansão do sistema.

### Listas

Utilizadas para armazenar históricos de dados:

"geracao_solar": [40, 38, 35, 30, 28, 22]

Motivo:

- Permitem análise temporal.
- Facilitam cálculos estatísticos.
- Servem como base para a previsão de energia.

### Fila (Queue) e Pilha (Stack)

Utilizadas para gerenciamento e priorização de alertas e eventos.

Fila (.pop(0)): Aplica o conceito FIFO (First-In, First-Out) para garantir que os alertas mais antigos sejam analisados primeiro.

Pilha (.pop()): Aplica o conceito LIFO (Last-In, First-Out) para exibir o evento mais recente registrado na telemetria.

Motivo: 

- Fila (Queue): Garante que os alertas do sistema sejam processados na ordem cronológica exata em que ocorreram, impedindo que um problema antigo e não resolvido seja esquecido.
- Pilha (Stack): Permite o acesso imediato ao evento mais recente registrado pelos sensores, facilitando a análise rápida do contexto atual e imediato da missão.


### Arquivo JSON

Utilizado como banco de dados da aplicação.

Motivo:

- Fácil leitura e manutenção.
- Estrutura leve.
- Compatível com Python através da biblioteca json.

## Regras Lógicas Principais do Diagnóstico
### 1. Verificação de Consumo Energético

O sistema analisa o balanço de energia cruzando o consumo com a carga da bateria:
```python
if consumo > geracao and bateria < 40: → Status "CRÍTICO MAX"

elif consumo > geracao or bateria <= 60: → Status "CRÍTICO"

else: → Status "ESTÁVEL"
```

Expressão Booleana Principal do Diagnóstico:
```python
ALERTA_CRITICO_MAX = (Consumo > Geracao) AND (Bateria < 40)
```

Interpretação:

CRÍTICO MAX → Défice de energia aliado a um nível de bateria perigosamente baixo (< 40%). Risco iminente de apagão.

CRÍTICO → Consumo maior que a geração ou baterias começando a atingir níveis de atenção (<= 60%).

ESTÁVEL → Geração suficiente para atender o consumo e baterias operando em níveis seguros.

### 2. Diagnóstico de Módulos
O sistema verifica as falhas operacionais invertendo a lógica de validação:
```python
if not status == 1: 
     → Situação "DESLIGADO"

else: 
     → Situação "LIGADO"
```

Interpretação:

0 = módulo desligado.

1 = módulo operacional.

### 3. Monitoramento Ambiental
O sistema exibe:

- Temperatura atual;
- Nível de radiação;
- Qualidade do sinal;
- Velocidade do vento.

Esses dados ajudam na avaliação das condições externas da colônia.

## Técnica de previsão utilizada e resultado
### Método utilizado
Foi aplicada uma técnica de Regressão Linear Simples.

A regressão relaciona:

- Velocidade do vento (variável independente);
- Energia gerada (variável dependente).

Modelo matemático:

y = ax + b

Os coeficientes são calculados pelas fórmulas:

- a = ((n × Σxy) − (Σx × Σy)) / ((n × Σx²) − (Σx)²)

- b = (Σy − a × Σx) / n

Após calcular os coeficientes, a previsão é obtida por:

- Previsão = (a × vento_atual) + b

Onde:

- y = energia prevista;
- x = velocidade do vento;
- a = coeficiente angular;
- b = coeficiente linear.

### Resultados obtidos
Com os dados fornecidos:

Vento Atual =	28 km/h

Energia Prevista = Aproximadamente 22 kW

O sistema classifica:

- Menor que 30 kW → Geração Baixa
- Maior ou igual a 30 kW → Geração Estável

No cenário analisado, a previsão indica risco de baixa geração energética.

### Como Executar
- Instalar Dependências
  ```python
  - pip install tabulate
  ```
  
- Executar o Sistema
  ```python
  - python sistema.py
  ```

## Exemplo de Entrada e Saída
### Entrada

Login:

Nome: Eduardo

Senha: FIAP

Escolha da opção:

1 - VERIFICAÇÃO DO CONSUMO DA COLONIA

### Saída

| MINUTO | GERAÇÃO SOLAR (kW) | CONSUMO (kW) | BATERIA (%) | STATUS |
|---------|-------------------|-------------|-------------|---------|
| 1 | 40 | 45 | 90 | CRÍTICO |
| 2 | 38 | 50 | 82 | CRÍTICO |
| 3 | 35 | 58 | 74 | CRÍTICO |
| 4 | 30 | 65 | 60 | CRÍTICO |
| 5 | 28 | 70 | 48 | CRÍTICO |
| 6 | 22 | 78 | 32 | CRÍTICO MAX |

Recomendações Geradas pelo Sistema

Com base nos diagnósticos apresentados, recomenda-se:

### Energia
- Reduzir o consumo dos módulos não essenciais.
- Priorizar sistemas de suporte à vida.
- Monitorar constantemente o nível das baterias.
- Expandir a geração energética através de fontes complementares.
### Comunicação
- Investigar falhas recorrentes de comunicação.
- Verificar antenas e repetidores.
### Radiação
- Restringir atividades externas durante períodos críticos.
- Reforçar protocolos de proteção dos astronautas.
### Módulos

Os módulos identificados como desligados devem passar por inspeção técnica para verificar:

- Falhas elétricas;
- Problemas de comunicação;
- Necessidade de manutenção preventiva.

## Conclusão
O desenvolvimento do Sistema Operacional Aurora permitiu aplicar conceitos fundamentais de programação em Python, manipulação de arquivos JSON, estruturas de dados, criação de código e análise de dados.

Além disso, foi possível usar uma técnica simples de Inteligência Artificial baseada em regressão linear para realizar previsões energéticas, simulando situações reais enfrentadas em missões espaciais.

O projeto demonstra como sistemas computacionais podem ajudar no monitoramento de recursos críticos, aumentando a segurança, eficiência e sustentabilidade de futuras colônias espaciais.

Como aprendizado principal, destaca-se a importância da análise de dados para apoiar decisões operacionais e prevenir falhas em ambientes de alta complexidade, como bases espaciais autônomas.
