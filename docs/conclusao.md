# Resultados e Conclusão

Síntese das duas modelagens e dos 36 experimentos (4 problemas de teste × 3 direções × 3 métodos de busca 1D). Todos os valores vêm das execuções e da tabela dos experimentos.

---

## 1. Modelagens práticas

---

## 2. Os 36 experimentos

---

## 3. Conclusão

1. **Newton puro não é seguro.** Em 2 dos 4 problemas (TP12 e TP15), a partir do ponto inicial dado, $\mathbf{d}_N$ não é direção de descida. O Newton modificado resolve esses casos e é a melhor direção neles; nos demais, coincide com o Newton.
2. **Exata contra inexata.** Os métodos exatos (Fibonacci, Newton 1D) reduziram mais $f$ por passo em todos os casos, ao custo de mais avaliações. O Goldstein custa menos por passo, o que tende a compensar em problemas maiores, mas isso não foi testado aqui, já que todos os problemas têm poucas variáveis.
3. **Escolha do método 1D.** Newton 1D é rápido quando $\phi$ é bem comportada; o Fibonacci lidou melhor com o caso mais difícil (TP15/$\mathbf{d}_M$). Em ambos, a tolerância deve ser compatível com a escala de $\alpha^*$.
4. **Escala importa.** O mesmo princípio aparece no California Housing: sem normalizar os dados, o passo cai para $10^{-6}$.
5. **Reprodução.** As rotinas têm testes automatizados e os resultados saem dos scripts do repositório.