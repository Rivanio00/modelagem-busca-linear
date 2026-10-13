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

# ---- TP7 ----
def f7(x):
    return (-13 + x[0] + ((5 - x[1]) * x[1] - 2) * x[1])**2 + (-29 + x[0] + ((x[1] + 1) * x[1] - 14) * x[1])**2

def grad7(x):
    return np.array(
        [
            2*(-13 + x[0] + ((5 - x[1]) * x[1] - 2) * x[1]) + 2*(-29 + x[0] + ((x[1] + 1) * x[1] - 14) * x[1]),
            2*(-13 + x[0] + ((5 - x[1]) * x[1] - 2) * x[1])*((-2*x[1] + 5) * x[1] + ((5 - x[1]) * x[1] - 2)) + 2*(-29 + x[0] + ((x[1] + 1) * x[1] - 14) * x[1])*((2*x[1] + 1) * x[1] + ((x[1] + 1)*x[1] - 14))
        ]
    )

def hess7(x):
    return np.array(
        [
            [4, (-2*x[1] + 5) * 2*x[1] + 2((5-x[1])*x[1] - 2) + (2*x[1] + 1)* 2*x[1] + 2((x[1] + 1)*x[1] - 14)],
            [(-2*x[1] + 5) * 2*x[1] + 2((5-x[1])*x[1] - 2) + (2*x[1] + 1)* 2*x[1] + 2((x[1] + 1)*x[1] - 14), (6*x[1]**2 + 20*x[1] - 4)*(-3*x[1]**2 + 10*x[1] - 2) + (2*x[1]**3 + 10*x[1]**2 - 4*x[1])*(-6*x[1] + 10) + (6*x[1]**2 + 4*x[1] - 28)*(3*x[1]**2 + 2*x[1] - 14) + (3*x[1]**3 + 2*x[1]**2 - 28*x[1])*(6*x[1]+2)]
        ]
    )

TP7 = Problema(
    nome="TP7",
    f=f7,
    grad=grad7,
    hess=hess7,
    x0=np.array([15, -2.0]),
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

# ---- TP17 ----
def f17(x):
    return 10000*x[0]**2 + 100*x[1]**2 + x[2]**2 + 0.01*x[3]**2

def grad17(x):
    return np.array([
        2*10000*x[0],
        2*100*x[1],
        2*x[2],
        2*0.01*x[3]
    ])

def hess17(x):
    return np.array([
        [2*10000,0,0,0],
        [0,2*100,0,0],
        [0,0,2,0],
        [0,0,0,2*0.01]
    ])

TP17 = Problema(
    nome="TP17",
    f=f17,
    grad=grad17,
    hess=hess17,
    x0=np.array([-4, -2, (-4)/3, -1]),
)