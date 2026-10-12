import numpy as np
from base import make_phi
from problemas import TP6, TP12
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


def test_phi_tp12_com_d_G():
    d_G = -TP12.grad(TP12.x0)
    phi, dphi, d2phi = make_phi(TP12, TP12.x0, d_G)
    mostrar("phi(0)", phi(0))
    mostrar("dphi(0)", dphi(0))
    mostrar("d2phi(0)", d2phi(0))
    checar(np.isclose(phi(0), 106), "phi(0) = 106", f"obtido: {phi(0)}")
    checar(np.isclose(dphi(0), -3560), "phi'(0) = -3560 (= -||g||^2)")
    checar(np.isclose(d2phi(0), -41488), "phi''(0) = -41488 (curvatura NEGATIVA em alpha=0)")