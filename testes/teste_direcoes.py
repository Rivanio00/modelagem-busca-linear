import numpy as np
from direcoes import (dir_gradiente, dir_newton, dir_newton_mod,
                      escolher_mu, eh_descida)
from problemas import TP6, TP7, TP12, TP15
from testes.utils import checar, mostrar


def test_direcoes_tp6():
    x0 = TP6.x0
    g, H = TP6.grad(x0), TP6.hess(x0)
    d_G, d_N, d_M = dir_gradiente(g, H), dir_newton(g, H), dir_newton_mod(g, H)
    mu = escolher_mu(H)
    mostrar("d_G", d_G)
    mostrar("d_N", d_N)
    mostrar("d_M", d_M)
    mostrar("mu", mu)
    checar(np.allclose(d_G, [5, 4]), "d_G = (5, 4)")
    checar(np.allclose(d_N, [5, 2]), "d_N = (5, 2)")
    checar(mu == 0.0, "mu = 0 (H ja e definida positiva)")
    checar(np.allclose(d_M, d_N), "d_M = d_N quando mu = 0")
    checar(eh_descida(g, d_G) and eh_descida(g, d_N) and eh_descida(g, d_M),
           "as tres direcoes sao de descida")
    checar(np.allclose(x0 + d_N, [1, 0]), "x0 + d_N cai no minimizador (1, 0)")

def test_direcoes_tp7():
    x0 = TP7.x0
    g, H = TP7.grad(x0), TP7.hess(x0)
    d_G, d_N, d_M = dir_gradiente(g, H), dir_newton(g, H), dir_newton_mod(g, H)
    mu = escolher_mu(H)
    mostrar("d_G", d_G)
    mostrar("d_N", d_N)
    mostrar("g . d_G", g @ d_G)
    mostrar("g . d_N", g @ d_N)
    mostrar("mu", mu)
    mostrar("d_M", d_M)
    mostrar("x0 + d_N", x0 + d_N)
    mostrar("f7(x0 + d_N)", TP7.f(x0 + d_N))
    checar(np.allclose(d_G, [-88, 2432]), "d_G = (-88, 2432)")
    checar(np.allclose(d_N, [-15.5385, 0.3231], atol=1e-3), "d_N = (-15.5385, 0.3231)")
    checar(np.isclose(g @ d_G, -5922368), "g . d_G = -5922368 (= -||g||^2)")
    checar(np.isclose(g @ d_N, -2153.1, rtol=1e-4), "g . d_N = -2153.1")
    checar(mu == 0.0, "mu = 0 (H ja e definida positiva)")
    checar(np.allclose(d_M, d_N), "d_M = d_N quando mu = 0")
    checar(eh_descida(g, d_G) and eh_descida(g, d_N) and eh_descida(g, d_M),
           "as tres direcoes sao de descida")
    checar(np.allclose(x0 + d_N, [-0.5385, -1.6769], atol=1e-3),
           "x0 + d_N = (-0.5385, -1.6769)")
    checar(np.isclose(TP7.f(x0 + d_N), 137.254, rtol=1e-4),
           "f7(x0 + d_N) ~ 137.25 < f7(x0) = 1256 (reduz, mas nao chega no minimizador)")

def test_direcoes_tp12():
    x0 = TP12.x0
    g, H = TP12.grad(x0), TP12.hess(x0)
    d_G, d_N, d_M = dir_gradiente(g, H), dir_newton(g, H), dir_newton_mod(g, H)
    mu = escolher_mu(H)
    mostrar("d_G", d_G)
    mostrar("d_N", d_N)
    mostrar("g . d_N", g @ d_N)
    mostrar("mu", mu)
    mostrar("d_M", d_M)
    mostrar("g . d_M", g @ d_M)
    checar(eh_descida(g, d_G), "d_G e de descida")
    checar(np.allclose(d_N, [-3.898, -6.918], atol=1e-3), "d_N = (-3.898, -6.918)")
    checar(np.isclose(g @ d_N, 442.2, rtol=1e-3), "g . d_N = +442.2")
    checar(not eh_descida(g, d_N), "d_N NAO e de descida (falha teorica esperada)")
    checar(np.isclose(mu, 100), "mu = 100")
    checar(np.allclose(d_M, [0.5816, 0.3705], atol=1e-4), "d_M = (0.5816, 0.3705)")
    checar(eh_descida(g, d_M), "d_M e de descida (a regularizacao corrige d_N)")


def test_escolher_mu_tp12_limiar():
    H = TP12.hess(TP12.x0)
    menor_10 = np.linalg.eigvalsh(H + 10 * np.eye(2)).min()
    menor_100 = np.linalg.eigvalsh(H + 100 * np.eye(2)).min()
    mostrar("menor autovalor de H + 10 I", menor_10)
    mostrar("menor autovalor de H + 100 I", menor_100)
    checar(menor_10 < 0, "mu = 10 nao basta (precisa de mu > 29.31)")
    checar(menor_100 > 0, "mu = 100 basta")


def test_direcoes_casos_de_borda():
    g = np.array([-46.0, -38.0])
    checar(dir_newton(g, np.zeros((2, 2))) is None, "H singular: d_N devolve None")
    checar(not eh_descida(g, None), "direcao None conta como nao-descida")

def test_direcoes_tp15():
  x0 = TP15.x0
  g, H = TP15.grad(x0), TP15.hess(x0)
  d_G, d_N, d_M = dir_gradiente(g, H), dir_newton(g, H), dir_newton_mod(g, H)
  mu = escolher_mu(H)

  mostrar("d_G", d_G)
  mostrar("d_N", d_N)
  mostrar("g . d_N", g @ d_N)
  mostrar("mu", mu)
  mostrar("d_M", d_M)
  mostrar("g . d_M", g @ d_M)

  checar(eh_descida(g, d_G), "d_G e de descida")
  checar(
      not eh_descida(g, d_N),
      "d_N NAO e de descida em x0 (Hessiana indefinida)",
  )
  checar(np.isclose(mu, 1.0, atol=1e-2), "mu = 1.0 para regularizar H")
  checar(
      eh_descida(g, d_M), "d_M e de descida (a regularizacao corrige d_N)"
  )