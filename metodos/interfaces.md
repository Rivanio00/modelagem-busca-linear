# Contrato de Interfaces

## 1. Módulos Previstos na Pasta `metodos/`

* `metodos/__init__.py` — Exporta as funções principais dos três otimizadores.
* `metodos/gradiente.py` — Método do Gradiente Clássico (Descida Mais Íngreme / Baseline).
* `metodos/sr1.py` — Método Quase-Newton SR1 (Symmetric Rank-1) com Salvaguarda.
* `metodos/polak_ribiere.py` — Método do Gradiente Conjugado Não-Linear Polak-Ribière ($\text{PR}^+$).

---

## 2. Assinatura Padrão das Funções

Cada módulo deve expor uma função principal seguindo exatamente os mesmos parâmetros de entrada e valores padrão:

```python
import numpy as np
from typing import Callable, Dict, Any

def otimizar_metodo(
    problema: Any,
    x0: np.ndarray,
    busca_linear_fn: Callable,
    tol_grad: float = 1e-5,
    tol_f: float = 1e-7,
    max_iter: int = 1000
) -> Dict[str, Any]:
```

### Descrição dos Parâmetros
1. **`problema`**: Instância da classe `Problema` (definida em `base.py`), fornecendo `problema.f(x)` e `problema.grad(x)`.
2. **`x0`**: Vetor `np.ndarray` unidimensional (`dtype=float`) representando o ponto inicial ($x_A^0$ ou $x_B^0 = -x_A^0$). **Importante:** Sempre fazer `x = x0.astype(float).copy()` no início para não mutar o array original passado por referência.
3. **`busca_linear_fn`**: Função de busca linear 1D reaproveitada da Atividade 1 (ex.: `fibonacci` ou `armijo`/`goldstein`) encarregada de encontrar o passo $\alpha_k > 0$ ao longo da direção $d_k$.
4. **`tol_grad`**: Tolerância para a norma euclidiana do gradiente ($10^{-5}$).
5. **`tol_f`**: Tolerância para a variação relativa da função objetivo ($10^{-7}$).
6. **`max_iter`**: Limite máximo de iterações externas ($1000$).

---

## 3. Estrutura Obrigatória do Dicionário de Retorno

Todas as funções devem retornar um `dict` contendo exatamente as seguintes 8 chaves:

```python
{
    "metodo": str,              # Nome legível: "Gradiente Clássico", "SR1" ou "Polak-Ribière (PR+)"
    "x_final": np.ndarray,      # Ponto final x_k encontrado
    "f_final": float,           # Valor escalar de f(x_final)
    "norma_grad": float,        # Norma L2 do gradiente final: np.linalg.norm(grad_k)
    "iteracoes": int,           # Número total de iterações realizadas (k)
    "status": str,              # Motivo exato da parada (ver Seção 4)
    "trajetoria_x": list,       # Lista de np.ndarray [x_0, x_1, ..., x_k] para análise de bacias
    "trajetoria_f": list        # Lista de floats [f(x_0), f(x_1), ..., f(x_k)] para curvas de convergência
}
```

---

## 4. Critérios de Parada e Strings de Status

A convergência deve ser avaliada a cada iteração $k$ na seguinte ordem de prioridade, utilizando exatamente as strings de `status` padronizadas abaixo:

1. **Critério do Gradiente (Estacionariedade):**
   $$\|\nabla f(x_k)\|_2 \le 10^{-5}$$
   * `status = "Convergiu (Gradiente)"`

2. **Critério de Variação Relativa da Função (Após calcular $x_{k+1}$):**
   $$\frac{|f(x_{k+1}) - f(x_k)|}{\max(1, |f(x_k)|)} \le 10^{-7}$$
   * `status = "Convergiu (f)"`

3. **Limite de Iterações:**
   $$k \ge 1000$$
   * `status = "Max Iter"`

4. **Falha Numérica / Divergência (ex.: `NaN`, `Inf` ou falha na busca linear):**
   * `status = "Falha"` (interrompe o laço de forma segura sem quebrar a bateria de testes).

---

## 5. Diretrizes Específicas de Implementação

### 5.1 Polak-Ribière ($\text{PR}^+$) — 
* **Direção inicial ($k=0$):** $d_0 = -\nabla f(x_0)$.
* **Parâmetro $\beta_k$ ($k \ge 1$):**
  $$\beta_k^{PR} = \frac{g_{k+1}^T (g_{k+1} - g_k)}{\|g_k\|_2^2}$$
* **Reinício Automático ($\text{PR}^+$):** Caso $\beta_k^{PR} < 0$, adotar $\beta_k = \max(0, \beta_k^{PR}) = 0$, o que reinicia automaticamente a direção para o gradiente negativo ($d_{k+1} = -g_{k+1}$).
* **Salvaguarda de Descida:** Caso por erro numérico $g_{k+1}^T d_{k+1} \ge 0$, forçar $d_{k+1} = -g_{k+1}$.

### 5.2 SR1 com Salvaguarda —
* **Inicialização:** $B_0 = I$ (matriz identidade $n \times n$).
* **Direção de busca:** Resolver o sistema linear $B_k d_k = -g_k$. Se $g_k^T d_k \ge 0$ ou $B_k$ for mal-condicionada/singular, adotar $d_k = -g_k$ e reiniciar $B_k = I$.
* **Condição de Salvaguarda:** Definindo $s_k = x_{k+1} - x_k$ e $y_k = g_{k+1} - g_k$, atualizar a matriz apenas se:
  $$\left| s_k^T (y_k - B_k s_k) \right| \ge r \|s_k\|_2 \|y_k - B_k s_k\|_2, \quad \text{com } r = 10^{-8}$$
  Caso contrário, manter $B_{k+1} = B_k$.