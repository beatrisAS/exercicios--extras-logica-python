<div align="center">

# 🧮 Exercícios Complementares de Lógica de Programação em Python

**Atividade Prática 01 · Bootcamp de Análise de Dados**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Exercícios](https://img.shields.io/badge/exerc%C3%ADcios-17%2F17-success)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Foco](https://img.shields.io/badge/foco-l%C3%B3gica%20de%20programa%C3%A7%C3%A3o-blue)

</div>

---

## 📌 Sobre o projeto

Este repositório reúne a resolução dos **17 exercícios complementares** da Atividade Prática 01 do bootcamp de **Análise de Dados**, implementados em **Python 3**.

A lista é opcional e foi elaborada para consolidar os fundamentos que sustentam qualquer atividade com dados: **raciocínio lógico, tomada de decisão em código, repetição controlada e manipulação de coleções**. Antes de usar bibliotecas como Pandas ou NumPy, é essencial dominar o que acontece "por baixo": como um valor é lido, transformado, comparado e armazenado.

### 🎯 Objetivos de aprendizagem

- Ler dados do usuário (`input`) e apresentá-los de forma clara e formatada (`print` + *f-strings*).
- Aplicar operadores aritméticos, relacionais e lógicos para resolver problemas reais.
- Controlar o fluxo do programa com estruturas condicionais (`if / elif / else`).
- Automatizar tarefas repetitivas com laços (`for` e `while`).
- Armazenar e manipular conjuntos de dados com **listas**.
- Validar entradas e tratar casos de borda.

### 🧭 Princípios adotados

| Princípio | Como foi aplicado |
|---|---|
| **Simplicidade** | Apenas recursos básicos da linguagem, sem funções personalizadas, classes ou estruturas avançadas, de acordo com o nível da atividade. |
| **Experiência visual** | Saída de terminal estilizada com cores, caixas e símbolos, sem bibliotecas externas e sem alterar a lógica da solução. |
| **Legibilidade** | Nomes de variáveis descritivos (`valor_restante`, `tempo_viagem`) e comentários objetivos. |
| **Fidelidade ao enunciado** | Entradas, saídas e formatos seguem os exemplos fornecidos. |
| **Verificabilidade** | Cada exercício foi executado com os exemplos do enunciado e as saídas conferidas. |
| **Organização** | Exercícios agrupados por tema, com numeração sequencial. |

---

## 🗂️ Estrutura do repositório

```text
exercicios-logica-python/
│
├── 01_variaveis_e_operadores/
│   ├── 01_area_circulo.py
│   ├── 02_consumo_combustivel.py
│   ├── 03_conversao_tempo.py
│   └── 04_decomposicao_cedulas.py
│
├── 02_lacos_condicionais/
│   ├── 05_ordenacao_tres_numeros.py
│   ├── 06_tipo_triangulo.py
│   ├── 07_ddd_cidade.py
│   ├── 08_reajuste_salarial.py
│   └── 09_presentes_duende.py
│
├── 03_lacos_de_repeticao/
│   ├── 10_divisores.py
│   ├── 11_soma_impares.py
│   ├── 12_pares_ao_quadrado.py
│   ├── 13_quadrado_e_cubo.py
│   └── 14_feliz_natal.py
│
├── 04_listas/
│   ├── 15_lista_menores_ou_iguais_10.py
│   ├── 16_inverter_lista.py
│   └── 17_sequencia_repetitiva.py
│
├── .gitignore
└── README.md
```

---

## 🎨 Identidade visual no terminal

Todos os programas compartilham o mesmo padrão visual, construído **somente com a biblioteca padrão** do Python, usando códigos de escape ANSI e caracteres de desenho de caixa (Unicode).

```text
╔══════════════════════════════════════════════════════╗
║                   ÁREA DO CÍRCULO                    ║
╚══════════════════════════════════════════════════════╝

➤ Digite o raio do círculo: 2.00

┌──────────────────────────────────────────────────────┐
│  A área do círculo é: 12.57                          │
└──────────────────────────────────────────────────────┘
```

| Elemento | Cor / Símbolo | Uso |
|---|---|---|
| Cabeçalho `╔═╗` | 🟣 Roxo | Título de cada exercício |
| Prompt `➤` | 🔵 Ciano | Indica onde digitar |
| Resultado `┌─┐` | 🟢 Verde | Saídas e respostas corretas |
| Destaques | 🟡 Amarelo | Subtítulos e valores intermediários |
| Erros `✖` | 🔴 Vermelho | Validação de entradas inválidas |
| Apoio | ⚪ Cinza | Informações secundárias |

**Detalhes que tornam a experiência mais rica:**

- **Exercício 04:** cédulas utilizadas aparecem em verde e as não utilizadas em cinza.
- **Exercício 06:** a cor muda conforme o tipo de triângulo (equilátero, isósceles, escaleno ou inválido).
- **Exercício 13:** os resultados são apresentados em uma **tabela formatada** (Número, Quadrado e Cubo).
- **Exercício 14:** `Feliz Nataaaal!` aparece em vermelho e verde, com 🎄 e ❄️.
- **Validações (12, 13, 14, 17):** mensagens de erro em vermelho, com nova solicitação do dado.

> ⚙️ **Como funciona:** cada cor é uma constante de texto (por exemplo, `VERDE = "\033[92m"`), inserida nas *f-strings*. O comando `os.system("")` no início de cada arquivo habilita as cores no terminal do Windows. O alinhamento das caixas usa os métodos de texto `.center()` e `.ljust()` com uma largura fixa (`LARGURA`).
>
> 💻 **Recomendado:** Windows Terminal, VS Code, PowerShell moderno ou qualquer terminal Linux/macOS. Em terminais muito antigos (como o `cmd` clássico), as cores podem aparecer como símbolos estranhos.

---

## ▶️ Como executar

**Pré-requisito:** [Python 3.8+](https://www.python.org/downloads/) instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/exercicios-logica-python.git

# 2. Acesse a pasta do projeto
cd exercicios-logica-python

# 3. Execute qualquer exercício
python 01_variaveis_e_operadores/01_area_circulo.py
```

> 💡 Em alguns sistemas o comando é `python3` em vez de `python`.

---

## 📋 Índice dos exercícios

| Nº | Exercício | Categoria | Conceitos principais |
|:--:|---|---|---|
| 01 | [Área de um círculo](01_variaveis_e_operadores/01_area_circulo.py) | Variáveis e Operadores | `float`, `math.pi`, potenciação |
| 02 | [Consumo de combustível](01_variaveis_e_operadores/02_consumo_combustivel.py) | Variáveis e Operadores | Constantes, fórmulas encadeadas |
| 03 | [Conversão de tempo](01_variaveis_e_operadores/03_conversao_tempo.py) | Variáveis e Operadores | `//` e `%` |
| 04 | [Decomposição em cédulas](01_variaveis_e_operadores/04_decomposicao_cedulas.py) | Variáveis e Operadores | Algoritmo guloso, resto da divisão |
| 05 | [Ordenação de 3 números](02_lacos_condicionais/05_ordenacao_tres_numeros.py) | Laços Condicionais | `if` aninhado, operadores lógicos |
| 06 | [Tipo de triângulo](02_lacos_condicionais/06_tipo_triangulo.py) | Laços Condicionais | Desigualdade triangular |
| 07 | [DDD e cidade](02_lacos_condicionais/07_ddd_cidade.py) | Laços Condicionais | `if / elif / else` |
| 08 | [Reajuste salarial](02_lacos_condicionais/08_reajuste_salarial.py) | Laços Condicionais | Faixas, percentuais |
| 09 | [Presentes do duende](02_lacos_condicionais/09_presentes_duende.py) | Laços Condicionais | Comparação de somas |
| 10 | [Divisores de um número](03_lacos_de_repeticao/10_divisores.py) | Laços de Repetição | `for`, `range`, divisibilidade |
| 11 | [Soma de ímpares](03_lacos_de_repeticao/11_soma_impares.py) | Laços de Repetição | Acumulador, intervalo |
| 12 | [Pares ao quadrado](03_lacos_de_repeticao/12_pares_ao_quadrado.py) | Laços de Repetição | `while` para validação |
| 13 | [Quadrado e cubo](03_lacos_de_repeticao/13_quadrado_e_cubo.py) | Laços de Repetição | Tabelas, validação |
| 14 | [Feliz Nataaaal](03_lacos_de_repeticao/14_feliz_natal.py) | Laços de Repetição | Construção de strings |
| 15 | [Valores ≤ 10 na lista](04_listas/15_lista_menores_ou_iguais_10.py) | Listas | `append`, índices |
| 16 | [Inversão de lista](04_listas/16_inverter_lista.py) | Listas | Troca com variável auxiliar |
| 17 | [Sequência repetitiva](04_listas/17_sequencia_repetitiva.py) | Listas | Ciclo com módulo (`%`) |

---

## 📖 Detalhamento dos exercícios

### 🔹 Categoria 1 · Variáveis e Operadores

#### 01 · Área de um círculo
- **Problema:** calcular a área de um círculo a partir do raio informado pelo usuário.
- **Fórmula:** `área = π × r²`
- **Solução:** o raio é lido como `float`; a constante π vem do módulo nativo `math` (`math.pi`) e a potenciação usa o operador `**`. O resultado é exibido com 2 casas decimais (`:.2f`).
- **Validação:** `2.00 → 12.57` e `100.64 → 31819.34`.

```text
Digite o raio do círculo: 2.00
A área do círculo é: 12.57
```

#### 02 · Consumo de combustível
- **Problema:** estimar os litros consumidos em uma viagem, dado o tempo e a velocidade média, com rendimento fixo de **12 km/L**.
- **Fórmulas:** `distância = tempo × velocidade` e `consumo = distância ÷ rendimento`.
- **Solução:** o rendimento é uma constante nomeada (`RENDIMENTO`), o que evita "números mágicos" e facilita a manutenção. A saída usa 2 casas decimais.
- **Validação:** `10 h × 85 km/h → 70.83 L`.

#### 03 · Conversão de segundos para `hh:mm:ss`
- **Problema:** converter um intervalo em segundos para horas, minutos e segundos.
- **Solução:** combinação de **divisão inteira** (`//`) e **resto** (`%`):
  - `horas = tempo // 3600`
  - `minutos = (tempo % 3600) // 60`
  - `segundos = tempo % 60`
- **Destaque:** a lógica funciona para qualquer valor, inclusive acima de 24 h (`140153 → 38:55:53`).

#### 04 · Decomposição de um valor em cédulas
- **Problema:** informar a menor quantidade de cédulas (200, 100, 50, 20, 10, 5, 2 e 1) que compõe um valor em reais.
- **Estratégia:** abordagem **gulosa**: usar sempre a maior nota possível e passar o que sobra para a nota seguinte.
  - `quantidade = valor_restante // valor_da_nota`
  - `valor_restante = valor_restante % valor_da_nota`
- **Destaque:** como o sistema monetário brasileiro é "canônico", a estratégia gulosa produz o mínimo de notas. O valor é convertido com `int(float(...))`, aceitando entradas como `576.00`. Cédulas utilizadas são destacadas em verde e as não utilizadas ficam em cinza.

---

### 🔹 Categoria 2 · Laços Condicionais

#### 05 · Ordenação de três números
- **Problema:** exibir três inteiros na ordem original, crescente e decrescente.
- **Solução:** sem usar `sort()`, o algoritmo identifica o **menor**, o **do meio** e o **maior** com `if` aninhado e operadores lógicos (`and`). A ordem decrescente é a crescente invertida.
- **Validação:** `7, 21, -14 → crescente: -14 7 21 · decrescente: 21 7 -14`.

#### 06 · Tipo de triângulo
- **Problema:** classificar um triângulo como equilátero, isósceles ou escaleno, ou indicar que os lados não formam um triângulo.
- **Solução:** a **condição de existência** é verificada primeiro; depois, a classificação é feita pelo número de lados iguais.
- **Decisão técnica:** o enunciado cita apenas `A ≥ B + C`, mas a regra geométrica exige que **nenhum** lado seja maior ou igual à soma dos outros dois. Por isso foram verificadas as três combinações, o que evita classificar incorretamente entradas como `(30, 10, 10)`.

#### 07 · DDD e cidade
- **Problema:** informar a cidade correspondente a um DDD (11, 21, 27 ou 31).
- **Solução:** cadeia `if / elif / else`, com mensagem padrão `DDD não encontrado!` para valores fora da tabela.

#### 08 · Reajuste salarial
- **Problema:** aplicar o percentual de reajuste conforme a faixa salarial e exibir novo salário, valor do reajuste e percentual.

| Salário | Reajuste |
|---|:---:|
| Até R$ 1.412,00 | 15% |
| R$ 1.412,01 a R$ 2.824,00 | 12% |
| R$ 2.824,01 a R$ 4.236,00 | 10% |
| R$ 4.236,01 a R$ 5.648,00 | 7% |
| Acima de R$ 5.648,00 | 5% |

- **Solução:** as faixas são avaliadas em ordem crescente, de modo que cada `elif` só precisa verificar o limite superior.
- **Fórmulas:** `reajuste = (salário × percentual) / 100` e `novo_salário = salário + reajuste`.
- **Validação:** `R$ 3.000,00 → R$ 3.300,00 (10%)`.

#### 09 · Presentes do duende Ed
- **Problema:** decidir se o duende conclui os dois presentes antes do fim do expediente.
- **Solução:** compara-se `presente_1 + presente_2 <= tempo_restante`. O uso de `<=` garante que, se o tempo for exatamente suficiente, a resposta seja "Farei hoje!".

---

### 🔹 Categoria 3 · Laços de Repetição

#### 10 · Divisores de um número
- **Problema:** listar todos os divisores positivos de um inteiro.
- **Solução:** `for i in range(1, n + 1)` testando `n % i == 0`. Números menores ou iguais a zero são tratados com uma mensagem orientativa.
- **Complexidade:** O(n).

#### 11 · Soma dos ímpares entre dois números
- **Problema:** somar todos os ímpares entre X e Y (extremos não incluídos).
- **Solução:** variável **acumuladora** (`soma`) e laço que percorre o intervalo. Se X > Y, os valores são reorganizados para o laço sempre ir do menor ao maior.
- **Validação:** entre 2 e 10 → `3 + 5 + 7 + 9 = 24`.

#### 12 · Pares elevados ao quadrado
- **Problema:** exibir o quadrado de todos os pares de 1 até N (5 ≤ N ≤ 2000).
- **Solução:** validação com `while` (o programa pede o valor novamente enquanto estiver fora do intervalo) e `for` com filtro `i % 2 == 0`.

#### 13 · Quadrado e cubo
- **Problema:** gerar, de 1 até N (1 ≤ N ≤ 1000), uma tabela com número, quadrado e cubo.
- **Solução:** `for` com `i`, `i ** 2` e `i ** 3`, além de validação de intervalo com `while`. Os dados são exibidos em uma **tabela formatada**, com colunas centralizadas por `.center()`.

#### 14 · Feliz Nataaaal!
- **Problema:** repetir a letra `a` em "Natal" conforme o índice de felicidade (1 a 100).
- **Solução:** a string de letras `a` é construída por **concatenação em laço** e inserida entre `"Feliz Nat"` e `"l!"`.
- **Validação:** `5 → Feliz Nataaaaal!`.

---

### 🔹 Categoria 4 · Listas

#### 15 · Valores menores ou iguais a 10
- **Problema:** ler 10 inteiros e mostrar posição e valor dos que forem menores ou iguais a 10.
- **Solução:** a lista é preenchida com `append()` dentro de um `for` e percorrida novamente com filtro `lista[i] <= 10`.
- **Observação:** o título do exemplo diz "menores do que 10", mas o próprio exemplo inclui o valor `10`. O programa segue a regra do enunciado (`<= 10`) e usa o título "menores **ou iguais** a 10" para ser coerente.

#### 16 · Inversão de lista
- **Problema:** inverter uma lista de 20 elementos trocando o 1º com o 20º, o 2º com o 19º e assim por diante.
- **Solução:** 10 trocas com **variável auxiliar** (`auxiliar`), usando o índice espelhado `19 - i`. Cada elemento é trocado uma única vez, sem recriar a lista.
- **Resultado:** `[1, 2, ..., 20] → [20, 19, ..., 1]`.

#### 17 · Sequência repetitiva
- **Problema:** preencher uma lista de 100 posições com a sequência cíclica `0, 1, …, T-1` (2 ≤ T ≤ 50).
- **Solução:** o valor de cada posição é `i % T`. O operador módulo reinicia a contagem automaticamente ao chegar em `T`.
- **Validação:** para `T = 5`: `N[0..4] = 0,1,2,3,4`, `N[5] = 0`, …, `N[99] = 4`.

---

## 🧠 Competências desenvolvidas

- **Pensamento algorítmico:** decompor um problema em passos ordenados.
- **Tratamento de casos de borda:** valores nos limites, entradas inválidas e intervalos invertidos.
- **Formatação de saída:** *f-strings*, casas decimais, alinhamento de texto e apresentação clara dos resultados.
- **Experiência do usuário:** interface de terminal organizada, com feedback visual para sucesso e erro.
- **Base para análise de dados:** acumuladores, filtros, contagens e iteração sobre coleções são a essência de operações que depois serão feitas com Pandas, SQL e Power BI.

---

## 🛠️ Tecnologias

- **Linguagem:** Python 3
- **Módulos da biblioteca padrão:** `math` (Exercício 01) e `os` (habilita as cores no Windows)
- **Estilização:** códigos de escape ANSI e caracteres Unicode de desenho de caixa
- **Versionamento:** Git e GitHub

---

## 👩‍💻 Autoria

**Beatris Antunes Silva**
Estudante de Análise de Dados · Bootcamp de Análise de Dados

