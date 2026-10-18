import numpy as np
from base import Problema
from direcoes import dir_gradiente

def armijo(
    p: Problema,
    x,
    grad,
    d,
    hess,
    alpha0: float = 1.0,
    rho: float = 0.5,
    c: float = 1e-4,
    limit: int = 100,
):
    alpha = alpha0
    fx = p.f(x)
    grad_d = np.dot(grad, d)

    if grad_d >= 0:
        #se não for direção de descida, troca para inverso do gradiente
        d = dir_gradiente(grad, hess)
        grad_d = np.dot(grad, d)

    for _ in range(limit):
        x_novo = x + alpha * d

        if p.f(x_novo) <= fx + c * alpha * grad_d:
            return alpha, d

        alpha *= rho

    raise RuntimeError(
        "A busca de Armijo não encontrou um passo válido."
    )

def condicoes_wolfe(
    p: Problema,
    x,
    grad,
    d,
    alpha: float,
    sigma1: float = 1e-4,
    sigma2: float = 0.9,
):
    x_novo = x + alpha * d

    #decréscimo suficiente (Armijo)
    armijo = p.f(x_novo) <= (
        p.f(x) + sigma1 * alpha * np.dot(grad, d)
    )

    #condição de curvatura de Wolfe
    grad_novo = p.grad(x_novo)
    curvatura = (
        np.dot(grad_novo, d)
        >= sigma2 * np.dot(grad, d)
    )

    return armijo, curvatura


def wolfe(
    p: Problema,
    x,
    grad,
    d,
    hess,
    alpha0: float = 1.0,
    sigma1: float = 1e-4,
    sigma2: float = 0.9,
    limit: int = 100,
    alpha_max: float = 1e6,
):
    # Garantir que d seja uma direção de descida
    if np.dot(grad, d) >= 0:
        d = dir_gradiente(grad, hess)

    if np.dot(grad, d) >= 0:
        raise ValueError(
            "Não foi possível obter uma direção de descida."
        )

    # Limites do intervalo de busca
    alpha_til = 0.0
    alpha_hat = None

    alpha = alpha0

    for _ in range(limit):
        armijo, curvatura = condicoes_wolfe(
            p, x, grad, d, alpha, sigma1, sigma2
        )

        # Passo 1: ambas as condições foram satisfeitas
        if armijo and curvatura:
            return alpha, d

        # Passo 2: Armijo foi violada; definir limite superior
        if not armijo:
            alpha_hat = alpha

        # Passo 3: curvatura foi violada; definir limite inferior
        elif not curvatura:
            alpha_til = alpha

        # Passo 4: extrapolação
        if alpha_hat is None:
            alpha = 2 * alpha

            if alpha > alpha_max:
                raise RuntimeError(
                    "A busca de Wolfe excedeu alpha_max."
                )

        # Passo 5: interpolação
        else:
            alpha = (alpha_til + alpha_hat) / 2

    raise RuntimeError(
        "A busca de Wolfe não encontrou um passo válido."
    )