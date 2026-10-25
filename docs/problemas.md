# Funções de Teste Sorteadas

Projeto Computacional 1: Modelagem e Busca Linear

---

## Resumo em tabela

| TP | Grupo | $f(\mathbf{x})$ | $\mathbf{x}^0$ |
|----|-------|-----------------|----------------|
| 6  | G1 | $\tfrac{1}{2}x_1^2 + x_2^2 - x_1$ | $(-4,\,-2)^T$ |
| 7  | G2 | $[-13 + x_1 + ((5-x_2)x_2 - 2)x_2]^2 + [-29 + x_1 + ((x_2+1)x_2 - 14)x_2]^2$ | $(15,\,-2)^T$ |
| 12 | G2 | $(x_1^2 + x_2 - 11)^2 + (x_1 + x_2^2 - 7)^2$ | $(1,\,1)^T$ |
| 15 | G3 | $[10(x_1 - x_2^2)^2 + (x_1 - 1)^2]^{1/4}$ | $(-1{,}2,\,1{,}0)^T$ |

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

## Grupo 2: TP 7

$$
f_7(\mathbf{x}) = \Big[-13 + x_1 + \big((5 - x_2)\,x_2 - 2\big)\,x_2\Big]^2 + \Big[-29 + x_1 + \big((x_2 + 1)\,x_2 - 14\big)\,x_2\Big]^2
$$

Ponto inicial:

$$
\mathbf{x}^0 = \begin{pmatrix} 15 \\ -2 \end{pmatrix}
$$

### Gradiente

Definindo $u(\mathbf{x}) = x_1 - x_2^3 + 5x_2^2 - 2x_2 - 13$ e $v(\mathbf{x}) = x_1 + x_2^3 + x_2^2 - 14x_2 - 29$:

$$
\nabla f_7(\mathbf{x}) =
\begin{pmatrix}
2u + 2v \\[4pt]
2u\left(-3x_2^2 + 10x_2 - 2\right) + 2v\left(3x_2^2 + 2x_2 - 14\right)
\end{pmatrix}
$$

### Hessiana

$$
\nabla^2 f_7(\mathbf{x}) =
\begin{pmatrix}
4 & 2\left(-3x_2^2 + 10x_2 - 2\right) + 2\left(3x_2^2 + 2x_2 - 14\right) \\[4pt]
\text{Simétrico} & 2\left(-3x_2^2 + 10x_2 - 2\right)^2 + 2u\left(-6x_2 + 10\right) + 2\left(3x_2^2 + 2x_2 - 14\right)^2 + 2v\left(6x_2 + 2\right)
\end{pmatrix}
$$

### Avaliação em $\mathbf{x}^0$

Em $\mathbf{x}^0 = (15, -2)^T$ tem-se $u = 33$ e $v = -11$:

$$
\nabla f_7(\mathbf{x}^0) = \begin{pmatrix} 88 \\ -2432 \end{pmatrix}, \qquad
\nabla^2 f_7(\mathbf{x}^0) = \begin{pmatrix} 4 & -80 \\ -80 & 3680 \end{pmatrix}
$$

### Convexidade e implicações para as direções

- **$f_7$ não é convexa.** Trata-se de uma função polinomial não linear com múltiplos pontos críticos (mínimo local e mínimo global em $\mathbf{x}^* = (5, 4)^T$).
- **Em $\mathbf{x}^0$ a Hessiana é definida positiva:** $\operatorname{tr} = 3684 > 0$ e $\det = 8240 > 0$, com autovalores $\lambda_1 \approx 2{,}26$ e $\lambda_2 \approx 3681{,}74$.
- **Consequência:** A direção pura de Newton $\mathbf{d}_N$ é de descida ($\nabla f(\mathbf{x}^0)^T \mathbf{d}_N < 0$).
- **Escolha de $\mu$:** Como $\nabla^2 f_7(\mathbf{x}^0) \succ 0$, temos $\mu = 0$ e $\mathbf{d}_M = \mathbf{d}_N$.

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

## Grupo 3: TP 15

$$
f_{15}(\mathbf{x}) = \Big[\,10\left(x_1 - x_2^2\right)^2 + \left(x_1 - 1\right)^2\,\Big]^{1/4}
$$

Ponto inicial:

$$
\mathbf{x}^0 = \begin{pmatrix} -1{,}2 \\ 1{,}0 \end{pmatrix}
$$

### Gradiente e Hessiana

Definindo $a(\mathbf{x}) = 10(x_1 - x_2^2)^2 + (x_1 - 1)^2$, de modo que $f_{15}(\mathbf{x}) = a(\mathbf{x})^{1/4}$:

$$
\nabla a(\mathbf{x}) = \begin{pmatrix} 20(x_1 - x_2^2) + 2(x_1 - 1) \\[4pt] -40x_2(x_1 - x_2^2) \end{pmatrix}, \qquad
\nabla^2 a(\mathbf{x}) = \begin{pmatrix} 22 & -40x_2 \\[4pt] -40x_2 & 120x_2^2 - 40x_1 \end{pmatrix}
$$

Pela regra da cadeia para derivadas de ordem superior:

$$
\nabla f_{15}(\mathbf{x}) = \tfrac{1}{4} \, a(\mathbf{x})^{-3/4} \, \nabla a(\mathbf{x})
$$

$$
\nabla^2 f_{15}(\mathbf{x}) = \tfrac{1}{4} \, a(\mathbf{x})^{-3/4} \, \nabla^2 a(\mathbf{x}) - \tfrac{3}{16} \, a(\mathbf{x})^{-7/4} \, \nabla a(\mathbf{x}) \, \nabla a(\mathbf{x})^T
$$

### Avaliação em $\mathbf{x}^0$

Em $\mathbf{x}^0 = (-1{,}2;\, 1{,}0)^T$ tem-se $a(\mathbf{x}^0) = 53{,}24$:

$$
\nabla f_{15}(\mathbf{x}^0) \approx \begin{pmatrix} -0{,}6139 \\ 1{,}1162 \end{pmatrix}, \qquad
\nabla^2 f_{15}(\mathbf{x}^0) \approx \begin{pmatrix} -0{,}1395 & 0{,}2537 \\[4pt] 0{,}2537 & 0{,}7472 \end{pmatrix}
$$

### Convexidade e implicações para as direções

- **$f_{15}$ não é convexa.** É uma variante fracionária da função de Rosenbrock, com mínimo global em $\mathbf{x}^* = (1, 1)^T$ onde $f_{15}(\mathbf{x}^*) = 0$.
- **Em $\mathbf{x}^0$ a Hessiana é indefinida:** $\operatorname{tr} \approx 0{,}6077$ e $\det \approx -0{,}1686 < 0$, com autovalores $\lambda_1 \approx -0{,}2070$ e $\lambda_2 \approx 0{,}8147$.
- **Consequência:** A direção pura de Newton $\mathbf{d}_N$ aponta para subida ($\nabla f(\mathbf{x}^0)^T \mathbf{d}_N \approx 2{,}7012 > 0$), tornando necessária a regularização via $\mathbf{d}_M$.
- **Escolha de $\mu$:** Para que $\nabla^2 f_{15}(\mathbf{x}^0) + \mu I \succ 0$ é necessário $\mu > 0{,}2070$. Na busca heurística por potências de 10, obtém-se $\mu = 1{,}0$.

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