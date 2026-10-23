from pathlib import Path
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from base import Problema
from condicoes import armijo

# ============================================================
# 1. CARREGAMENTO E PREPARAÇÃO DOS DADOS
# ============================================================

# Define o caminho do CSV na mesma pasta deste arquivo .py
DATA_DIR = Path(__file__).resolve().parent
csv_path = DATA_DIR / "housing.csv"

if not csv_path.is_file():
  print("\n" + "=" * 75)
  print("[AVISO] O arquivo 'housing.csv' não foi encontrado!")
  print(
      "Lembre-se de baixar o arquivo CSV pelo link disponibilizado no PNL_modelagem_trabalho.pdf"
  )
  print(
      f"e salvá-lo nesta mesma pasta para poder rodar a modelagem!"
  )
  print("=" * 75 + "\n")
  sys.exit(1)

data = np.genfromtxt(csv_path, delimiter=",", dtype=float, skip_header=1)

R = data[:, 7]  # Variável independente
V = data[:, 8]  # Variável dependente


# ============================================================
# 2. DEFINIÇÃO DA FUNÇÃO OBJETIVO
# ============================================================

def fcal(W):
    """Calcula o erro quadrático total dividido por 2."""
    residuo = V - W[0] - W[1] * R
    return 0.5 * np.sum(residuo**2)


def gradcal(W):
    """Calcula o gradiente da função objetivo."""
    residuo = V - W[0] - W[1] * R

    return np.array([
        -np.sum(residuo),
        -np.sum(R * residuo)
    ])


def hesscal(W):
    """Calcula a matriz Hessiana da função objetivo."""
    return np.array([
        [len(R), np.sum(R)],
        [np.sum(R), np.sum(R**2)]
    ])


# ============================================================
# 3. INICIALIZAÇÃO DO PROBLEMA
# ============================================================

W0 = np.array([1.0, 1.0])

Cal = Problema(
    nome="California Housing",
    f=fcal,
    grad=gradcal,
    hess=hesscal,
    x0=W0.copy()
)


# ============================================================
# 4. CÁLCULO DA DIREÇÃO E BUSCA LINEAR DE ARMIJO
# ============================================================

gradiente = Cal.grad(W0)

# Direção oposta ao gradiente: direção de máxima descida local.
d = -gradiente

# Busca linear para determinar o tamanho do passo.
alpha, *_ = armijo(
    Cal,
    W0,
    gradiente,
    d,
    Cal.hess(W0),
    1.0,    # Passo inicial
    0.5,    # Fator de redução
    1e-4,   # Parâmetro de Armijo
    100     # Limite de iterações da busca
)


# ============================================================
# 5. ATUALIZAÇÃO DOS PARÂMETROS
# ============================================================

W = W0 + alpha * d

f_inicial = fcal(W0)
f_final = fcal(W)
reducao = f_inicial - f_final


# ============================================================
# 6. EXIBIÇÃO DOS RESULTADOS
# ============================================================

print("=" * 60)
print("       OTIMIZAÇÃO IRRESTRITA — CALIFORNIA HOUSING")
print("=" * 60)

print("\n[1] PONTO INICIAL")
print(f"    W₀ = {np.array2string(W0, precision=6)}")
print(f"    f(W₀) = {f_inicial:.6f}")

print("\n[2] GRADIENTE E DIREÇÃO DE BUSCA")
print(f"    ∇f(W₀) = {np.array2string(gradiente, precision=6)}")
print(f"    d      = {np.array2string(d, precision=6)}")
print(f"    ||∇f(W₀)||₂ = {np.linalg.norm(gradiente):.6f}")

print("\n[3] BUSCA LINEAR DE ARMIJO")
print(f"    Passo encontrado (α) = {alpha:.10f}")

print("\n[4] ATUALIZAÇÃO DOS PARÂMETROS")
print("    W₁ = W₀ + αd")
print(f"    W₁ = {np.array2string(W, precision=6)}")

print("\n[5] RESULTADO DA OTIMIZAÇÃO")
print(f"    Função inicial : {f_inicial:.6f}")
print(f"    Função final   : {f_final:.6f}")
print(f"    Redução        : {reducao:.6f}")

if f_inicial != 0:
    percentual = 100 * reducao / abs(f_inicial)
    print(f"    Redução percentual: {percentual:.6f}%")

print("\n" + "=" * 60)

