# Funções de Teste Sorteadas

Projeto Computacional 1: Modelagem e Busca Linear

---

## Grupo 1: TP 6

$$
f_6(\mathbf{x}) = \tfrac{1}{2}\,x_1^2 + x_2^2 - x_1
$$

Ponto inicial:

$$
\mathbf{x}^0 = \begin{pmatrix} -4 \\ -2 \end{pmatrix}
$$

### Gradiente e Hessiana

$$
\nabla f_6(\mathbf{x}) = \begin{pmatrix} x_1 - 1 \\ 2x_2 \end{pmatrix}, \qquad
\nabla^2 f_6(\mathbf{x}) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}
$$

### Convexidade

A Hessiana é constante e definida positiva (autovalores $1$ e $2$). Logo, $f_6$ é **globalmente convexa**, com minimizador global único em $\mathbf{x}^* = (1, 0)^T$.

### Avaliação em $\mathbf{x}^0$

$$
\nabla f_6(\mathbf{x}^0) = \begin{pmatrix} -5 \\ -4 \end{pmatrix}, \qquad
\nabla^2 f_6(\mathbf{x}^0) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}
$$

---

## Grupo 2: TP 12

$$
f_{12}(\mathbf{x}) = \left(x_1^2 + x_2 - 11\right)^2 + \left(x_1 + x_2^2 - 7\right)^2
$$

Ponto inicial:

$$
\mathbf{x}^0 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

### Gradiente

Pela regra da cadeia, com $u = x_1^2 + x_2 - 11$ e $v = x_1 + x_2^2 - 7$:

$$
\nabla f_{12}(\mathbf{x}) =
\begin{pmatrix}
4x_1\left(x_1^2 + x_2 - 11\right) + 2\left(x_1 + x_2^2 - 7\right) \\[4pt]
2\left(x_1^2 + x_2 - 11\right) + 4x_2\left(x_1 + x_2^2 - 7\right)
\end{pmatrix}
$$

Forma expandida:

$$
\nabla f_{12}(\mathbf{x}) =
\begin{pmatrix}
4x_1^3 + 4x_1x_2 + 2x_2^2 - 42x_1 - 14 \\[4pt]
2x_1^2 + 4x_1x_2 + 4x_2^3 - 26x_2 - 22
\end{pmatrix}
$$

### Hessiana

$$
\nabla^2 f_{12}(\mathbf{x}) =
\begin{pmatrix}
12x_1^2 + 4x_2 - 42 & 4x_1 + 4x_2 \\[4pt]
4x_1 + 4x_2 & 4x_1 + 12x_2^2 - 26
\end{pmatrix}
$$

### Avaliação em $\mathbf{x}^0$

Em $\mathbf{x}^0 = (1, 1)^T$ tem-se $u = -9$ e $v = -5$:

$$
\nabla f_{12}(\mathbf{x}^0) = \begin{pmatrix} -46 \\ -38 \end{pmatrix}, \qquad
\nabla^2 f_{12}(\mathbf{x}^0) = \begin{pmatrix} -26 & 8 \\ 8 & -10 \end{pmatrix}
$$

### Convexidade e implicações para as direções

- **$f_{12}$ não é convexa.** O sinal da Hessiana muda conforme o ponto (a função possui 4 mínimos locais e pontos de sela).
- **Em $\mathbf{x}^0$ a Hessiana é definida negativa:** $\operatorname{tr} = -36$ e $\det = 196 > 0$, então os dois autovalores são negativos ($\lambda \approx -6{,}69$ e $\lambda \approx -29{,}31$).
- **Consequência:** $\mathbf{d}_N$ aponta para subida, ou seja, $\nabla f(\mathbf{x}^0)^T \mathbf{d}_N > 0$. É o caso em que se registra a falha teórica e se aplica $\mathbf{d}_M$.
- **Escolha de $\mu$:** para $\nabla^2 f(\mathbf{x}^0) + \mu I \succ 0$ é preciso $\mu > 29{,}31$ (módulo do autovalor mais negativo). Com a heurística de multiplicar por 10 a partir de $10^{-3}$, o valor encontrado seria $\mu = 100$.

---

## Grupo 2: TP 7

$$
f_7(\mathbf{x}) = \Big[-13 + x_1 + \big((5 - x_2)\,x_2 - 2\big)\,x_2\Big]^2 + \Big[-29 + x_1 + \big((x_2 + 1)\,x_2 - 14\big)\,x_2\Big]^2
$$

Ponto inicial:

$$
\mathbf{x}^0 = \begin{pmatrix} 15 \\ -2 \end{pmatrix}
$$

*(gradiente e Hessiana: a cargo do outro membro)*

---

## Grupo 3: TP 15

$$
f_{15}(\mathbf{x}) = \Big[\,10\left(x_1 - x_2^2\right)^2 + \left(x_1 - 1\right)^2\,\Big]^{1/4}
$$

Ponto inicial:

$$
\mathbf{x}^0 = \begin{pmatrix} -1{,}2 \\ 1{,}0 \end{pmatrix}
$$

*(gradiente e Hessiana: a cargo do outro membro)*

---

## Resumo em tabela

| TP | Grupo | $f(\mathbf{x})$ | $\mathbf{x}^0$ |
|----|-------|-----------------|----------------|
| 6  | G1 | $\tfrac{1}{2}x_1^2 + x_2^2 - x_1$ | $(-4,\,-2)^T$ |
| 12 | G2 | $(x_1^2 + x_2 - 11)^2 + (x_1 + x_2^2 - 7)^2$ | $(1,\,1)^T$ |
| 7  | G2 | $[-13 + x_1 + ((5-x_2)x_2 - 2)x_2]^2 + [-29 + x_1 + ((x_2+1)x_2 - 14)x_2]^2$ | $(15,\,-2)^T$ |
| 15 | G3 | $[10(x_1 - x_2^2)^2 + (x_1 - 1)^2]^{1/4}$ | $(-1{,}2,\,1{,}0)^T$ |

---

## Função unidimensional parametrizada (busca linear)

Para cada direção de descida $\mathbf{d}$ ($\mathbf{d}_G$, $\mathbf{d}_N$ ou $\mathbf{d}_M$):

$$
\varphi(\alpha) = f(\mathbf{x}^k + \alpha\,\mathbf{d}^k), \qquad
\varphi'(\alpha) = \nabla f(\mathbf{x}^k + \alpha\,\mathbf{d}^k)^T \mathbf{d}^k, \qquad
\varphi''(\alpha) = {\mathbf{d}^k}^T \,\nabla^2 f(\mathbf{x}^k + \alpha\,\mathbf{d}^k)\, \mathbf{d}^k
$$

## Direções de descida

$$
\mathbf{d}_G = -\nabla f(\mathbf{x}^0)
$$

$$
\mathbf{d}_N = -\left[\nabla^2 f(\mathbf{x}^0)\right]^{-1} \nabla f(\mathbf{x}^0)
$$

$$
\mathbf{d}_M = -\left[\nabla^2 f(\mathbf{x}^0) + \mu I\right]^{-1} \nabla f(\mathbf{x}^0), \qquad \mu \ge 0
$$

Condição de descida:

$$
\nabla f(\mathbf{x}^0)^T \mathbf{d} < 0
$$

Próximo ponto:

$$
\mathbf{x}^1 = \mathbf{x}^0 + \alpha^*\,\mathbf{d}
$$