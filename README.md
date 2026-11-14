# modelagem-busca-linear
O objetivo deste projeto computacional é implementar, validar e analisar algoritmos de otimização multidimensional irrestrita acoplados a sub-rotinas de busca linear unidimensional, investigando sua convergência e o comportamento de bacias de atração sob simetria refletida em problemas de teste clássicos.

---

# Segunda Atividade Computacional - Programação Não Linear (PNL)

Este repositório contém a implementação e análise computacional de três métodos de otimização multidimensional — **Gradiente Clássico **, **Quase-Newton SR1 (Symmetric Rank-1) com Salvaguarda** e **Gradiente Conjugado Não-Linear Polak-Ribière ($\text{PR}^+$)** — reaproveitando os algoritmos de busca linear 1D da primeira atividade e aplicados às funções de teste **TP6, TP7, TP12 e TP15** a partir do ponto padrão ($x_A^0$) e do ponto refletido ($x_B^0 = -x_A^0$).**.

---

## Estrutura do Repositório

```text
.
├── base.py                    # Classes base e construtor de funções 
├── problemas.py               # Definição e validação das funções de teste (TP6, TP7, TP12, TP15)
├── condicoes.py               # Motor de busca linear e condições de descida (Armijo, Wolfe e Goldstein)
├── direcoes.py                # Direção básica de descida (fallback de segurança para busca linear)
├── busca_iterativa.py         # Utilitário legado de passo iterativo
├── experimentos.py            # Script executor da bateria de 24 experimentos (Simetria Refletida)
├── requirements.txt           # Dependências do projeto (numpy, pandas, tabulate)
├── metodos/                   # Suíte de métodos multidimensionais
│   ├── __init__.py
│   ├── gradiente.py           # Baseline: Método do Gradiente Clássico
│   ├── sr1.py                 # Quase-Newton SR1 com condição de    salvaguarda 
│   └── polak_ribiere.py       # Gradiente Conjugado Polak-Ribière (PR+) com reinício automático
├── busca_linear/              # Módulos dos métodos de busca 1D (reaproveitados da Atividade 1)
│   ├── __init__.py
│   └── fibonacci.py           # Método de Fibonacci + Enquadramento de Intervalo
└── docs/                      # Relatórios, tabela consolidada de testes, análises e apêndices
```

---

## Documentação

Na pasta `/docs` organizamos a documentação técnica do projeto, incluindo a dedução analítica dos problemas (`problemas.md`), a tabela consolidada dos experimentos (`tabela_24_experimentos.md`), a análise geométrica das bacias de atração, o manual de uso e o apêndice de auditoria de IA.

---

## Executando o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/Rivanio00 modelagem-busca-linear.git
cd modelagem-busca-linear
```

### 2. Configurar o Ambiente Virtual e Instalar Dependências

Criar e ativar o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 3. Executar a Bateria de Experimentos

Para rodar a combinação dos $4 \text{ Problemas} \times 2 \text{ Pontos Iniciais } (x_A^0 \text{ e } x_B^0 = -x_A^0) \times 3 \text{ Métodos}$ e gerar a tabela consolidada em `docs/tabela_24_experimentos.md`:

```bash
python experimentos.py
```

---

# Matriz de Responsabilidades

| Tarefa | José Rivânio | Pedro Wagner | Detalhes / Observações |
| :--- | :---: | :---: | :--- |
| **Estruturação do Repositório & Contrato** | X |   | Limpeza do repositório, módulo `metodos/` e especificação em `CONTRATO_INTERFACES.md`. |
| **Método do Gradiente Clássico (Baseline)** | X |   | Implementação do laço iterativo acoplado à busca linear 1D e critérios de parada. |
| **Método Quase-Newton SR1** | X |   | Atualização de posto 1 com salvaguarda $\|s_k^T(y_k - B_k s_k)\| \ge r\|s_k\|\|y_k - B_k s_k\|$. |
| **Gradiente Conjugado Polak-Ribière ($\text{PR}^+$)** |   | X | Implementação da fórmula $\beta_k^{PR+}$ com reinício automático quando $\beta_k < 0$. |
| **Script dos 24 Experimentos** | X |   | Automação da bateria com ponto padrão ($x_A^0$) e refletido ($x_B^0 = -x_A^0$). |
| **Testes Unitários & Validação** |   | X | Verificação de convergência e tolerâncias numéricas ($10^{-5}$ e $10^{-7}$). |
| **Fichamentos EU-UFC (5 Trabalhos)** | X | X | Análise crítica de artigos dos anais dos EU-UFC (3 por José Rivânio, 2 por Pedro Wagner). |
| **Análise de Bacias de Atração & Manual** | X |   | Estudo da simetria refletida em problemas convexos e não-convexos + Manual de Uso. |
| **Comparativo de Desempenho & Auditoria IA** |   | X | Análise entre métodos e documentação crítica do uso de LLMs no relatório. |
| **Revisão e Formatação Final** | X | X | Validação final dos entregáveis e compilação do relatório técnico. |

---

## Resumo dos Resultados dos Experimentos (Simetria Refletida)

1. **Problema Convexo (TP6):** Tanto a partir de $x_A^0 = [-4, -2]^T$ quanto do ponto refletido $x_B^0 = [4, 2]^T$, os algoritmos convergem em apenas **2 iterações** para o mesmo minimizador global $[1, 0]^T$ ($f = -0{,}5$), confirmando a unicidade da bacia de atração em funções estritamente convexas.
2. **Vale Estreito e Mal-Condicionado (TP7):** O Gradiente Clássico sofre severamente com o ziguezague ortogonal, atingindo o teto de **1000 iterações** sem convergir em ambos os pontos iniciais. Em contraste, o **SR1 com Salvaguarda** aproxima a curvatura local e converge com precisão de máquina para $[5, 4]^T$ em **12 iterações** ($x_A^0$) e **10 iterações** ($x_B^0$).
3. **Múltiplas Bacias de Atração (TP12 — Himmelblau):** A inversão de sinais muda o quadrante de convergência. A partir de $x_A^0 = [1, 1]^T$, os métodos convergem para $[3, 2]^T$; partindo de $x_B^0 = [-1, -1]^T$, cruzam a fronteira entre bacias e convergem para outro mínimo global distinto em $[-3{,}7793, -3{,}2832]^T$.
4. **Curvatura Extrema (TP15):** O **SR1** reduz o custo iterativo em aproximadamente **10 vezes** em relação ao Gradiente Clássico (~40 vs. ~400 iterações), evidenciando a eficiência da informação de segunda ordem aproximada frente a vales muito íngremes.