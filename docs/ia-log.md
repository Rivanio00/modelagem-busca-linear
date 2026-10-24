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
| 10 | 22/10 | Rivânio | Claude | Organizar os resultados dos experimentos em um .md | Ao final da execução de experimentos.py salvar os resultados num markdown, organizado em uma tabela| tabela_36_experimentos.md | Verificando com a saída do terminal |
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

---

## 4. Reflexão sobre o uso de IA

O uso de LLM's acelerou bastante a realização do trabalho e a execuções de tarefas repetitivas, como um exemplo o desenvovimento de problemas.md que seria bem trabalhoso de realizar devido a sua formatação e organização, todos os arquivos de documentação ou são gerados por LLM e sofrem alterações ou são gerados como formulário a ser preenchido pelos desenvolvedores, facilitando todo o processo de documentação. Para a verificação de cálculos é também muito útil, toda a etapa que calculamos o gradiente e hessiana foi verificada com LLM's, a partir do nosso desenvolvimento e da pesquisa conseguimos validar os cálculos. Para código, o maior benefício foi o desenvolvimentos de testes, que nos ajudaram a sempre que uma nova funcionalidade era implementada, poderíamos verificar a sua corretude. O resultado que tivemos utilizando as LLM's é muito bom, sem o uso dessas ferramentas teríamos mais dificuldades, o trabalho levaria mais tempo. Mas o nosso aprendizado seria maior? Essas ferramentas nos prejudicam a longo prazo? A resposta é o equilíbrio, sem ele ainda seremos programadores?

---

## 5. Distribuição do uso por integrante

| Integrante | Principais usos de IA | Principais verificações feitas |
|------------|----------------------|--------------------------------|
| José Rivânio | Geração de Documentação a partir do código desenvolvido e desenvolvimento de testes | Revisão e modificações do conteúdo
| Pedro Wagner | Uso de IA para verificar corretude de cálculos extensos | Verificação de cálculos de gradientes e hessianas, de complexidade e de autovalores|