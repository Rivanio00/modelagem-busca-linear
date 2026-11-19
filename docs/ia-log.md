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

## 3. Distribuição do uso por integrante

| Integrante | Principais usos de IA | Principais verificações feitas |
|------------|----------------------|--------------------------------|
| José Rivânio | Geração de Documentação e código a partir do código desenvolvido na etapa anterior, seguindo o padrão | Revisão e modificações do conteúdo
| Pedro Wagner | Uso de IA para verificar corretude de código e otimização da implementação| Verificação a partir do resultado esperado dos experimentos|