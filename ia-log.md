# Apêndice: Auditoria de Uso de Inteligência Artificial

Projeto Computacional 1: Modelagem e Busca Linear
---

## 1. Visão geral do uso

**Integrantes:** José Rivânio e Pedro Wagner

**Ferramentas utilizadas:**

| Ferramenta / modelo | Quem usou | Finalidades principais |
|---------------------|-----------|------------------------|
| Claude | Rivânio | Verificação de cálculos e documentação |
| ChatGPT | Wagner | Verificação de cálculos e documentação |
| [ex.: GitHub Copilot] | [A / B] | [ex.: autocompletar código] |

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

---

## 3. Auditoria crítica de erros

O enunciado exige documentar **pelo menos uma** situação em que o modelo gerou formulação equivocada, derivada parcial incorreta ou bug de implementação (ex.: laço infinito na busca linear, violação de descida), explicando como a equipe identificou e corrigiu o erro **analiticamente**.

Copiem o bloco abaixo para cada erro encontrado.

### Erro 1: [título curto, ex.: "Derivada incorreta de f₁₅"]

- **Integrante que identificou:** [A / B]
- **Contexto:** [O que foi pedido ao modelo e a qual parte do trabalho se refere]
- **Tipo de erro:** [ ] Formulação matemática  [ ] Derivada  [ ] Bug de implementação  [ ] Violação de descida  [ ] Outro: ____

**O que o modelo produziu:**

```text
[cole aqui o trecho de código ou a fórmula gerada incorretamente]
```

Em LaTeX, se for fórmula:

$$
[fórmula incorreta]
$$

**Por que está errado:** [explicação matemática, não apenas "deu erro"]

**Como foi detectado:** [o teste ou a verificação que revelou o problema, ex.: comparação com diferenças finitas, ∇f(x⁰)ᵀd ≥ 0 inesperado, execução que não termina]

**Correção analítica:**

$$
[dedução correta, passo a passo]
$$

**Verificação após a correção:** [o teste que agora passa, com valores numéricos se possível]

---

### Erro 2: [título curto]

*(copiar o bloco acima)*

---

## 4. Reflexão sobre o uso de IA

Parágrafo curto e honesto sobre o que a IA ajudou, onde atrapalhou e o que a dupla aprendeu ao auditá-la.

[Escrever ao final do projeto.]

---

## 5. Distribuição do uso por integrante

*(Conecta com a Matriz de Responsabilidades do relatório.)*

| Integrante | Principais usos de IA | Principais verificações feitas |
|------------|----------------------|--------------------------------|
| José Rivânio | | |
| Pedro Wagner | Uso de IA para verificar corretude de cálculos extensos | Verificação de cálculos de gradientes e hessianas, de complexidade e de autovalores|