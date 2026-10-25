# Apêndice: Auditoria de Uso de Inteligência Artificial

Projeto Computacional 1: Modelagem e Busca Linear
---

## 1. Visão geral do uso

**Integrantes:** José Rivânio e Pedro Wagner


| Ferramenta / modelo | Quem usou | Finalidades principais |
|---------------------|-----------|------------------------|
| Claude | Rivânio | Verificação de cálculos e documentação |
| ChatGPT | Wagner | Verificação de cálculos e documentação |

---

## 2. Registro de prompts

Resumo das principais solicitações feitas aos modelos.

| # | Data | Quem | Ferramenta | Objetivo | Resumo do prompt | Resultado e uso | Como foi verificado |
|---|------|------|------------|----------|------------------|-----------------|---------------------|
| 1 | 10/10 | Rivânio | Claude | Gradiente e Hessiana do TP6,TP12 | Conferindo ∇f e ∇²f das funções que foram calculadas à mão e gerando um .md documentando o resultado | problemas.md | Calculo feito à mão |
| 2 | 10/10 | Rivânio | Claude | Documentação dos prompts | Gerar um arquivo .md que será usado como teamplate para registar o uso de LLM's | ia-log.md | Documento foi revisado e alterado pelos membros |
| 3 | 12/10 | Rivânio | Calude | Aprimoramento dos testes | Avalie os testes desenvolvidos, adicione outputs no terminal durante a execução e pontue problemas na implementação | testes/__main__.py| Testes foram avaliados e executados, comparando a execução correta |
| 4 | 13/10 | Wagner | ChatGPT | Verificação e tradução dos cálculos do gradiente e da Hessiana | Verificação dos cálculos feitos a mão dos gradientes e das hesssianas do TP7 e o TP15 e tradução das expressões matemáticas para código python| problemas.py | cálculos verificados à mão
| 5 | 13/10 | Wagner | ChatGPT | Verificação de convexidade das funções e se as hessianas eram definidas positivas | Verificação das contas feitas à mão que checavam se as funções eram convexas e se as matrizes hessianas eram definidas positivas| problemas.md | cálculos verificados à mão
| 6 | 16/10 | Wagner | ChatGPT | Correção do uso de backtracking para a condição de armijo | Correção do código usando backtracking para achar um passo que satisfaça a condição de armijo | condicoes.py | Código base feito manualmente
| 7 | 17/10 | Wagner | ChatGPT | Compleção do código da condição de Wolfe | Complementação do código base já feito para achar um tamanho de passo usando as condições de wolfe | as funções Wolfe e condicoes_wolfe | Código base feito manualmente |
| 8 | 21/10 | Rivânio | Claude | Desenvolvimento do Critério de Kelly(mdoelagem de problema prático) | Desenvolvimento de documentação, formulação a partir de fontes(rerenciadas em Kelly_bet.md) e cálculos de Gradiente e Hessiana  | Kelly_bet.md | Pesquisa Bibliográfica |
| 9 | 21/10 | Rivânio | Claude | Organização do código e do output no terminal | Aprimorar o código em kelly_bet.py, adicionando mais comentários e organizando a etapa final de output no terminal | kelly_bet.py | Comparando resultados com cálculo analítico |
| 10 | 21/10 | Wagner | ChatGPT | Verificação da derivação da função objetivo da regressão linear | Verificação dos cálculos e da derivação da função objetivo do problema de regressão linar, usando máxima verossimilhança gaussiana  | .PNL_modelagem_trabalho.pdf | Cálculos verificados na mão |
| 11 | 21/10 | Wagner | ChatGPT | Organização de código da última etapa | Aprimorar o código em california_problema.py, adicionando mais comentários e organizando a etapa final de output no terminal | california_problema.py | Comparando os resultados com código manualmente feito anteriormente |
| 12 | 22/10 | Rivânio | Claude | Organizar os resultados dos experimentos em um .md | Ao final da execução de experimentos.py salvar os resultados num markdown, organizado em uma tabela| tabela_36_experimentos.md | Verificando com a saída do terminal |
---

## 3. Auditoria crítica de erros

### Erro 1: Propagação de NaN por omissão de cabeçalho no dataset California Housing

- **Integrante que identificou:** José Rivânio
- **Contexto:** Carregamento de dados reais do arquivo `housing.csv` via `numpy.genfromtxt` e execução da Busca Linear de Armijo na modelagem do problema do California Housing (`california_problema.py`).
- **Tipo de erro:** `[ ]` Formulação matemática  `[ ]` Derivada  `[X]` Bug de implementação  `[ ]` Violação de descida  `[X]` Outro: Propagação de valores indefinidos (NaN) e estouro de exceção em tempo de execução

**O que o modelo produziu:**

```python
# O código gerado lia o CSV sem tratar o cabeçalho com strings
data = np.genfromtxt(csv_path, delimiter=",", dtype=float)

R = data[:, 7]  # Variável independente
V = data[:, 8]  # Variável dependente
```

**Por que está errado:** 

O arquivo `housing.csv` possui uma primeira linha contendo o cabeçalho textual das colunas (`longitude,latitude,...`). Ao executar `np.genfromtxt` com `dtype=float` sem omitir essa linha, o NumPy tenta converter texto em número e preenche a primeira linha do array com `np.nan`. 

A presença desse `NaN` propaga-se por todas as operações aritméticas subsequentes:
1. O resíduo $V - W_0 - W_1 R$ resulta em um vetor contendo `NaN`.
2. A função objetivo $f(W_0) = \frac{1}{2} \sum \text{resíduo}^2$ avalia para `NaN`.
3. O gradiente $\nabla f(W_0)$ resulta em $[\text{NaN}, \text{NaN}]^T$.

Ao entrar no laço da Busca Linear de Armijo em `condicoes.py`, a verificação do decréscimo suficiente avalia a desigualdade:

$$f(W_0 + \alpha d) \le f(W_0) + c \cdot \alpha \cdot \nabla f(W_0)^T d \implies \text{NaN} \le \text{NaN}$$

No Python/NumPy, qualquer comparação de ordem com `NaN` avalia estritamente como `False`. Consequentemente, o algoritmo reduz o passo $\alpha$ iterativamente até esgotar o limite (`limit=100`) sem jamais satisfazer a condição, lançando a exceção `RuntimeError: A busca de Armijo não encontrou um passo válido.`.

**Como foi detectado:** 

O erro foi detectado ao executar o script no terminal com o comando `python modelagem/california/california_problema.py`, que falhou e exibiu o *traceback*:

```text
File ".../condicoes.py", line 33, in armijo
    raise RuntimeError("A busca de Armijo não encontrou um passo válido.")
RuntimeError: A busca de Armijo não encontrou um passo válido.
```

**Correção analítica:**

A correção exigiu duas etapas: tratar a leitura do cabeçalho no código de E/S e ajustar a escala das variáveis reais para estabilidade numérica.

1. **Tratamento do Cabeçalho no CSV:**
   O parâmetro `skip_header=1` foi adicionado à leitura do arquivo:
   ```python
   data = np.genfromtxt(csv_path, delimiter=",", dtype=float, skip_header=1)
   ```

2. **Ajuste de Escala (Normalização):**
   Como $V$ representa valores de imóveis na ordem de centenas de milhares, o gradiente inicial $\nabla f(W_0)$ sem escala atingia magnitudes da ordem de $10^9$. Aplicou-se a normalização:
   $$R = \frac{R}{\max(R)}, \quad V = \frac{V}{100.000}$$

**Verificação após a correção:**

Após a inclusão de `skip_header=1` e do ajuste de escala, o script executou sem exceções. O gradiente $\nabla f(W_0)$ passou a ser numérico e bem-condicionado, e a busca de Armijo encontrou um passo válido $\alpha = 0{,}001$ logo na 1ª iteração, reduzindo a função de custo $f(W_0)$ de $1256{,}00$ para $136{,}12$ ($89{,}16\%$ de redução).

### Erro 2: Derivação incorreta da função de custo gaussiana por omissão do fator \(1/2\)

- **Integrante que identificou:** Wagner
- **Contexto:** Dedução da função de custo a partir da verossimilhança gaussiana para o problema de regressão linear simples, seguida do cálculo do gradiente e da Hessiana utilizados no método de Newton com busca linear.
- **Tipo de erro:** `[ ]` Formulação matemática  `[X]` Derivada  `[ ]` Bug de implementação  `[ ]` Violação de descida  `[X]` Outro: Inconsistência na função objetivo e alteração do comportamento de convergência do método de otimização.

**O que o modelo produziu:**

Ao derivar a função de custo a partir da verossimilhança gaussiana, a LLM desconsiderou o fator constante \(1/2\) que multiplicava a soma dos erros quadráticos. Para os resíduos definidos por \(u_i(W)=v_i-w_0-w_1r_i\), a função objetivo correta, desconsiderando termos constantes independentes de \(W\), é:

\[
f(W)=\frac{1}{2}\sum_{i=1}^{n}
(v_i-w_0-w_1r_i)^2.
\]

Entretanto, a derivação apresentada pela LLM correspondeu à função:

\[
\widetilde{f}(W)=\sum_{i=1}^{n}
(v_i-w_0-w_1r_i)^2.
\]

Consequentemente, as expressões obtidas para o gradiente e a Hessiana também ficaram incorretas em relação à função objetivo originalmente definida:

\[
\nabla \widetilde{f}(W)=2\nabla f(W),
\]

\[
\nabla^2\widetilde{f}(W)=2\nabla^2 f(W).
\]

**Por que está errado:**

O fator \(1/2\) não pode ser omitido durante a derivação sem que a função objetivo seja explicitamente redefinida e as consequências dessa alteração sejam consideradas. Embora multiplicar uma função por uma constante positiva preserve seus minimizadores e sua convexidade, isso não significa que as expressões da função, do gradiente e da Hessiana permaneçam iguais.

Nesse caso, a LLM produziu derivadas correspondentes a uma função de custo diferente daquela estabelecida na modelagem. Isso comprometeu a consistência matemática entre a função objetivo implementada e as derivadas utilizadas pelo algoritmo de otimização.

Além disso, a alteração pode afetar o comportamento de convergência do método, especialmente quando se utiliza uma busca linear com condições de aceitação de passo, como Armijo, Wolfe ou Goldstein, pois essas condições dependem dos valores da função objetivo e de suas derivadas. A utilização de expressões incompatíveis entre si pode levar a avaliações incorretas dos passos candidatos e prejudicar o funcionamento esperado do algoritmo.

**Como foi detectado:**

O erro foi identificado por Wagner durante a revisão matemática da modelagem. Ao refazer manualmente os cálculos das derivadas parciais, do gradiente e da Hessiana, ele percebeu que os resultados apresentados pela LLM continham um fator multiplicativo \(2\) em relação às expressões corretas. A divergência foi rastreada até a omissão do fator \(1/2\) na função de custo derivada da verossimilhança gaussiana.

**Correção analítica:**

A correção consistiu em retomar a função objetivo com o fator \(1/2\) e recalcular manualmente o gradiente e a Hessiana, garantindo a correspondência entre a função minimizada e suas derivadas.

1. **Função objetivo corrigida:**

   \[
   f(W)=\frac{1}{2}\sum_{i=1}^{n}
   (v_i-w_0-w_1r_i)^2.
   \]

2. **Gradiente corrigido:**

   Definindo \(u_i(W)=v_i-w_0-w_1r_i\), obtém-se:

   \[
   \nabla f(W)=
   \begin{bmatrix}
   -\displaystyle\sum_{i=1}^{n}u_i(W)\\[6pt]
   -\displaystyle\sum_{i=1}^{n}r_i u_i(W)
   \end{bmatrix}.
   \]

3. **Hessiana corrigida:**

   \[
   \nabla^2 f(W)=
   \begin{bmatrix}
   n & \displaystyle\sum_{i=1}^{n}r_i\\[6pt]
   \displaystyle\sum_{i=1}^{n}r_i &
   \displaystyle\sum_{i=1}^{n}r_i^2
   \end{bmatrix}.
   \]

**Verificação após a correção:**

Após a revisão manual, a função objetivo, o gradiente e a Hessiana passaram a ser matematicamente consistentes entre si. A Hessiana corrigida é semidefinida positiva, sendo definida positiva quando as variáveis independentes apresentam variabilidade suficiente para que as duas colunas da matriz de projeto sejam linearmente independentes. Portanto, a função de mínimos quadrados permanece convexa.

A correção também restabeleceu a formulação pretendida para o método de Newton e sua busca linear. É importante observar que, se o fator \(2\) tivesse sido aplicado uniformemente à função, ao gradiente e à Hessiana, o passo puro de Newton seria matematicamente invariável, pois o fator se cancelaria em \(-(\nabla^2 f)^{-1}\nabla f\). O problema identificado foi a inconsistência da derivação em relação à função objetivo definida, que poderia afetar a busca linear caso as expressões incorretas fossem utilizadas de maneira incompatível na implementação.


---

## 4. Reflexão sobre o uso de IA

O uso de LLM's acelerou bastante a realização do trabalho e a execuções de tarefas repetitivas, como um exemplo o desenvovimento de problemas.md que seria bem trabalhoso de realizar devido a sua formatação e organização, todos os arquivos de documentação ou são gerados por LLM e sofrem alterações ou são gerados como formulário a ser preenchido pelos desenvolvedores, facilitando todo o processo de documentação. Para a verificação de cálculos é também muito útil, toda a etapa que calculamos o gradiente e hessiana foi verificada com LLM's, a partir do nosso desenvolvimento e da pesquisa conseguimos validar os cálculos. Para código, o maior benefício foi o desenvolvimentos de testes, que nos ajudaram a sempre que uma nova funcionalidade era implementada, poderíamos verificar a sua corretude. O resultado que tivemos utilizando as LLM's é muito bom, sem o uso dessas ferramentas teríamos mais dificuldades, o trabalho levaria mais tempo. Mas o nosso aprendizado seria maior? Essas ferramentas nos prejudicam a longo prazo? A resposta é o equilíbrio, sem ele ainda seremos programadores?

---

## 5. Distribuição do uso por integrante

| Integrante | Principais usos de IA | Principais verificações feitas |
|------------|----------------------|--------------------------------|
| José Rivânio | Geração de Documentação a partir do código desenvolvido e desenvolvimento de testes | Revisão e modificações do conteúdo
| Pedro Wagner | Uso de IA para verificar corretude de cálculos extensos | Verificação de cálculos de gradientes e hessianas, de complexidade e de autovalores|