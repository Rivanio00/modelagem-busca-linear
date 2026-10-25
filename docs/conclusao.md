# Resultados e Conclusão

Síntese das duas modelagens e dos 36 experimentos (4 problemas de teste × 3 direções × 3 métodos de busca 1D). Todos os valores vêm das execuções e da tabela dos experimentos.

---

## 1. Modelagens práticas

### 1.1 Critério de Kelly (`kelly_bet.py`)

Minimiza-se $f(\mathbf{x}) = -\mathbb{E}[\ln(1 + \mathbf{R}^T\mathbf{x})]$ por máxima descida com busca linear de Fibonacci, a partir de $\mathbf{x}^0 = (10\%, 10\%)$ (80% em caixa).

* **Derivadas:** o erro entre o gradiente analítico e as diferenças finitas centrais é $3{,}7 \times 10^{-11}$.
* **Convexidade:** em $\mathbf{x}^0$ os autovalores da Hessiana são $0{,}0297$ e $0{,}1420$ (definida positiva). A convexidade estrita global está demonstrada no modelo teórico.

| | $\mathbf{x}^0$ | $\mathbf{x}^1$ ($\alpha^* \approx 8{,}81$; 41 avaliações de $\phi$) | $\mathbf{x}^*$ (4 passos) |
| :--- | :---: | :---: | :---: |
| Ativo 1 | $10{,}00\%$ | $77{,}69\%$ | $130{,}23\%$ |
| Ativo 2 | $10{,}00\%$ | $131{,}23\%$ | $102{,}81\%$ |
| Caixa | $80{,}00\%$ | $-108{,}93\%$ | $-133{,}04\%$ |
| $g = -f$ (taxa de crescimento logarítmica esperada) | $2{,}27\%$ | $13{,}10\%$ | $13{,}67\%$ |

* **Eficiência:** o 1º passo captura $95{,}0\%$ do ganho total de $g$ (de $2{,}27\%$ até $13{,}67\%$). O método converge com $\|\nabla f(\mathbf{x}^*)\| = 1{,}7 \times 10^{-8}$.
* **Ortogonalidade:** $\nabla f(\mathbf{x}^1)^T\mathbf{d}^0 = 1{,}1 \times 10^{-7} \approx 0$, como esperado de uma busca exata (gradientes consecutivos ortogonais, o que explica o zigue-zague da máxima descida).
* **Risco:** o ótimo é alavancado (exposição bruta de $233\%$, caixa negativo). Na recessão (cenário 4) a riqueza cai para $36{,}6\%$ do capital, perda de $63{,}4\%$. Isso é típico do Kelly pleno, e na prática se usa Kelly fracionário.

### 1.2 California Housing (`california_problema.py`)

Minimiza-se o erro quadrático $f(\mathbf{W}) = \frac{1}{2}\sum_{i=1}^{N}(V_i - w_0 - w_1 R_i)^2$ ($N = 20.640$) a partir de $\mathbf{W}_0 = (1, 1)$, com busca de Armijo.

| | $\mathbf{W}_0$ | $\mathbf{W}_1$ |
| :--- | :---: | :---: |
| $f$ | $5{,}790 \times 10^{14}$ | $2{,}152 \times 10^{14}$ |
| $\mathbf{W}$ | $(1{,}0;\ 1{,}0)$ | $(1{,}629 \times 10^{4};\ 7{,}492 \times 10^{4})$ |

* **Resultado:** redução de $62{,}83\%$ no 1º passo, com $\alpha = 3{,}81 \times 10^{-6}$.
* **Escala:** $\|\nabla f(\mathbf{W}_0)\| = 2{,}01 \times 10^{10}$, porque os dados não estão normalizados. O passo coincide com $2^{-18}$, compatível com 18 reduções pela metade no backtracking a partir de $\alpha_0 = 1$. A padronização das variáveis melhoraria muito o condicionamento.
- **Alcance:** este é apenas o 1º passo; o resultado mostra que o método reduz \(f\), mas não que \(\mathbf{W}_1\) esteja perto do ótimo. Como a hessiana é constante e definida positiva em todo o domínio, a função objetivo é estritamente convexa e possui um único ótimo global. Assim, sob as condições usuais de convergência do método de Newton com busca de Armijo, as iterações convergem para esse ótimo global.

---

## 2. Os 36 experimentos

Menor $f(\mathbf{x}^1)$ por problema e direção, entre Fibonacci e Newton 1D (na maioria dos casos os dois coincidem):

| Problema | $f(\mathbf{x}^0)$ | $\mathbf{d}_G$ | $\mathbf{d}_N$ | $\mathbf{d}_M$ |
| :---: | ---: | ---: | ---: | ---: |
| TP6 | $16$ | $1{,}254$ | $-0{,}5$ | $-0{,}5$ |
| TP7 | $1256$ | $136{,}1$ | $133{,}2$ | $133{,}2$ |
| TP12 | $106$ | $3{,}888$ | sem redução | $0{,}757$ |
| TP15 | $2{,}701$ | $1{,}531$ | sem redução | $0{,}974$ (Fibonacci) |

Em todos os problemas o melhor resultado vem de uma direção de 2ª ordem ($\mathbf{d}_N$ ou $\mathbf{d}_M$). Os 6 casos sem redução são todos $\mathbf{d}_N$ em TP12 e TP15.

### 2.1 Direções

* **$\mathbf{d}_G$:** sempre de descida ($\nabla f^T\mathbf{d}_G = -\|\nabla f\|^2 < 0$), mas reduz menos $f$ que as de 2ª ordem nos 4 problemas (em TP7 e TP12 a diferença é pequena, menos de 3%). O passo ótimo varia muito entre problemas: $\alpha^* \approx 2{,}4 \times 10^{-3}$ em TP7, $0{,}037$ em TP12 e $1{,}2$ em TP15.
* **$\mathbf{d}_N$:** em TP6 (quadrático) o passo $\alpha^* = 1$ leva ao ótimo ($f = -0{,}5$). Em TP7 também é a melhor direção. Em TP12 e TP15 não é direção de descida ($\nabla f^T\mathbf{d}_N > 0$), o que implica Hessiana com autovalor negativo em $\mathbf{x}^0$. Nenhum método 1D corrige isso, e o Newton 1D ainda foi para pontos sem sentido ($\alpha^* = 0{,}58$ em TP12 e $1{,}9 \times 10^8$ em TP15).
* **$\mathbf{d}_M$:** coincide com $\mathbf{d}_N$ em TP6 e TP7 (Hessiana já definida positiva em $\mathbf{x}^0$) e corrige TP12 e TP15. Com os métodos exatos, $f$ cai $99{,}3\%$ em TP12 e entre $59\%$ e $64\%$ em TP15.

### 2.2 Buscas 1D (30 casos em que a direção é de descida)

| Método | Iterações | Redução obtida, em relação à melhor do mesmo caso |
| :--- | :---: | :---: |
| Fibonacci | 10 a 23 (mediana 21) | $\ge 99{,}4\%$ |
| Newton 1D | 1 a 33 (mediana 3,5) | $\ge 91{,}8\%$ (pior caso: TP15/$\mathbf{d}_M$) |
| Goldstein | 1 a 10 (mediana 3) | $14\%$ a $85\%$ (mediana $43\%$) |

* **Newton 1D** usa $\phi'$ e $\phi''$ e costuma precisar de poucas iterações (até 4 em 7 dos 10 casos), mas não sempre: 33 em TP7/$\mathbf{d}_G$ e 11 em TP12/$\mathbf{d}_G$. Em TP15/$\mathbf{d}_M$ parou em $\alpha = 2{,}009$ com $f(\mathbf{x}^1) = 1{,}115$, pior que o Fibonacci ($\alpha = 1{,}388$, $f(\mathbf{x}^1) = 0{,}974$). Sendo de convergência local, ele pode terminar fora do minimizador quando $\phi$ não é convexa.
* **Fibonacci** não usa derivadas nem depende de convexidade local, com número de iterações definido pela tolerância e pelo tamanho do intervalo inicial. A tolerância é absoluta ($10^{-4}$), o que limita a precisão quando $\alpha^*$ é pequeno: em TP7/$\mathbf{d}_G$ ($\alpha^* \approx 2{,}4 \times 10^{-3}$) o resultado ficou $1{,}2\%$ distante do Newton 1D e o $f(\mathbf{x}^1)$ foi $142{,}2$ contra $136{,}1$.
* **Goldstein** é o mais barato, mas só aceita um passo que satisfaz as condições (decréscimo suficiente e limite inferior contra passos curtos), sem buscar o mínimo. Cada passo reduz bem menos: em TP12/$\mathbf{d}_M$, $f$ cai $28\%$ contra $99\%$ dos métodos exatos, e em TP15/$\mathbf{d}_M$ cai apenas $8{,}8\%$.

As contagens de iterações não são comparáveis entre métodos: cada um conta uma coisa diferente e o custo por iteração difere (o Newton 1D exige derivadas).

---

## 3. Conclusão

1. **Newton puro não é seguro.** Em 2 dos 4 problemas (TP12 e TP15), a partir do ponto inicial dado, $\mathbf{d}_N$ não é direção de descida. O Newton modificado resolve esses casos e é a melhor direção neles; nos demais, coincide com o Newton.
2. **Exata contra inexata.** Os métodos exatos (Fibonacci, Newton 1D) reduziram mais $f$ por passo em todos os casos, ao custo de mais avaliações. O Goldstein custa menos por passo, o que tende a compensar em problemas maiores, mas isso não foi testado aqui, já que todos os problemas têm poucas variáveis.
3. **Escolha do método 1D.** Newton 1D é rápido quando $\phi$ é bem comportada; o Fibonacci lidou melhor com o caso mais difícil (TP15/$\mathbf{d}_M$). Em ambos, a tolerância deve ser compatível com a escala de $\alpha^*$.
4. **Escala importa.** O mesmo princípio aparece no California Housing: sem normalizar os dados, o passo cai para $10^{-6}$.
5. **Reprodução.** As rotinas têm testes automatizados e os resultados saem dos scripts do repositório.