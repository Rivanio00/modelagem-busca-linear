from pathlib import Path
import sys
import numpy as np
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
  sys.path.append(str(ROOT_DIR))

from base import make_phi
from condicoes import achar_passo
from direcoes import dir_gradiente, dir_newton, dir_newton_mod
from problemas import TP6, TP7, TP12, TP15
from busca_linear.fibonacci import busca_fibonacci

try:
  from busca_linear.newton1d import busca_newton1d
except ImportError:

  def busca_newton1d(phi, dphi, d2phi, alpha0=1.0, tol=1e-5, max_iter=50):
    """Fallback para Newton 1D caso não esteja no arquivo externo."""
    alpha = alpha0
    for k in range(max_iter):
      d2 = d2phi(alpha)
      if abs(d2) < 1e-12:
        break
      passo = dphi(alpha) / d2
      alpha = alpha - passo
      if abs(passo) < tol:
        break
    return alpha, {"num_iter": k + 1, "phi_star": phi(alpha)}


# BATERIA DE EXPERIMENTOS: 36 CASOS (4 TP x 3 Direções x 3 Métodos 1D)

PROBLEMAS = [TP6, TP7, TP12, TP15]

DIRECOES = {
    "d_G": dir_gradiente,
    "d_N": dir_newton,
    "d_M": dir_newton_mod,
}


def executar_busca_1d(metodo_nome, p, x0, g0, d0, H0, phi, dphi, d2phi):
  """Executa a busca 1D selecionada e padroniza a saída (alpha*, num_iter)."""
  if metodo_nome == "Fibonacci":
    alpha_star, info = busca_fibonacci(phi)
    num_iter = info.get("num_iter", "-")
    return alpha_star, num_iter

  elif metodo_nome == "Newton 1D":
    alpha_star, info = busca_newton1d(phi, dphi, d2phi)
    num_iter = info.get("num_iter", "-")
    return alpha_star, num_iter

  elif metodo_nome == "Goldstein":
    try:
      alpha_star, _ , k = achar_passo(
          p=p,
          x=x0,
          grad=g0,
          d=d0,
          hess=H0,
          condicao="goldstein",
          alpha0=1.0,
          rho=0.5,
          c=1e-4,
          sigma1=1e-4,
          sigma2=0.4,
          limit=100,
          alpha_max=1e6,
      )
      return alpha_star, k
    except Exception:
      return None, "Falha"

  raise ValueError(f"Método 1D desconhecido: {metodo_nome}")


def rodar_todos_experimentos():
  resultados = []
  metodos_1d = ["Fibonacci", "Newton 1D", "Goldstein"]

  print(
      "=========================================================================================="
  )
  print(
      "                      EXECUTANDO BATERIA DE 36 EXPERIMENTOS                     "
  )
  print(
      "=========================================================================================="
  )

  for p in PROBLEMAS:
    x0 = p.x0.copy()
    g0 = p.grad(x0)
    H0 = p.hess(x0)
    f0 = p.f(x0)

    for dir_nome, fn_dir in DIRECOES.items():
      # Calcula a direção com as funções de direcoes.py
      d0 = fn_dir(g0, H0)

      # Se a direção for indefina
      if d0 is None:
        for m_nome in metodos_1d:
          resultados.append({
              "Problema": p.nome,
              "Direção": dir_nome,
              "Método 1D": m_nome,
              "alpha*": "N/A",
              "f(x0)": round(f0, 6),
              "f(x1)": "Singular",
              "Delta f": "N/A",
              "Iterações 1D": "-",
              "Status": "Hessiana Singular (d_N falhou)",
          })
        continue

      # Constroi phi, dphi e d2phi via make_phi
      phi, dphi, d2phi = make_phi(p, x0, d0)

      for m_nome in metodos_1d:
        alpha_star, num_iter = executar_busca_1d(
            m_nome, p, x0, g0, d0, H0, phi, dphi, d2phi
        )

        if alpha_star is None:
          resultados.append({
              "Problema": p.nome,
              "Direção": dir_nome,
              "Método 1D": m_nome,
              "alpha*": "Falha",
              "f(x0)": round(f0, 6),
              "f(x1)": "Falha",
              "Delta f": "Falha",
              "Iterações 1D": num_iter,
              "Status": "Não convergiu",
          })
        else:
          f1 = phi(alpha_star)
          delta_f = f0 - f1
          resultados.append({
              "Problema": p.nome,
              "Direção": dir_nome,
              "Método 1D": m_nome,
              "alpha*": round(alpha_star, 6),
              "f(x0)": round(f0, 6),
              "f(x1)": round(f1, 6),
              "Delta f": round(delta_f, 6),
              "Iterações 1D": num_iter,
              "Status": "OK" if delta_f > 0 else "Sem redução",
          })

  # DataFrame com os 36 casos
  df = pd.DataFrame(resultados)

  # Imprimir tabela no terminal
  print("\n" + df.to_string(index=False))

  # Exportar tabela formatada em Markdown para o relatório final
  df.to_markdown("tabela_36_experimentos.md", index=False)
  print("\n[OK] Tabela salva com sucesso em 'tabela_36_experimentos.md'!")

  return df


if __name__ == "__main__":
  rodar_todos_experimentos()