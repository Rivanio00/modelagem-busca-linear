from pathlib import Path
import sys
import numpy as np

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
if str(ROOT_DIR) not in sys.path:
  sys.path.append(str(ROOT_DIR))

from busca_linear.fibonacci import busca_fibonacci

# Parâmetros e dados do mercado (4 Cenários e 2 Ativos)
p = np.array([0.35, 0.35, 0.20, 0.10])

# Matriz de Retornos R [4 cenários x 2 ativos]
R = np.array([
    [ 0.30,  0.50],  # Cenário 1: Expansão Forte do Mercado
    [ 0.10, -0.20],  # Cenário 2: Crescimento Seletivo (Ativo 1)
    [-0.15,  0.40],  # Cenário 3: Rotação de Capital (Ativo 2)
    [-0.25, -0.30]   # Cenário 4: Recessão / Retração Geral
])

# Função objetivo (definida no domínio D = {x : 1 + R_s^T x > 0 para todo s})
def f_kelly(x):
    """Função Custo: -E[ln(1 + R @ x)] (Minimização do log negativo da riqueza)."""
    W = 1.0 + R @ x
    if np.any(W <= 1e-12):
        # Fora de D: f -> +inf. Ao longo do raio x0 + alpha*d a região viável é
        # [0, alpha_max), então o "muro" fica sempre à direita e o Fibonacci
        # recua corretamente (comparações inf > inf caem no ramo do else).
        return 1e9
    return -np.sum(p * np.log(W))

def grad_kelly(x):
  r"""Vetor Gradiente: grad f(x) = -\sum (p_s / W_s) * R_s."""
  W = 1.0 + R @ x
  pesos = p / W
  return -R.T @ pesos


def hess_kelly(x):
  r"""Matriz Hessiana: hess f(x) = \sum (p_s / W_s^2) * (R_s R_s^T)."""
  W = 1.0 + R @ x
  pesos = p / (W**2)
  return R.T @ (pesos[:, None] * R)  # forma vetorizada de sum_s pesos_s * R_s R_s^T


def checar_gradiente(x, h=1e-6):
  """Compara o gradiente analítico com diferenças finitas centrais."""
  g_fd = np.zeros_like(x)
  for i in range(len(x)):
    e = np.zeros_like(x)
    e[i] = h
    g_fd[i] = (f_kelly(x + e) - f_kelly(x - e)) / (2 * h)
  return np.linalg.norm(g_fd - grad_kelly(x))


def passo_busca_linear(x):
  """Um passo de máxima descida com busca linear de Fibonacci a partir de x."""
  g = grad_kelly(x)
  d = -g  # Direção do Gradiente Negativo (descida mais íngreme)

  # Função unidimensional phi(alpha), com contador de avaliações
  n_aval = [0]
  def phi(alpha):
    n_aval[0] += 1
    return f_kelly(x + alpha * d)

  # Execução da busca linear utilizando o teu módulo de Fibonacci
  alpha_star, info = busca_fibonacci(phi)
  return x + alpha_star * d, alpha_star, d, n_aval[0], info


def fmt_x(x):
  return f"[{x[0]*100:.2f}%, {x[1]*100:.2f}%]"


def main():
  # EXECUÇÃO DO 1º PASSO
  # Ponto inicial conservador: x0 = [10%, 10%] em ativos, 80% em caixa
  x0 = np.array([0.10, 0.10])
  f0 = f_kelly(x0)
  g0 = grad_kelly(x0)
  H0 = hess_kelly(x0)

  x1, alpha_star, d0, n_aval, info = passo_busca_linear(x0)
  f1 = f_kelly(x1)

  # Autovalores para verificação de convexidade estrita (conferência local;
  # a prova global está na seção 4.3 do .md)
  autovalores_H0 = np.linalg.eigvalsh(H0)
  pd_ok = bool(np.all(autovalores_H0 > 0))
  descida = float(np.dot(g0, d0))

  # CONVERGÊNCIA: repete máxima descida + Fibonacci até ||grad f|| pequeno
  x, f_atual = x1.copy(), f1
  n_it = 1
  for _ in range(500):
    if np.linalg.norm(grad_kelly(x)) < 1e-6:
      break
    x_novo, _, _, _, _ = passo_busca_linear(x)
    f_novo = f_kelly(x_novo)
    if f_novo >= f_atual:  # sem redução: limite da tolerância do Fibonacci
      break
    x, f_atual = x_novo, f_novo
    n_it += 1
  g_final = np.linalg.norm(grad_kelly(x))
  W_star = 1.0 + R @ x

  print("=" * 78)
  print(" KELLY MULTI-ATIVO: MÁXIMA DESCIDA + BUSCA LINEAR DE FIBONACCI")
  print("=" * 78)
  print(f"Gradiente analítico vs dif. finitas (x0): erro = {checar_gradiente(x0):.1e}")
  print(f"x0 = {fmt_x(x0)}  caixa {(1 - x0.sum())*100:.2f}%  "
        f"g(x0) = {-f0*100:.4f}% por período")
  print(f"grad f(x0) = [{g0[0]:.6f}, {g0[1]:.6f}]  "
        f"autovalores H = [{autovalores_H0[0]:.4f}, {autovalores_H0[1]:.4f}]  "
        f"def. positiva: {pd_ok}")
  print("-" * 78)
  print("1º PASSO")
  print(f"  grad f^T d0 = {descida:.6f}  (direção de descida: {descida < 0})")
  print(f"  alpha* = {alpha_star:.6f}  "
        f"({n_aval} avaliações de phi, incluindo o enquadramento)")
  print(f"  x1 = {fmt_x(x1)}  caixa {(1 - x1.sum())*100:.2f}%")
  print(f"  f(x1) = {f1:.6f}  g(x1) = {-f1*100:.4f}% por período  "
        f"(ganho de {(f0 - f1)*100:.2f} p.p.)")
  print(f"  grad f(x1)^T d0 = {np.dot(grad_kelly(x1), d0):.1e}  "
        "(~0: busca exata, passos consecutivos ortogonais)")
  print("-" * 78)
  print(f"CONVERGÊNCIA em {n_it} passos")
  print(f"  x* = {fmt_x(x)}  caixa {(1 - x.sum())*100:.2f}%  "
        f"exposição bruta {np.abs(x).sum()*100:.1f}%")
  print(f"  g* = {-f_atual*100:.4f}% por período  ||grad f(x*)|| = {g_final:.1e}")
  print(f"  riqueza por cenário W_s = {np.round(W_star, 4)}  "
        f"(pior: {W_star.min():.4f})")
  print(f"  1º passo capturou {(f0 - f1)/(f0 - f_atual)*100:.1f}% do ganho total")
  print("-" * 78)
  print("LEITURA")
  print("  - O gradiente em x0 aponta para os dois ativos porque ambos têm retorno")
  print(f"    esperado positivo (E[R] = [{p @ R[:, 0]*100:.1f}%, {p @ R[:, 1]*100:.1f}%]); "
        "o Ativo 2 domina por render mais.")
  if (1 - x.sum()) < 0:
    print("  - Caixa negativo = tomada de empréstimo (alavancagem). Premissas: "
          "empréstimo a taxa")
    print("    zero e sem limite, períodos i.i.d. e reinvestimento total.")
  print("  - Kelly pleno é agressivo: na recessão a riqueza cai para "
        f"{W_star[3]*100:.1f}% do capital.")
  print("  - Máxima descida com busca exata faz zigue-zague e converge "
        "linearmente a x*.")
  print("=" * 78)


if __name__ == "__main__":
  main()