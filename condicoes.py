
import numpy as np
from base import Problema

def armijo(p: Problema, x, grad, d,
           alpha0: float = 1.0,
           rho: float = 0.5,
           c: float = 1e-4,
           limit: int = 100):

    alpha = alpha0
    fx = p.f(x)
    grad_d = np.dot(grad, d)

    if grad_d >= 0:
        raise ValueError("A direção não é de descida.")

    for _ in range(limit):
        x_novo = x + alpha * d

        if p.f(x_novo) <= fx + c * alpha * grad_d:
            return alpha

        alpha *= rho

    raise RuntimeError("A busca de Armijo não encontrou um passo válido.")