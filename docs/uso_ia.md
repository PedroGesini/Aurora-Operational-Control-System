## Declaração de Uso de Inteligência Artificial

Em conformidade com as diretrizes da Global Solution, a equipe declara que utilizou ferramentas de Inteligência Artificial Generativa (LLMs) como apoio educacional e de estruturação durante o desenvolvimento do Sistema Operacional Aurora. O uso foi estritamente focado no aprendizado de estrutura e na compreensão de fórmulas matemáticas, garantindo que toda a implementação lógica e tomada de decisão fossem desenvolvidas pelos integrantes.

Abaixo, nós detalhamos as duas frentes em que a IA foi acionada e as respectivas validações críticas realizadas pelo grupo:

### 1. Estruturação do Banco de Dados (Formato JSON)

**Como a IA foi utilizada** Inicialmente, a equipe possuía dúvidas sobre qual seria o formato de arquivo mais leve, eficiente e integrado com Python para atuar como o banco de dados simulado da telemetria. A IA recomendou o uso do formato JSON. Como não tínhamos familiaridade prévia com a sua estrutura, solicitamos à IA que explicasse as regras de formatação (uso de chaves, listas internas, pares de chave-valor) e como a biblioteca nativa `json` do Python faria a leitura desses dados.

**Validação Crítica**
Não copiamos um banco de dados pronto da IA. Após compreendermos as regras estruturais, a equipe elaborou o próprio conjunto de dados (o arquivo `data.json`), inserindo manualmente os cenários, os valores das 6 leituras de energia, os status dos módulos operacionais e a anomalia exigida pelo projeto. Em seguida, testamos o carregamento no Python (`json.load`) para garantir que os dados estavam acessíveis nos formatos de listas e dicionários.

---

### 2. Algoritmo de Regressão Linear Simples

**Como a IA foi utilizada**
O requisito do projeto exigia uma técnica de previsão sem o uso de bibliotecas avançadas. Como a equipe não sabia implementar o cálculo da Regressão Linear Simples de forma 100% manual, pedimos à IA que nos ensinasse a base matemática do modelo `y = ax + b`. A IA nos forneceu a explicação das equações necessárias para descobrir o coeficiente angular (a) e o coeficiente linear (b):

$$a = \frac{n \sum xy - \sum x \sum y}{n \sum x^2 - (\sum x)^2}$$

**Validação Crítica**
A IA forneceu apenas a teoria matemática. Já a tradução dessa fórmula para a linguagem Python, através de laços `for` e somatórias iterativas, foi construída e codificada manualmente pela equipe no arquivo `regressao.py`. Para validar criticamente se o algoritmo estava correto, a equipe calculou um cenário pequeno manualmente, com o apoio de uma calculadora, e comparou com o resultado impresso pelo nosso código no terminal. A equivalência dos resultados provou que nossa lógica de codificação estava matematicamente correta.

---

### Conclusão da Validação

A Inteligência Artificial atuou apenas como uma ferramenta de nivelamento de conhecimento (documentação de sintaxe e teoria matemática). Enquanto isso, o pensamento computacional, as arquiteturas de funções, o cruzamento de variáveis de telemetria e o controle de fluxo (`if/else`) foram integralmente desenvolvidos pelos integrantes do grupo.
