import numpy as np
from base import Problema


# ---- TP6 ----
def f6(x):
    return (0.5 * (x[0]*x[0])) + (x[1]*x[1]) - x[0]


def grad6(x):
    return np.array([x[0] - 1, 2 * x[1]])


def hess6(x):
    return np.array([[1.0, 0.0],
                     [0.0, 2.0]])


TP6 = Problema(
    nome="TP6",
    f=f6,
    grad=grad6,
    hess=hess6,
    x0=np.array([-4.0, -2.0]),
)

# ---- TP12 ----
def f12(x):
    u = (x[0]*x[0]) + x[1] - 11
    v = x[0] + (x[1]*x[1]) - 7
    return (u*u) + (v*v)


def grad12(x):
    u = (x[0]*x[0]) + x[1] - 11
    v = x[0] + (x[1]*x[1]) - 7
    return np.array([4 * x[0] * u + 2 * v,
                     2 * u + 4 * x[1] * v])


def hess12(x):
    return np.array([[12 * (x[0]*x[0]) + 4 * x[1] - 42, 4 * x[0] + 4 * x[1]],
                     [4 * x[0] + 4 * x[1],          4 * x[0] + 12 * (x[1]*x[1]) - 26]])


TP12 = Problema(
    nome="TP12",
    f=f12,
    grad=grad12,
    hess=hess12,
    x0=np.array([1.0, 1.0]),
)