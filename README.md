# modelagem-busca-linear
O objetivo deste projeto computacional é integrar a modelagem de problemas reais e o simulação de algoritmos de busca linear ou unidimensional em problemas de teste clássicos.

---

# Projeto Computacional - Otimização Não Linear (PNL)

Este repositório contém a implementação, validação e análise computacional de métodos de otimização irrestrita e busca linear 1D, aplicados tanto a funções de teste teóricas (TP6, TP7, TP12 e TP15) quanto a um problema de modelagem prática do mundo real baseado no **Critério de Kelly** para alocação de ativos e um problema de regressão linear baseado no dataset california_housing usando de **maximização de uma verossimilhança gaussiana**.

---

## Estrutura do Repositório

```text
.
├── base.py                   # Classes base e construtor de funções unidimensionais make_phi
├── problemas.py              # Definição e validação das funções de teste (TP6, TP7, TP12, TP15)
├── direcoes.py               # Métodos para cálculo das direções d_G, d_N e d_M (Newton Modificado)
├── condicoes.py              # Condições de descida (Armijo, Wolfe e Goldstein)
├── busca_iterativa.py        # Loop de otimização irrestrita iterativa
├── experimentos.py           # Script executor da bateria de 36 experimentos
├── requirements.txt          # Dependências do projeto (numpy, pandas, tabulate)
├── busca_linear/             # Módulos dos métodos de busca 1D
│   ├── __init__.py
│   ├── fibonacci.py          # Método de Fibonacci + Enquadramento de Intervalo
│   ├── newton1d.py           # Método de Newton 1D (Derivadas de phi)
│   └── goldstein.py          # Método Inexato de Goldstein
├── modelagem/                # Aplicação Prática do Mundo Real
│   └── kelly_bet/
│       ├── Kelly_bet.md      # Dedução teórica, gradiente, Hessiana, convexidade e referências
│       └── kelly_bet.py      # Execução do 1º passo e interpretação financeira
│   └── california/
│       ├── PNL_modelagem_trabalho.pdf      # Dedução teórica, gradiente, Hessiana, convexidade e relatório da execução do primeiro passo.
│       └── california_problema.py      # Execução do 1º passo e relatório detalhado.
│       └── housing.csv     # dataset usado na modelagem.
└── tabela_36_experimentos.md # Tabela consolidada dos 36 casos de teste
```
---
## Documentação

### Na pasta /docs organizamos a documentação de  desenvovimento do projeto de resultados!

---

## Executando o Projeto

### 1. Clone o repositório 

```bash 
git clone https://github.com/Rivanio00/modelagem-busca-linear.git 
cd modelagem-busca-linear
```

### 2. Configurar o Ambiente Virtual e Instalar Dependências

Criar e ativar o ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 3.1 Executar a Aplicação Prática (Critério de Kelly)

Para rodar a simulação do 1º passo de alocação de capital e visualizar a interpretação financeira dos resultados:

```bash
python modelagem/kelly_bet/kelly_bet.py
```

### 3.2 Executar a Aplicação Prática (California Housing Prices)

Para rodar a simulação do 1º passo que estima o valor médio de uma vizinhança a interpretação dos resultados:

```bash
python modelagem/california/california_problema.py
```

### 3.3 Executar a Bateria dos 36 Experimentos

Para rodar a combinação dos $4 \text{ Problemas} \times 3 \text{ Direções} \times 3 \text{ Métodos 1D}$ e gerar a tabela consolidada:

```bash
python experimentos.py
```

---

# Matriz de Responsabilidades

| Tarefa | José Rivânio | Pedro Wagner | Detalhes / Observações |
| :--- | :---: | :---: | :--- |
| **Modelagem Teórica & Derivadas** | X | X | Modelagem dos problemas TP6, TP7, TP12, TP15, Critério de Kelly e Regressão Linear. |
| **Implementação de Direções de Busca** | X |   | Métodos do Gradiente ($d_G$), Newton ($d_N$) e Newton Modificado ($d_M$). |
| **Busca Linear 1D — Fibonacci** | X |   | Algoritmo de cercamento de intervalo e redução via sequência de Fibonacci. |
| **Busca Linear 1D — Newton 1D** |   | X | Método exato utilizando 1ª e 2ª derivadas de $\varphi(\alpha)$ |
| **Busca Linear 1D — Goldstein** |   | X | Condições de decréscimo suficiente e canalização com contagem de iterações. |
| **Script dos 36 Experimentos** | X | X | Integração da matriz $4 \times 3 \times 3$ e exportação da tabela em Markdown. |
| **Modelagem Prática (Critério de Kelly)** | X |   | Formulação do problema real de alocação de ativos e script `kelly_bet.py`. |
| **Modelagem Prática (Regressão Linear)** |  | X | Formulação do problema de regressão linear com dados reais e script `california_problema.py`. |
| **Estruturação do Repositório & Módulos** | X |   | Configuração de pastas (`busca_linear/`, `modelagem/`), imports e `requirements.txt`. |
| **Redação do Relatório Técnico** | X | X | Análise dos resultados, gráficos, tabelas e apêndice de IA. |
| **Revisão e Formatação Final** | X | X | Teste de reproduzibilidade do zero e compilação do documento. |

---

## Resumo dos Resultados dos Experimentos (36 Casos)

1. **Newton Modificado ($\mathbf{d}_M$):** Resolveu com sucesso os casos em que a matriz Hessiana original $\nabla^2 f(\mathbf{x}^0)$ não era definida positiva (ex: **TP12** e **TP15**), onde o Newton Clássico ($\mathbf{d}_N$) falhou por gerar direções de subida.
2. **Comparação dos Métodos 1D:**
   * **Newton 1D:** Exigiu o **menor número de iterações** (1 a 4 iterações na maioria dos casos) por usar informação de 2ª ordem.
   * **Fibonacci:** Apresentou alta precisão em $\alpha^*$ sem necessidade de derivadas de $\varphi$.
   * **Goldstein:** Cumpriu com eficiência o papel de busca inexata, encontrando o passo de decréscimo em poucas iterações (1 a 10 iterações).