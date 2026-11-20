# Apêndice: Auditoria de Uso de Inteligência Artificial

Projeto Computacional 2: Resolução de problemas irrestritos com métodos de otimização multidimensionais
---

## 1. Visão geral do uso

**Integrantes:** José Rivânio e Pedro Wagner


| Ferramenta / modelo | Quem usou | Finalidades principais |
|---------------------|-----------|------------------------|
| Gemini | Rivânio | Correção de código e documentação |
| ChatGPT | Wagner | Verificação de cálculos e documentação |

---

## 2. Registro de prompts

Resumo das principais solicitações feitas aos modelos.

| # | Data | Quem | Ferramenta | Objetivo | Resumo do prompt | Resultado e uso | Como foi verificado |
|---|------|------|------------|----------|------------------|-----------------|---------------------|
| 1 | 14/11 | Rivânio | Gemini | Atualizar experimentos.py | Atualizar os experimentos, chamando os métodos do Gradiente e SR1, utilizando o experimentos.py do trabalho anterior como estrutura base | experimentos.py | Executando código e validando resultados dos métodos |
| 2 | 14/11 | Rivânio | Gemini | Atualizando README.md utilizando o anterior como estrutura base | Enviei o arquivo anterior, referente ao trabalho 1 e pedi pra atualizar seguindo as especificações do novo trabalho | README.md | Verificado pelos dois membros
| 3 | 15/11 | Rivânio | Gemini | Atualizando conclusao.md utilizando o anterior como estrutura base | Enviei o arquivo anterior, referente ao trabalho 1 e solicitei uma nova estrutura seguindo o que foi pedido nas especificações do trabalho | conclusao.md | Verificado e preenchido pelos membros com os resultados
| 4 | 15/11 | Rivânio | Gemini | Organizar o manual de uso para adaptações | Desenvolver um manual de uso para adicionar novos testes e alterar existentes | manual_de_uso.md | Corrigido com base no uso nos algoritmos
| 5 | 17/11 | Wagner | ChatGPT | Organizar a função de cálculo de Polak-Ribiere | Reorganizar a função que calcula o polak-ribiere e integrar ao algoritmo geral do gradiente conjugado | gradiente_conjugado.py | Baseado em um algoritmo anterior feito à mão

---

## 3. Auditoria Crítica de erros

Erro: Ausência de condição de parada por variação da função no algoritmo de Gradiente Conjugado

Integrante que identificou: Pedro Wagner

Contexto: Implementação e execução do algoritmo de Gradiente Conjugado para otimização irrestrita, durante a realização da bateria de testes com diferentes problemas e configurações.

Tipo de erro: Ausência de critério de convergência e encerramento inadequado da execução.

O que o modelo produziu:

O modelo gerou uma implementação do algoritmo de Gradiente Conjugado que não contemplava uma condição de parada baseada na variação do valor da função objetivo entre iterações consecutivas.

Consequentemente, o algoritmo dependia de outros critérios de encerramento, sem verificar adequadamente se a função objetivo havia atingido uma situação de estabilização. Isso comprometia a avaliação dos experimentos, especialmente nos casos em que o método se aproximava bastante da solução final, mas não satisfazia os critérios de parada existentes.

Por que está errado:

A ausência desse critério de parada prejudicava a identificação da convergência numérica do método. Em problemas de otimização irrestrita, além de verificar a norma do gradiente, é importante acompanhar a variação da função objetivo entre iterações consecutivas.

Uma condição adicional de convergência pode ser definida por:

$$|f(x_{k+1})-f(x_k)| < \varepsilon_f$$

em que $\varepsilon_f$ representa uma tolerância mínima para a variação da função objetivo.

Sem essa verificação, o algoritmo poderia continuar executando mesmo quando os valores da função já apresentavam variações numericamente insignificantes. Isso também dificultava a interpretação dos resultados da bateria de testes, fazendo com que diversos experimentos aparentassem apresentar problemas de convergência, embora já estivessem muito próximos do resultado final esperado.

Como foi detectado:

O erro foi identificado durante a execução e análise da bateria de testes do algoritmo de Gradiente Conjugado. Ao comparar os resultados obtidos com o comportamento esperado dos problemas, observou-se que algumas execuções não eram encerradas adequadamente, apesar de apresentarem valores da função objetivo muito próximos daqueles esperados para a solução final.

A análise da implementação revelou que não havia uma condição de parada responsável por verificar a variação da função objetivo entre iterações consecutivas.

Correção analítica:

A correção foi realizada manualmente, incorporando ao algoritmo uma condição adicional de parada baseada na variação absoluta da função objetivo entre duas iterações consecutivas

Com essa alteração, o algoritmo passou a considerar também a estabilização do valor da função objetivo como critério de convergência, complementando os demais critérios de parada já existentes.

Após a correção, a bateria de testes foi executada novamente. Os resultados obtidos apresentaram comportamento coerente com o esperado para os problemas avaliados, confirmando que diversas execuções anteriormente interpretadas como incorretas estavam, na realidade, muito próximas da convergência e apenas não possuíam um mecanismo adequado de encerramento.

## 4. Distribuição do uso por integrante

| Integrante | Principais usos de IA | Principais verificações feitas |
|------------|----------------------|--------------------------------|
| José Rivânio | Geração de Documentação e código a partir do código desenvolvido na etapa anterior, seguindo o padrão | Revisão e modificações do conteúdo
| Pedro Wagner | Uso de IA para verificar corretude de código e otimização da implementação| Verificação a partir do resultado esperado dos experimentos|