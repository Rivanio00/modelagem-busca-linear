# Parte 1: Questão de Modelagem Prática

## Aplicação do Critério de Kelly Multi-Ativo para Alocação Ótima de Capital

## 1. Contextualização do Fenômeno e Dados

### 1.1 Contextualização e Motivação Econômica
O **Critério de Kelly** (Kelly, 1956; Thorp, 2006) é um modelo clássico de teoria da informação e finanças quantitativas projetado para determinar a fração ótima de capital a ser alocada em investimentos arriscados. Em vez de focar apenas no retorno médio esperado (que pode levar à falência por alavancagem excessiva), o critério maximiza a **taxa esperada de crescimento composto (logarítmica)** do patrimônio a longo prazo.

Em mercados financeiros ou apostas simultâneas em múltiplos ativos correlacionados, um investidor busca alocar frações do seu patrimônio entre ativos de alto risco para maximizar o retorno acumulado, evitando o risco de falência.

### 1.2 Parâmetros e Dados do Mercado
Consideramos um horizonte de investimento com $S = 4$ cenários econômicos discretos (estados da natureza), onde cada cenário $s \in \{1, 2, 3, 4\}$ possui uma probabilidade de ocorrência $p_s$ (tal que $\sum_{s=1}^S p_s = 1$) e retornos associados $R_{s,1}$ e $R_{s,2}$ para dois ativos arriscados distintos.

| Cenário ($s$) | Descrição do Estado | Probabilidade ($p_s$) | Retorno Ativo 1 ($R_{s,1}$) | Retorno Ativo 2 ($R_{s,2}$) |
| :---: | :--- | :---: | :---: | :---: |
| **1** | Expansão Forte do Mercado | $0{,}35$ | $+30\%$ ($+0{,}30$) | $+50\%$ ($+0{,}50$) |
| **2** | Crescimento Seletivo (Ativo 1) | $0{,}35$ | $+10\%$ ($+0{,}10$) | $-20\%$ ($-0{,}20$) |
| **3** | Rotação de Capital (Ativo 2) | $0{,}20$ | $-15\%$ ($-0{,}15$) | $+40\%$ ($+0{,}40$) |
| **4** | Recessão / Retração Geral | $0{,}10$ | $-25\%$ ($-0{,}25$) | $-30\%$ ($-0{,}30$) |

Os retornos esperados são $\mathbb{E}[R_1] = 8{,}5\%$ e $\mathbb{E}[R_2] = 15{,}5\%$ por período, ambos positivos, de modo que existe incentivo a alocar capital nos dois ativos.

---

## 2. Definição das Variáveis de Decisão

O vetor de decisão é definido por $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} \in \mathbb{R}^2$, onde:

* $x_1 \in \mathbb{R}$: Fração do patrimônio total alocada no **Ativo 1**.
* $x_2 \in \mathbb{R}$: Fração do patrimônio total alocada no **Ativo 2**.

A fração restante $1 - x_1 - x_2$ permanece mantida em caixa (ativo livre de risco com retorno nulo). 

*Valores $x_i > 0$ indicam posições compradas (*long*). Se $x_1 + x_2 > 1$, o caixa é negativo, o que corresponde a tomar empréstimo (alavancagem). A formulação não impõe limite de alavancagem, e, como mostra a Seção 5, o ótimo do problema é de fato alavancado.*

**Premissas do modelo:** (i) o empréstimo e o caixa rendem taxa zero, sem limite de crédito; (ii) os períodos são independentes e identicamente distribuídos; (iii) todo o patrimônio é reinvestido a cada período; (iv) não há custos de transação.

---

## 3. Formulação da Função Objetivo Irrestrita $f(\mathbf{x})$

### 3.1 Dedução da Função de Riqueza
Dado o investimento inicial $W_0$, a riqueza acumulada no cenário $s$ após um período é dada por:

$$
W_s(\mathbf{x}) = W_0 \left(1 + x_1 R_{s,1} + x_2 R_{s,2}\right) = W_0 \left(1 + \mathbf{R}_s^T \mathbf{x}\right)
$$

onde $\mathbf{R}_s = \begin{pmatrix} R_{s,1} \\ R_{s,2} \end{pmatrix}$ é o vetor de retornos do cenário $s$.

Sem perda de generalidade, normaliza-se a riqueza inicial $W_0 = 1$. O fator de riqueza bruta no cenário $s$ é:

$$
W_s(\mathbf{x}) = 1 + x_1 R_{s,1} + x_2 R_{s,2}
$$

### 3.2 Maximização do Crescimento Logarítmico
O Critério de Kelly maximiza o valor esperado da taxa de crescimento logarítmica $\mathbb{E}[\ln W_s(\mathbf{x})]$:

$$
\max_{\mathbf{x}} \mathbb{E}[\ln W_s(\mathbf{x})] = \sum_{s=1}^S p_s \ln\left(1 + x_1 R_{s,1} + x_2 R_{s,2}\right)
$$

### 3.3 Reformulação para Minimização Irrestrita
Para adequação ao padrão de Programação Não Linear ($\min f(\mathbf{x})$), multiplica-se a função por $-1$:

$$
f(\mathbf{x}) = -\sum_{s=1}^S p_s \ln\left(1 + x_1 R_{s,1} + x_2 R_{s,2}\right) = -\sum_{s=1}^S p_s \ln\left(W_s(\mathbf{x})\right)
$$

#### Domínio e Tratamento da Inexistência de Restrições Explícitas
A função $f$ só está definida no conjunto

$$
D = \{\mathbf{x} \in \mathbb{R}^2 : 1 + \mathbf{R}_s^T \mathbf{x} > 0,\ s = 1, \dots, S\},
$$

interseção de $S$ semiplanos abertos, portanto **aberto e convexo**. Fora de $D$ (falência em algum cenário) o logaritmo não existe, e convenciona-se $f = +\infty$.

A função logarítmica atua como uma **barreira intrínseca**: quando $W_s(\mathbf{x}) \to 0^+$, $\ln(W_s) \to -\infty$, fazendo com que $f(\mathbf{x}) \to +\infty$ ao se aproximar da fronteira de $D$. Assim, um minimizador, se existir, é **interior** a $D$: nenhuma restrição fica ativa, e o problema pode ser tratado como **otimização irrestrita** (sem restrições explícitas), com $\nabla f(\mathbf{x}^*) = \mathbf{0}$ como condição necessária e, pela convexidade, também suficiente. Todas as análises a seguir são feitas em $D$.

---

## 4. Dedução Analítica de 1ª e 2ª Ordem e Convexidade

### 4.1 Vetor Gradiente $\nabla f(\mathbf{x})$

Aplicando a regra da cadeia para determinar as derivadas parciais de $f(\mathbf{x})$ em relação a $x_1$ e $x_2$:

$$
\frac{\partial f}{\partial x_1} = -\sum_{s=1}^S p_s \cdot \frac{1}{W_s(\mathbf{x})} \cdot \frac{\partial W_s}{\partial x_1} = -\sum_{s=1}^S \frac{p_s R_{s,1}}{1 + x_1 R_{s,1} + x_2 R_{s,2}}
$$

$$
\frac{\partial f}{\partial x_2} = -\sum_{s=1}^S p_s \cdot \frac{1}{W_s(\mathbf{x})} \cdot \frac{\partial W_s}{\partial x_2} = -\sum_{s=1}^S \frac{p_s R_{s,2}}{1 + x_1 R_{s,1} + x_2 R_{s,2}}
$$

Expressando em forma vetorial compacta:

$$
\nabla f(\mathbf{x}) = -\sum_{s=1}^S \frac{p_s}{W_s(\mathbf{x})} \begin{pmatrix} R_{s,1} \\ R_{s,2} \end{pmatrix} = -\sum_{s=1}^S \frac{p_s}{W_s(\mathbf{x})} \mathbf{R}_s
$$

---

### 4.2 Matriz Hessiana $\nabla^2 f(\mathbf{x})$

Diferenciando novamente as derivadas parciais para obter a matriz de segundas derivadas $2 \times 2$:

$$
\frac{\partial^2 f}{\partial x_1^2} = -\sum_{s=1}^S p_s R_{s,1} \cdot \left( -\frac{R_{s,1}}{\left[W_s(\mathbf{x})\right]^2} \right) = \sum_{s=1}^S \frac{p_s R_{s,1}^2}{\left[W_s(\mathbf{x})\right]^2}
$$

$$
\frac{\partial^2 f}{\partial x_2^2} = -\sum_{s=1}^S p_s R_{s,2} \cdot \left( -\frac{R_{s,2}}{\left[W_s(\mathbf{x})\right]^2} \right) = \sum_{s=1}^S \frac{p_s R_{s,2}^2}{\left[W_s(\mathbf{x})\right]^2}
$$

$$
\frac{\partial^2 f}{\partial x_1 \partial x_2} = \frac{\partial^2 f}{\partial x_2 \partial x_1} = \sum_{s=1}^S \frac{p_s R_{s,1} R_{s,2}}{\left[W_s(\mathbf{x})\right]^2}
$$

Expressando em forma vetorial através do produto externo ($\mathbf{R}_s \mathbf{R}_s^T$):

$$
\nabla^2 f(\mathbf{x}) = \sum_{s=1}^S \frac{p_s}{\left[W_s(\mathbf{x})\right]^2} \begin{pmatrix} R_{s,1} \\ R_{s,2} \end{pmatrix} \begin{pmatrix} R_{s,1} & R_{s,2} \end{pmatrix} = \sum_{s=1}^S \frac{p_s}{\left[W_s(\mathbf{x})\right]^2} \mathbf{R}_s \mathbf{R}_s^T
$$

---

### 4.3 Análise e Prova de Convexidade

Para verificar a convexidade de $f(\mathbf{x})$, avaliamos a forma quadrática $\mathbf{v}^T \nabla^2 f(\mathbf{x}) \mathbf{v}$ para qualquer vetor não-nulo $\mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \in \mathbb{R}^2 \setminus \{\mathbf{0}\}$:

$$
\mathbf{v}^T \nabla^2 f(\mathbf{x}) \mathbf{v} = \mathbf{v}^T \left( \sum_{s=1}^S \frac{p_s}{\left[W_s(\mathbf{x})\right]^2} \mathbf{R}_s \mathbf{R}_s^T \right) \mathbf{v} = \sum_{s=1}^S \frac{p_s}{\left[W_s(\mathbf{x})\right]^2} \left( \mathbf{v}^T \mathbf{R}_s \right) \left( \mathbf{R}_s^T \mathbf{v} \right)
$$

Como $\mathbf{v}^T \mathbf{R}_s = \mathbf{R}_s^T \mathbf{v}$ é um escalar:

$$
\mathbf{v}^T \nabla^2 f(\mathbf{x}) \mathbf{v} = \sum_{s=1}^S \frac{p_s}{\left[W_s(\mathbf{x})\right]^2} \left(\mathbf{R}_s^T \mathbf{v}\right)^2
$$

Dado que no domínio admissível $W_s(\mathbf{x}) > 0$, $p_s > 0$ e $\left(\mathbf{R}_s^T \mathbf{v}\right)^2 \ge 0$:
1. A soma é não-negativa para todo $\mathbf{x} \in D$.
2. Como os vetores de retorno $\mathbf{R}_s$ dos 4 cenários geram o espaço $\mathbb{R}^2$ (não são colineares), não existe vetor não-nulo $\mathbf{v}$ tal que $\mathbf{R}_s^T \mathbf{v} = 0$ para todos os cenários $s$ simultaneamente.

Logo, $\mathbf{v}^T \nabla^2 f(\mathbf{x}) \mathbf{v} > 0$ para todo $\mathbf{v} \neq \mathbf{0}$, demonstrando que a matriz Hessiana é **estritamente definida positiva** ($\nabla^2 f(\mathbf{x}) \succ 0$).

**Unicidade:** A função objetivo $f(\mathbf{x})$ é **estritamente convexa** em $D$. Logo, se existir um minimizador, ele é **único**, e todo ponto crítico é o minimizador global (não há outros mínimos locais nem pontos de sela).

### 4.4 Existência do Minimizador

A convexidade estrita garante apenas a unicidade (a função $e^x$ é estritamente convexa e não tem mínimo). A existência vem de três fatos:

1. $f$ é contínua em $D$ e $f \to +\infty$ na fronteira de $D$ (Seção 3.3).
2. $D$ é **limitado**. Se não fosse, existiria uma direção $\mathbf{v} \neq \mathbf{0}$ com $\mathbf{R}_s^T \mathbf{v} \ge 0$ para todo $s$. Pelos cenários 2, 3 e 4 isso exige $v_1 \ge 2 v_2$, $v_2 \ge 0{,}375\, v_1$ e $v_1 \le -1{,}2\, v_2$. Se $v_2 > 0$, a primeira e a terceira condições se contradizem ($v_1 > 0$ e $v_1 < 0$). Se $v_2 < 0$, a segunda dá $v_1 \le 2{,}67\, v_2 < 2 v_2$, contradizendo a primeira. Resta $v_2 = 0$, que força $v_1 \ge 0$ e $v_1 \le 0$, ou seja, $\mathbf{v} = \mathbf{0}$.
3. Assim, os conjuntos de nível $\{f \le c\}$ são compactos, e o mínimo é atingido (Weierstrass).

**Conclusão Teórica:** existe um **minimizador global único** $\mathbf{x}^* \in D$, caracterizado por

$$
\nabla f(\mathbf{x}^*) = \mathbf{0} \iff \sum_{s=1}^S \frac{p_s}{W_s(\mathbf{x}^*)} \mathbf{R}_s = \mathbf{0}.
$$

---

## 5. Resultado Numérico: Máxima Descida com Busca Linear de Fibonacci

Partindo de $\mathbf{x}^0 = (10\%, 10\%)$ (80% em caixa), com $f(\mathbf{x}^0) = -0{,}022700$ (taxa de crescimento logarítmica de $2{,}27\%$ por período), o método de máxima descida com busca linear de Fibonacci ($\mathbf{d}^k = -\nabla f(\mathbf{x}^k)$) fornece:

| | $\mathbf{x}^0$ | $\mathbf{x}^1$ (1º passo, $\alpha^* \approx 8{,}81$) | $\mathbf{x}^*$ (4 passos, $\lVert\nabla f\rVert < 10^{-6}$) |
| :--- | :---: | :---: | :---: |
| Ativo 1 | $10{,}00\%$ | $77{,}69\%$ | $130{,}23\%$ |
| Ativo 2 | $10{,}00\%$ | $131{,}23\%$ | $102{,}81\%$ |
| Caixa | $80{,}00\%$ | $-108{,}93\%$ | $-133{,}04\%$ |
| $g = -f$ (por período) | $2{,}27\%$ | $13{,}10\%$ | $13{,}67\%$ |

Observações:

* **O ótimo é alavancado.** A exposição bruta em $\mathbf{x}^*$ é $233\%$ do patrimônio, financiada por empréstimo ($-133\%$ em caixa). É o comportamento típico do Kelly pleno, que ignora aversão a risco além da maximização do crescimento logarítmico.
* **Risco associado.** A riqueza por cenário em $\mathbf{x}^*$ é $W = (1{,}905;\ 0{,}925;\ 1{,}216;\ 0{,}366)$: na recessão (probabilidade $10\%$) o patrimônio cai $63{,}4\%$. Na prática, usa-se *Kelly fracionário* (uma fração de $\mathbf{x}^*$) para reduzir essa volatilidade; isso fica fora do escopo da formulação irrestrita.
* **Comportamento do método.** O primeiro passo captura cerca de $95\%$ do ganho total. Como a busca linear é exata, o gradiente em $\mathbf{x}^1$ é ortogonal à direção anterior ($\nabla f(\mathbf{x}^1)^T \mathbf{d}^0 \approx 0$), o que caracteriza o zigue-zague da máxima descida, com convergência linear a $\mathbf{x}^*$.
* **Verificação.** Em $\mathbf{x}^*$, $\lVert \nabla f(\mathbf{x}^*) \rVert \approx 10^{-8}$, e a Hessiana é definida positiva (Seção 4.3), de modo que $\mathbf{x}^*$ é o ótimo global único.

---

## 6. Referências Bibliográficas

1. **Kelly, J. L.** (1956). *A New Interpretation of Information Rate*. Bell System Technical Journal, 35(4), 917–926. [DOI: 10.1002/j.1538-7305.1956.tb03809.x](https://doi.org/10.1002/j.1538-7305.1956.tb03809.x).
2. **Thorp, E. O.** (2006). *The Kelly Criterion in Blackjack Sports Betting and the Stock Market*. Handbook of Asset and Liability Management, Volume 1, Elsevier, pp. 385–428.
3. **Cover, T. M., & Thomas, J. A.** (2006). *Elements of Information Theory*. 2nd Edition, Wiley-Interscience, Chapter 16: *Information Theory and Portfolio Theory*.