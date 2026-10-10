# Apêndice: Auditoria de Uso de Inteligência Artificial

Projeto Computacional 1: Modelagem e Busca Linear
---

## 1. Visão geral do uso

**Integrantes:** José Rivânio e Pedro Wagner

**Ferramentas utilizadas:**

| Ferramenta / modelo | Quem usou | Finalidades principais |
|---------------------|-----------|------------------------|
| Claude | Rivânio | Verificação de cálculos e documentação |
| [ex.: GitHub Copilot] | [A / B] | [ex.: autocompletar código] |

---

## 2. Registro de prompts

Resumo das principais solicitações feitas aos modelos.

| # | Data | Quem | Ferramenta | Objetivo | Resumo do prompt | Resultado e uso | Como foi verificado |
|---|------|------|------------|----------|------------------|-----------------|---------------------|
| 1 | 10/10 | Rivânio | Claude | Gradiente e Hessiana do TP6 e do TP12 | Conferindo ∇f e ∇²f das funções que foram calculadas à mão e gerando um .md documentando o resultado | problemas.md | Calculo feito à mão |
| 2 | 10/10 | Rivânio | Claude | Documentação dos prompts | Gerar um arquivo .md que será usado como teamplate para registar o uso de LLM's | ia-log.md | Documento foi revisado e alterado pelos membros |
| 3 | | | | | | | |
| 4 | | | | | | | |

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
| Pedro Wagner | | |