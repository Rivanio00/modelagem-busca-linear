# Resultados e Conclusão

## 1. Análise dos Resultados e Bacias de Atração

### 1.1 Problema Convexo (TP6)
A função de teste **TP6**, definida por $f(x) = 0{,}5x_1^2 + x_2^2 - x_1$, possui matriz Hessiana constante e definida positiva em todo o domínio:

$$
\nabla^2 f(x) = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}, \quad \text{com número de condicionamento } \kappa(H) = \frac{\lambda_{\max}}{\lambda_{\min}} = 2
$$

Por ser uma função **estritamente convexa**, existe um único ponto estacionário em $\mathbb{R}^2$, o qual corresponde ao minimizador global $x^* = (1, 0)^T$ com $f(x^*) = -0{,}5$. Geometricamente, sua bacia de atração abrange todo o espaço $\mathbb{R}^2$ sem barreiras ou regiões de repulsão. Consequentemente, tanto partindo do ponto padrão $x_A^0 = (-4, -2)^T$ quanto do ponto refletido $x_B^0 = (4, 2)^T$, todos os algoritmos convergem rigorosamente para a mesma solução ótima (`Convergiu (Gradiente)` com $\|\nabla f(x^*)\|_2 = 0$), exigindo apenas **2 iterações** no Gradiente Clássico e no SR1, e **4 e 2 iterações** no Gradiente Conjugado com Polak-Ribiere ($\text{PR}^+$).

### 1.2 Geometria nos Problemas Não-Convexos e Mal-Condicionados (TP7, TP12 e TP15)

* **TP7 (Mal-Condicionado / Vale Estreito):**
  Possui minimizador global em $x^* = (5, 4)^T$ com $f(x^*) = 0$, inserido em um vale extremamente estreito e mal-condicionado ($\kappa \gg 1$). A inversão do ponto inicial de $x_A^0 = (15, -2)^T$ para $x_B^0 = (-15, 2)^T$ mantém ambos os pontos na mesma macro-bacia de atração do mínimo global, mas expõe drasticamente a diferença entre os métodos:
  * O **Gradiente Clássico** sofre com o efeito de ziguezague ortogonal ao cruzar as paredes íngremes do vale, estourando o teto de **1000 iterações** (`Max Iter`) em ambos os cenários sem atingir a convergência ($f = 0{,}7643$ a partir de $x_A^0$ e $f = 0{,}0374$ a partir de $x_B^0$).
  * O **SR1 com Salvaguarda** constrói progressivamente a curvatura local por meio de atualizações de posto 1, atravessando o vale em **12 iterações** a partir de $x_A^0$ ($f \approx 1{,}93 \times 10^{-16}$) e **10 iterações** a partir de $x_B^0$ ($f \approx 1{,}59 \times 10^{-21}$).
  * O **Gradiente Conjugado ($\text{PR}^+$)** aproxima-se satisfatoriamente do mínimo a partir de $x_A^0$ (**197 iterações**, $f \approx 9{,}21 \times 10^{-5}$), porém, no ponto refletido $x_B^0 = (-15, 2)^T$, sofre perda de conjugação das direções sob busca inexata de Armijo e estagna prematuramente em $(11{,}0816, -0{,}9171)^T$ ($f = 49{,}0295$) pelo critério de variação relativa de $f$.

* **TP12 (Não-Convexo / Função de Himmelblau — Múltiplas Bacias):**
  Esta função apresenta quatro minimizadores globais distintos ($f(x^*) = 0$) distribuídos nos quatro quadrantes, separados por cristas e pontos de sela. A reflexão de coordenadas altera diretamente a bacia de atração capturada pelos métodos:
  * Partindo de $x_A^0 = (1, 1)^T$ (1º quadrante), todos os algoritmos permanecem na bacia local e convergem para $x^* = (3, 2)^T$ (**8 iterações** no SR1, **14** no Gradiente Clássico e **17** no Gradiente Conjugado).
  * Ao refletir para $x_B^0 = (-1, -1)^T$ (3º quadrante), as trajetórias cruzam a fronteira de separação e convergem para outro minimizador global distinto: $x^* \approx (-3{,}7793, -3{,}2832)^T$ (**10 iterações** no SR1, **11** no Gradiente Clássico e **14** no Gradiente Conjugado).

* **TP15 (Não-Convexo com Curvatura Extrema):**
  Apresenta alta não-linearidade e regiões com gradientes de magnitude severa. Partindo de $x_A^0 = (-1{,}2, 1{,}0)^T$, o Gradiente Clássico (**429 iterações**) e o **SR1** (**40 iterações**, redução superior a $10\times$) seguem o vale rumo a $(1, 1)^T$, enquanto o **Gradiente Conjugado ($\text{PR}^+$)** cruza a crista devido ao termo de momento $\beta_k$ e é capturado pela bacia simétrica em $(1, -1)^T$ (**92 iterações**). Ao refletir o ponto inicial para $x_B^0 = (1{,}2, -1{,}0)^T$, todos os três métodos convergem para a região próxima a $(1, -1)^T$ (**42 iterações** no SR1, **31** no Gradiente Conjugado e **399** no Gradiente Clássico), acionando o critério de parada por variação relativa da função objetivo (`Convergiu (f)`, $\frac{|f_{k+1}-f_k|}{\max(1,|f_k|)} \le 10^{-7}$).

### 1.3 Sequência de Iterandos
Para ilustrar a evolução espacial exigida no protocolo experimental, destacam-se os passos iniciais e finais capturados via `trajetoria_x`:

* **TP6 (SR1 / Gradiente Clássico):**
  * Partindo de $x_A^0$: $[-4{,}0000, -2{,}0000]^T \to [1{,}0000, 2{,}0000]^T \to [1{,}0000, 0{,}0000]^T$.
  * Partindo de $x_B^0$: $[4{,}0000, 2{,}0000]^T \to [1{,}0000, -2{,}0000]^T \to [1{,}0000, 0{,}0000]^T$.
* **TP12 (SR1 com Salvaguarda):**
  * Partindo de $x_A^0$: $[1{,}0000, 1{,}0000]^T \to \dots \to [3{,}0000, 2{,}0000]^T$ (8 passos).
  * Partindo de $x_B^0$: $[-1{,}0000, -1{,}0000]^T \to \dots \to [-3{,}7793, -3{,}2832]^T$ (10 passos).

---

## 2. Os 24 Experimentos

* **Gradiente Clássico vs. SR1 com Salvaguarda:** Nos problemas com bom condicionamento local (TP6 e TP12), ambos os métodos alcançam os minimizadores em poucas iterações (2 a 14 passos). Contudo, na presença de vales estreitos e mal-condicionados (TP7 e TP15), o Gradiente Clássico sofre degradação severa devido à ortogonalidade entre passos consecutivos, enquanto o SR1 utiliza a informação de curvatura acumulada para atingir convergência superlinear.
* **Comportamento do Gradiente Conjugado Polak-Ribière ($\text{PR}^+$):** O método apresentou desempenho intermediário entre o Gradiente Clássico e o SR1, destacando-se pela economia de memória (não armazena aproximações matriciais $n \times n$ da Hessiana). No TP7 ($x_A^0$) e no TP15 ($x_A^0$), reduziu drasticamente o esforço iterativo em comparação ao Gradiente Clássico (197 vs. 1000 iterações no TP7 e 92 vs. 429 no TP15). Entretanto, evidenciou sensibilidade ao uso da busca linear inexata de Armijo em vales estreitos e curvos (caso do TP7 refletido em $x_B^0$), onde a perda de ortogonalidade entre gradientes consecutivos comprometeu a conjugação das direções e provocou parada prematura pelo critério de variação relativa de $f$.

---

## 3. Conclusão

1. **Unicidade vs. Multiplicidade de Bacias:** Em problemas estritamente convexos (TP6), a reflexão $x_B^0 = -x_A^0$ preserva rigorosamente o ponto de convergência. Em funções multimodais não-convexas (TP12 e TP15), a simetria refletida desloca o iterando inicial (ou a trajetória com momento conjugado) para bacias de atração distintas, conduzindo a minimizadores em outros quadrantes.
2. **Efeito do Condicionamento ($\kappa$) no Gradiente Clássico:** O método da descida mais íngreme apresenta convergência rápida apenas quando $\kappa(\nabla^2 f) \approx 1$ (caso do TP6, $\kappa = 2$). Em vales estreitos (TP7), o ziguezague impede a convergência dentro do limite de $1000$ iterações.
3. **Eficiência do Quase-Newton SR1 com Salvaguarda:** A condição $|s_k^T (y_k - B_k s_k)| \ge r \|s_k\|_2 \|y_k - B_k s_k\|_2$ somada à verificação de direção de descida garantiu estabilidade numérica mesmo nas regiões não-convexas, sendo o único método a atingir $\|\nabla f(x_k)\|_2 \le 10^{-5}$ no TP7 e no TP12 (em no máximo 12 iterações) e reduzindo em $10\times$ o esforço computacional no TP15.
4. **Papel do Polak-Ribière ($\text{PR}^+$) e Busca Linear:** O gradiente conjugado acelera significativamente a descida em relação ao gradiente puro sem custo matricial, mas exige condições de busca linear mais rígidas (como Wolfe forte) para preservar a conjugação em problemas altamente não-lineares e mal-condicionados.
5. **Critérios de Parada e Reprodução:** O critério combinado ($\|\nabla f(x_k)\|_2 \le 10^{-5}$ ou variação relativa de $f \le 10^{-7}$) evitou laços infinitos em regiões de curvatura extrema, sinalizando explicitamente as paradas por estagnação relativa (`Convergiu (f)`). Toda a suíte é determinística, modularizada em `metodos/` e reprodutível via `python experimentos.py`.