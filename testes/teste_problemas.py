import numpy as np
from problemas import TP6, TP7, TP12, TP15
from testes.utils import checar, mostrar


def test_tp6_valores_em_x0():
    x0 = TP6.x0
    mostrar("x0", x0)
    mostrar("f(x0)", TP6.f(x0))
    mostrar("grad(x0)", TP6.grad(x0))
    mostrar("hess(x0)", TP6.hess(x0))
    checar(np.isclose(TP6.f(x0), 16), "f6(x0) = 16", f"obtido: {TP6.f(x0)}")
    checar(np.allclose(TP6.grad(x0), [-5, -4]), "grad f6(x0) = (-5, -4)")
    checar(np.allclose(TP6.hess(x0), [[1, 0], [0, 2]]), "hess f6(x0) = diag(1, 2)")


def test_tp6_minimizador():
    m = np.array([1.0, 0.0])
    checar(np.isclose(TP6.f(m), -0.5), "f6(1, 0) = -0.5")
    checar(np.allclose(TP6.grad(m), [0, 0]), "grad f6(1, 0) = 0")
    checar(np.all(np.linalg.eigvalsh(TP6.hess(m)) > 0), "hess f6 definida positiva")

def test_tp7_valores_em_x0():
    x0 = TP7.x0
    H = TP7.hess(x0)
    autovalores, autovetores = np.linalg.eigh(H)
    mostrar("x0", x0)
    mostrar("f(x0)", TP7.f(x0))
    mostrar("grad(x0)", TP7.grad(x0))
    mostrar("hess(x0)", H)
    mostrar("autovalores da hess(x0)", autovalores)
    mostrar("autovetores da hess(x0)", autovetores)
    checar(np.isclose(TP7.f(x0), 1256), "f7(x0) = 1256", f"obtido: {TP7.f(x0)}")
    checar(np.allclose(TP7.grad(x0), [88, -2432]), "grad f7(x0) = (88, -2432)")
    checar(np.allclose(H, [[4, -80], [-80, 3680]]), "hess f7(x0) = [[4, -80], [-80, 3680]]")
    checar(np.allclose(autovalores, [2.2598, 3681.7402], atol=1e-3),
           "autovalores hess f7(x0) ~ (2.2598, 3681.7402)")
    checar(np.all(autovalores > 0), "hess f7(x0) definida positiva")
    checar(np.allclose(H @ autovetores, autovetores * autovalores),
           "H v = lambda v para os autovetores de hess f7(x0)")


def test_tp7_minimo_local():
    m = np.array([11.4127789858, -0.8968052534])
    H = TP7.hess(m)
    autovalores, autovetores = np.linalg.eigh(H)
    mostrar("m", m)
    mostrar("f(m)", TP7.f(m))
    mostrar("grad(m)", TP7.grad(m))
    mostrar("hess(m)", H)
    mostrar("autovalores da hess(m)", autovalores)
    mostrar("autovetores da hess(m)", autovetores)
    checar(np.isclose(TP7.f(m), 48.9843, atol=1e-3), "f7(m) ~ 48.9843", f"obtido: {TP7.f(m)}")
    checar(np.allclose(TP7.grad(m), [0, 0], atol=1e-5), "grad f7(m) ~ (0, 0)")
    checar(np.allclose(H, [[4, -53.5233], [-53.5233, 901.8878]], atol=1e-3),
           "hess f7(m) ~ [[4, -53.5233], [-53.5233, 901.8878]]")
    checar(np.allclose(autovalores, [0.8207, 905.0670], atol=1e-3),
           "autovalores hess f7(m) ~ (0.8207, 905.0670)")
    checar(np.all(autovalores > 0), "hess f7(m) definida positiva (minimo local)")
    checar(np.allclose(H @ autovetores, autovetores * autovalores),
           "H v = lambda v para os autovetores de hess f7(m)")


def test_tp7_minimo_global():
    g = np.array([5.0, 4.0])
    H = TP7.hess(g)
    autovalores, autovetores = np.linalg.eigh(H)
    mostrar("g", g)
    mostrar("f(g)", TP7.f(g))
    mostrar("grad(g)", TP7.grad(g))
    mostrar("hess(g)", H)
    mostrar("autovalores da hess(g)", autovalores)
    mostrar("autovetores da hess(g)", autovetores)
    checar(np.isclose(TP7.f(g), 0), "f7(5, 4) = 0", f"obtido: {TP7.f(g)}")
    checar(np.allclose(TP7.grad(g), [0, 0]), "grad f7(5, 4) = (0, 0)")
    checar(np.allclose(H, [[4, 64], [64, 3728]]), "hess f7(5, 4) = [[4, 64], [64, 3728]]")
    checar(np.allclose(autovalores, [2.9004, 3729.0996], atol=1e-3),
           "autovalores hess f7(5, 4) ~ (2.9004, 3729.0996)")
    checar(np.all(autovalores > 0), "hess f7(5, 4) definida positiva (minimo global)")
    checar(np.allclose(H @ autovetores, autovetores * autovalores),
           "H v = lambda v para os autovetores de hess f7(5, 4)")

def test_tp12_valores_em_x0():
    x0 = TP12.x0
    autovalores = np.linalg.eigvalsh(TP12.hess(x0))
    mostrar("x0", x0)
    mostrar("f(x0)", TP12.f(x0))
    mostrar("grad(x0)", TP12.grad(x0))
    mostrar("hess(x0)", TP12.hess(x0))
    mostrar("autovalores da hess(x0)", autovalores)
    checar(np.isclose(TP12.f(x0), 106), "f12(x0) = 106", f"obtido: {TP12.f(x0)}")
    checar(np.allclose(TP12.grad(x0), [-46, -38]), "grad f12(x0) = (-46, -38)")
    checar(np.allclose(TP12.hess(x0), [[-26, 8], [8, -10]]), "hess f12(x0) = [[-26, 8], [8, -10]]")
    checar(np.allclose(autovalores, [-29.314, -6.686], atol=1e-3),
           "hess f12(x0) definida negativa (autovalores ~ -29.31 e -6.69)")


def test_tp12_minimo_local():
    m = np.array([3.0, 2.0])
    checar(np.isclose(TP12.f(m), 0), "f12(3, 2) = 0")
    checar(np.allclose(TP12.grad(m), [0, 0]), "grad f12(3, 2) = 0")
    checar(np.allclose(TP12.hess(m), [[74, 20], [20, 34]]), "hess f12(3, 2) = [[74, 20], [20, 34]]")
    checar(np.all(np.linalg.eigvalsh(TP12.hess(m)) > 0), "hess f12(3, 2) definida positiva")

def test_tp15_valores_em_x0():
  x0 = TP15.x0
  f_val = TP15.f(x0)
  g_val = TP15.grad(x0)
  H_val = TP15.hess(x0)
  autovalores = np.linalg.eigvalsh(H_val)

  mostrar("x0", x0)
  mostrar("f(x0)", f_val)
  mostrar("grad(x0)", g_val)
  mostrar("hess(x0)", H_val)
  mostrar("autovalores da hess(x0)", autovalores)

  checar(np.isclose(f_val, 2.701217, atol=1e-4), "f15(x0) ~ 2.7012")
  checar(
      np.allclose(g_val, [-0.613913, 1.116205], atol=1e-4),
      "grad f15(x0) ~ (-0.6139, 1.1162)",
  )
  checar(
      np.allclose(autovalores, [-0.206971, 0.814657], atol=1e-4),
      "hess f15(x0) indefinida (autovalores ~ -0.207 e 0.815)",
  )


def test_tp15_minimizador():
  m = np.array([1.0, 1.0])
  checar(np.isclose(TP15.f(m), 0.0), "f15(1, 1) = 0.0 (minimo global)")