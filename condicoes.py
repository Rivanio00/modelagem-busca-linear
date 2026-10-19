import numpy as np
from base import Problema
from direcoes import dir_gradiente

def armijo(
    p: Problema,
    x,
    grad,
    d,
    hess,
    alpha0: float,
    rho: float,
    c: float,
    limit: int,
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

def condicoes_goldstein(
    p: Problema,
    x,
    grad,
    d,
    alpha: float,
    sigma1: float = 1e-4,
    sigma2: float = 0.9,
):
    fx = p.f(x)
    f_novo = p.f(x + alpha * d)
    grad_d = np.dot(grad, d)

    inferior = fx + sigma2 * alpha * grad_d
    superior = fx + sigma1 * alpha * grad_d

    return inferior <= f_novo <= superior


def busca_passo_wolfe_goldstein(
    p: Problema,
    x,
    grad,
    d,
    hess,
    condicao: str,
    alpha0: float,
    sigma1: float,
    sigma2: float,
    limit: int,
    alpha_max: float,
):
    if not (0 < sigma1 < sigma2 < 1):
        raise ValueError("É necessário 0 < sigma1 < sigma2 < 1.")

    if condicao not in ("wolfe", "goldstein"):
        raise ValueError("Use 'wolfe' ou 'goldstein'.")

    if np.dot(grad, d) >= 0:
        d = dir_gradiente(grad, hess)

    grad_d = np.dot(grad, d)

    if grad_d >= 0:
        raise ValueError("Não foi possível obter uma direção de descida.")

    fx = p.f(x)
    alpha_til = 0.0
    alpha_hat = None
    alpha = alpha0

    for _ in range(limit):
        x_novo = x + alpha * d
        f_novo = p.f(x_novo)

        if condicao == "wolfe":
            armijo = f_novo <= fx + sigma1 * alpha * grad_d
            curvatura = (
                np.dot(p.grad(x_novo), d) >= sigma2 * grad_d
            )

            if armijo and curvatura:
                return alpha, d

            if not armijo:
                alpha_hat = alpha
            else:
                alpha_til = alpha

        else:  # Goldstein
            inferior = fx + sigma2 * alpha * grad_d
            superior = fx + sigma1 * alpha * grad_d

            if inferior <= f_novo <= superior:
                return alpha, d

            if f_novo < inferior:
                # Passo pequeno demais: extrapolar
                alpha_til = alpha
            else:
                # Passo grande demais: reduzir o intervalo
                alpha_hat = alpha

        if alpha_hat is None:
            alpha = min(2 * alpha, alpha_max)

            if alpha >= alpha_max:
                raise RuntimeError(
                    "A busca atingiu alpha_max sem encontrar um passo válido."
                )
        else:
            alpha = (alpha_til + alpha_hat) / 2

    raise RuntimeError(
        f"A busca de passo ({condicao}) não encontrou um passo válido."
    )

def achar_passo(p: Problema,
    x,
    grad,
    d,
    hess,
    condicao: str,
    alpha0: float,
    rho: float,
    c: float,
    sigma1: float,
    sigma2: float,
    limit: int,
    alpha_max: float):

    if condicao == "armijo":
        return armijo(p, x, grad, d, hess, alpha0, rho, c, limit)
    else:
        return busca_passo_wolfe_goldstein(p, x, grad, d, hess, condicao, alpha0, sigma1, sigma2, limit, alpha_max)