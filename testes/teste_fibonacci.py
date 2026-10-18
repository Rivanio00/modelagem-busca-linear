import numpy as np
from base import make_phi
from busca_linear.fibonacci import busca_fibonacci, enquadrar_intervalo
from problemas import TP6, TP15
from testes.utils import checar


def test_fibonacci_tp6():
  g = TP6.grad(TP6.x0)
  d_G = -g
  phi, _, _ = make_phi(TP6, TP6.x0, d_G)

  alpha_star, info = busca_fibonacci(phi)
  print(
      f"TP6 (d_G): alpha* = {alpha_star:.6f}, phi(alpha*) = {info['phi_star']:.6f}"
  )

  checar(
      phi(alpha_star) < phi(0), "TP6 (d_G): Fibonacci reduz o valor da funcao"
  )
  checar(
      np.isclose(alpha_star, 41 / 57, atol=1e-4),
      "TP6 (d_G): alpha* proximo do valor teorico (41/57)",
  )


def test_fibonacci_tp15():
  g = TP15.grad(TP15.x0)
  d_G = -g
  phi, _, _ = make_phi(TP15, TP15.x0, d_G)

  alpha_star, info = busca_fibonacci(phi)
  print(
      f"TP15 (d_G): alpha* = {alpha_star:.6f}, phi(alpha*) ="
      f" {info['phi_star']:.6f}"
  )

  checar(
      phi(alpha_star) < phi(0), "TP15 (d_G): Fibonacci reduz o valor da funcao"
  )

def test_fibonacci_quadratica_simples():
  phi = lambda x: (x - 0.3) ** 2
  alpha, info = busca_fibonacci(phi, tol=1e-6)
  assert abs(alpha - 0.3) < 1e-6
  assert info["a_final"] <= 0.3 <= info["b_final"]


def test_enquadrar_nao_perde_minimo_assimetrico():
  phi = lambda x: (x - 0.5) ** 2 if x < 0.5 else 10 * (x - 0.5) ** 2
  a, b = enquadrar_intervalo(phi, step_inicial=0.8)
  assert a <= 0.5 <= b

  # o Fibonacci, usando esse enquadramento, também deve achar o mínimo
  alpha, _ = busca_fibonacci(phi, tol=1e-6)
  assert abs(alpha - 0.5) < 1e-4