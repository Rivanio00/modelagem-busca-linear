# Manual de Uso — Suíte de Otimização Multidimensional Irrestrita

Este manual descreve a arquitetura de entrada e saída dos programas desenvolvidos, detalhando como configurar problemas, parametrizar os otimizadores e interpretar os resultados gerados. Para configurar e rodar o projeto basta seguir os passos definidos em `README.md`

---

## 1. Como Entrar com Dados

Todos os algoritmos multidimensionais estão centralizados no pacote `metodos` e aceitam qualquer instância compatível com a classe `Problema` (definida em `base.py`).

### 1.1 Assinatura Padrão dos Otimizadores

```python
import numpy as np
from problemas import TP6, TP7, TP12, TP15
from metodos import gradiente_classico, sr1

# Exemplo de execução com ponto inicial customizado e tolerâncias explícitas
resultado = sr1(
    p=TP7,                              # Instância de Problema (.f, .grad, .hess, .x0)
    x0=np.array([-15.0, 2.0]),          # Ponto inicial opcional (padrão: p.x0)
    tol_grad=1e-5,                      # Tolerância para ||grad f(x_k)||_2
    tol_f=1e-7,                         # Tolerância para variação relativa de f
    k_limit=1000,                       # Número máximo de iterações externas
    condicao_passo="armijo",            # Regra 1D de condicoes.py ("armijo", "goldstein", "wolfe")
)
```

### 1.2 Parâmetros de Entrada Disponíveis

| Parâmetro | Tipo | Padrão | Descrição |
| :--- | :--- | :--- | :--- |
| `p` | `Problema` | *(obrigatório)* | Objeto contendo os métodos `f(x)`, `grad(x)`, `hess(x)` e o vetor inicial `x0`. |
| `x0` | `np.ndarray` | `None` | Vetor unidimensional com o ponto de partida. Se `None`, utiliza `p.x0.copy()`. |
| `tol_grad` | `float` | `1e-5` | Limiar de parada para a norma Euclidiana do gradiente ($\|\nabla f(x_k)\|_2 \le \text{tol\_grad}$). |
| `tol_f` | `float` | `1e-7` | Limiar para variação relativa entre passos consecutivos da função objetivo. |
| `k_limit` | `int` | `1000` | Limite superior de iterações externas permitidas. |
| `condicao_passo` | `str` | `"armijo"` | Critério utilizado pela sub-rotina `achar_passo` (reaproveitada da Atividade 1). |
| `r_salvaguarda` | `float` | `1e-8` | *(Exclusivo do `sr1`)* Constante $r \in (0, 1)$ que impede denominadores nulos na atualização de posto 1. |

### 1.3 Definindo um Novo Problema Customizado

Para testar uma função própria $f: \mathbb{R}^n \to \mathbb{R}$, instancie a classe `Problema` de `base.py`:

```python
import numpy as np
from base import Problema
from metodos import sr1

meu_problema = Problema(
    nome="Quadrática Teste",
    f=lambda x: (x[0] - 2.0)**2 + 4.0 * (x[1] + 1.0)**2,
    grad=lambda x: np.array([2.0 * (x[0] - 2.0), 8.0 * (x[1] + 1.0)]),
    hess=lambda x: np.array([[2.0, 0.0], [0.0, 8.0]]),
    x0=np.array([0.0, 0.0]),
)

res = sr1(meu_problema)
```

---

## 2. Como Ler e Interpretar as Saídas

Cada chamada a `gradiente_classico`, `sr1` ou `polak_ribiere` retorna um dicionário Python (`dict`) estruturado conforme o contrato definido em `metodos/interfaces.md`:

```python
{
    "metodo": "SR1",
    "x_final": array([5., 4.]),
    "f_final": 1.925174e-16,
    "norma_grad": 1.2014e-06,
    "iteracoes": 12,
    "status": "Convergiu (Gradiente)",
    "trajetoria_x": [...],
    "trajetoria_f": [...]
}
```

### 2.1 Significado das Chaves de Retorno

* **`metodo` (`str`):** Nome identificador do algoritmo executado.
* **`x_final` (`np.ndarray`):** Coordenadas do último iterando $x_k$ alcançado.
* **`f_final` (`float`):** Valor escalar da função objetivo avaliada em $x_{\text{final}}$.
* **`norma_grad` (`float`):** Norma Euclidiana $\|\nabla f(x_{\text{final}})\|_2$ no ponto de parada.
* **`iteracoes` (`int`):** Quantidade total de passos externos executados até a interrupção.
* **`trajetoria_x` (`list[np.ndarray]`):** Sequência completa $[x_0, x_1, \dots, x_k]$ percorrida pelo método, utilizada para inspecionar saltos entre quadrantes e bacias de atração.
* **`trajetoria_f` (`list[float]`):** Histórico escalar $[f(x_0), f(x_1), \dots, f(x_k)]$ da evolução da função objetivo.

### 2.2 Códigos de Status de Convergência (`status`)

1. **`"Convergiu (Gradiente)"`**: Sucesso pleno — o algoritmo atingiu um ponto estacionário com $\|\nabla f(x_k)\|_2 \le 10^{-5}$.
2. **`"Convergiu (f)"`**: Parada por estagnação relativa — a variação $\frac{|f(x_{k+1}) - f(x_k)|}{\max(1, |f(x_k)|)}$ tornou-se $\le 10^{-7}$ antes que o gradiente atingisse $10^{-5}$ (comum em vales muito estreitos com passos minúsculos).
3. **`"Max Iter"`**: O algoritmo atingiu o teto de $1000$ iterações sem satisfazer as tolerâncias (indica lentidão severa por mal-condicionamento, como o ziguezague do Gradiente Clássico no TP7).
4. **`"Falha (...)"`**: Interrupção segura caso a busca linear não encontre passo válido ou ocorra instabilidade numérica (`NaN`/`Inf`).