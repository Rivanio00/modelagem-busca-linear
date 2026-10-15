import numpy as np
from base import make_phi
from problemas import TP6, TP7, TP12, TP15
from testes.utils import checar, mostrar


def test_phi_tp6_com_d_G():
    g = TP6.grad(TP6.x0)
    d_G = -g
    phi, dphi, d2phi = make_phi(TP6, TP6.x0, d_G)
    mostrar("d_G", d_G)
    mostrar("phi(0)", phi(0))
    mostrar("dphi(0)", dphi(0))
    mostrar("d2phi(0)", d2phi(0))
    checar(np.isclose(phi(0), 16), "phi(0) = 16")
    checar(np.isclose(dphi(0), -41), "phi'(0) = -41 (= -||g||^2)")
    checar(np.isclose(d2phi(0), 57), "phi''(0) = 57")
    alpha_star = 41 / 57
    mostrar("alpha* exato (TP6 e quadratico)", alpha_star)
    checar(np.isclose(dphi(alpha_star), 0), "phi'(alpha*) = 0")


def test_phi_tp6_com_d_N():
    g, H = TP6.grad(TP6.x0), TP6.hess(TP6.x0)
    d_N = -np.linalg.solve(H, g)
    phi, _, _ = make_phi(TP6, TP6.x0, d_N)
    mostrar("d_N", d_N)
    mostrar("phi(1)", phi(1))
    checar(np.allclose(d_N, [5, 2]), "d_N = (5, 2)")
    checar(np.isclose(phi(1), -0.5), "phi(1) = f6(1, 0) = -0.5 (minimo em um passo)")


def test_phi_tp6_derivadas_numericas():
    d_G = -TP6.grad(TP6.x0)
    phi, dphi, d2phi = make_phi(TP6, TP6.x0, d_G)
    h, a = 1e-6, 0.3
    num1 = (phi(a + h) - phi(a - h)) / (2 * h)
    num2 = (dphi(a + h) - dphi(a - h)) / (2 * h)
    mostrar("phi' analitica  em alpha=0.3", dphi(a))
    mostrar("phi' numerica   em alpha=0.3", num1)
    checar(np.isclose(dphi(a), num1, rtol=1e-5), "phi' analitica = numerica")
    checar(np.isclose(d2phi(a), num2, rtol=1e-5), "phi'' analitica = numerica")

def test_phi_tp7_com_d_G():
    d_G = -TP7.grad(TP7.x0)
    phi, dphi, d2phi = make_phi(TP7, TP7.x0, d_G)
    mostrar("phi(0)", phi(0))
    mostrar("dphi(0)", dphi(0))
    mostrar("d2phi(0)", d2phi(0))
    checar(np.isclose(phi(0), 1256), "phi(0) = 1256", f"obtido: {phi(0)}")
    checar(np.isclose(dphi(0), -5922368), "phi'(0) = -5922368 (= -||g||^2)")
    checar(np.isclose(d2phi(0), 21800089856), "phi''(0) = 21800089856 (curvatura positiva)")
    alpha_q = -dphi(0) / d2phi(0)
    mostrar("alpha quadratico = -phi'(0)/phi''(0)", alpha_q)
    mostrar("phi(alpha_q)", phi(alpha_q))
    mostrar("phi'(alpha_q)", dphi(alpha_q))
    checar(np.isclose(alpha_q, 2.7167e-4, rtol=1e-3), "alpha quadratico ~ 2.7167e-4")
    checar(phi(alpha_q) < phi(0), "phi(alpha_q) < phi(0): o passo quadratico reduz f")
    checar(abs(dphi(alpha_q)) > 1e5,
           "phi'(alpha_q) != 0: TP7 NAO e quadratico, alpha_q nao e o minimizador exato")


def test_phi_tp7_com_d_N():
    g, H = TP7.grad(TP7.x0), TP7.hess(TP7.x0)
    d_N = -np.linalg.solve(H, g)
    phi, dphi, d2phi = make_phi(TP7, TP7.x0, d_N)
    mostrar("d_N", d_N)
    mostrar("phi(1)", phi(1))
    mostrar("dphi(0)", dphi(0))
    mostrar("d2phi(0)", d2phi(0))
    checar(np.allclose(d_N, [-15.5385, 0.3231], atol=1e-3), "d_N = (-15.5385, 0.3231)")
    checar(np.isclose(phi(1), 137.254, rtol=1e-4), "phi(1) = f7(x0 + d_N) ~ 137.25")
    checar(np.isclose(dphi(0), -2153.1, rtol=1e-4), "phi'(0) = g . d_N = -2153.1")
    checar(np.isclose(d2phi(0), -dphi(0)),
           "phi''(0) = -phi'(0) (porque H d_N = -g)")


def test_phi_tp7_derivadas_numericas():
    x0 = TP7.x0
    g, H = TP7.grad(x0), TP7.hess(x0)
    # com d_N, phi e bem escalada: alpha = 0.3 e h = 1e-6 funcionam
    d_N = -np.linalg.solve(H, g)
    phi, dphi, d2phi = make_phi(TP7, x0, d_N)
    h, a = 1e-6, 0.3
    num1 = (phi(a + h) - phi(a - h)) / (2 * h)
    num2 = (dphi(a + h) - dphi(a - h)) / (2 * h)
    mostrar("phi' analitica (d_N) em alpha=0.3", dphi(a))
    mostrar("phi' numerica  (d_N) em alpha=0.3", num1)
    checar(np.isclose(dphi(a), num1, rtol=1e-5), "phi' analitica = numerica (d_N)")
    checar(np.isclose(d2phi(a), num2, rtol=1e-5), "phi'' analitica = numerica (d_N)")
    # com d_G, ||d|| ~ 2433: phi explode, entao usa alpha minusculo e h menor
    phi, dphi, d2phi = make_phi(TP7, x0, -g)
    h, a = 1e-9, 1e-4
    num1 = (phi(a + h) - phi(a - h)) / (2 * h)
    mostrar("phi' analitica (d_G) em alpha=1e-4", dphi(a))
    mostrar("phi' numerica  (d_G) em alpha=1e-4", num1)
    checar(np.isclose(dphi(a), num1, rtol=1e-5), "phi' analitica = numerica (d_G)")

def test_phi_tp12_com_d_G():
    d_G = -TP12.grad(TP12.x0)
    phi, dphi, d2phi = make_phi(TP12, TP12.x0, d_G)
    mostrar("phi(0)", phi(0))
    mostrar("dphi(0)", dphi(0))
    mostrar("d2phi(0)", d2phi(0))
    checar(np.isclose(phi(0), 106), "phi(0) = 106", f"obtido: {phi(0)}")
    checar(np.isclose(dphi(0), -3560), "phi'(0) = -3560 (= -||g||^2)")
    checar(np.isclose(d2phi(0), -41488), "phi''(0) = -41488 (curvatura NEGATIVA em alpha=0)")

def test_phi_tp15_com_d_G():
  d_G = -TP15.grad(TP15.x0)
  phi, dphi, d2phi = make_phi(TP15, TP15.x0, d_G)

  mostrar("phi(0)", phi(0))
  mostrar("dphi(0)", dphi(0))
  mostrar("d2phi(0)", d2phi(0))

  checar(np.isclose(phi(0), 2.701217, atol=1e-4), "phi(0) ~ 2.7012")
  checar(dphi(0) < 0, "phi'(0) < 0 (direcao de descida)")


def test_phi_tp15_derivadas_numericas():
  x0 = TP15.x0
  g, H = TP15.grad(x0), TP15.hess(x0)
  d_N = -np.linalg.solve(H, g)

  phi, dphi, d2phi = make_phi(TP15, x0, d_N)
  h, a = 1e-6, 0.1
  num1 = (phi(a + h) - phi(a - h)) / (2 * h)
  num2 = (dphi(a + h) - dphi(a - h)) / (2 * h)

  mostrar("phi' analitica em alpha=0.1", dphi(a))
  mostrar("phi' numerica  em alpha=0.1", num1)

  checar(np.isclose(dphi(a), num1, rtol=1e-4), "phi' analitica = numerica (d_N)")
  checar(
      np.isclose(d2phi(a), num2, rtol=1e-4), "phi'' analitica = numerica (d_N)"
  )