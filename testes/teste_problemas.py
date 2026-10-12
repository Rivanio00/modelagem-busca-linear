import numpy as np
from problemas import TP6, TP12
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