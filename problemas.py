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
    y = x[1]
    a = x[0] - 13 - y**3 + 5*y**2 - 2*y
    b = x[0] - 29 + y**3 + y**2 - 14*y
    return a**2 + b**2

def grad7(x):
    y = x[1]
    a = x[0] - 13 - y**3 + 5*y**2 - 2*y
    b = x[0] - 29 + y**3 + y**2 - 14*y

    da = -3*y**2 + 10*y - 2
    db = 3*y**2 + 2*y - 14

    return np.array([
        2*a + 2*b,
        2*a*da + 2*b*db
    ])

def hess7(x):
    y = x[1]
    a = x[0] - 13 - y**3 + 5*y**2 - 2*y
    b = x[0] - 29 + y**3 + y**2 - 14*y

    da = -3*y**2 + 10*y - 2
    db = 3*y**2 + 2*y - 14

    dda = -6*y + 10
    ddb = 6*y + 2

    hxy = 2*(da + db)
    hyy = 2*(da**2 + a*dda + db**2 + b*ddb)

    return np.array([
        [4, hxy],
        [hxy, hyy]
    ])

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

# ---- TP15 ----
def f15(x):
  a = 10 * (x[0] - x[1] ** 2) ** 2 + (x[0] - 1) ** 2
  return a ** (1 / 4)


def grad15(x):
  y = x[1]
  a = 10 * (x[0] - y**2) ** 2 + (x[0] - 1) ** 2

  da_dx1 = 20 * (x[0] - y**2) + 2 * (x[0] - 1)
  da_dx2 = -40 * y * (x[0] - y**2)

  return np.array([(1 / 4) * a ** (-3 / 4) * da_dx1, (1 / 4) * a ** (-3 / 4) * da_dx2])


def hess15(x):
  x1, x2 = x
  a = 10 * (x1 - x2**2) ** 2 + (x1 - 1) ** 2

  grad_a = np.array([20 * (x1 - x2**2) + 2 * (x1 - 1), -40 * x2 * (x1 - x2**2)])

  hess_a = np.array([[22, -40 * x2], [-40 * x2, 120 * x2**2 - 40 * x1]])

  return (1 / 4) * a ** (-3 / 4) * hess_a - (3 / 16) * a ** (-7 / 4) * np.outer(
      grad_a, grad_a
  )


TP15 = Problema(
    nome="TP15",
    f=f15,
    grad=grad15,
    hess=hess15,
    x0=np.array([-1.2, 1.0]),
)