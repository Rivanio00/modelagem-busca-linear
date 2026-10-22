import numpy as np
from base import Problema
from condicoes import achar_passo
from problemas import TP6, TP7, TP12, TP15
from direcoes import dir_gradiente, dir_newton, dir_newton_mod

E = 1e-4
K_LIMIT = 100

def busca_iterativa(
    p: Problema,
    e: float = E,
    k_limit: int = K_LIMIT,
    direcao_inicial: str = "newton",
    direcao_iterativa: str = "newton",
    condicao_passo: str = "armijo",
    alpha0: float = 1.0,
    rho: float = 0.5,
    c: float = 1e-4,
    sigma1: float = 1e-4,
    sigma2: float = 0.9,
    limit: int = 100,
    alpha_max: float = 1e6,
):
    x = p.x0.copy()
    grad = p.grad(x)
    hess = p.hess(x)

    # Escolhendo a direção inicial
    if direcao_inicial == "gradiente":
        d = dir_gradiente(grad, hess)
    elif direcao_inicial == "newton_modificado":
        d = dir_newton_mod(grad, hess)
    elif direcao_inicial == "newton":
        d = dir_newton(grad, hess)
    else:
        raise ValueError(
            "Direção inicial inválida. Use 'newton', "
            "'newton_modificado' ou 'gradiente'."
        )

    i = 0

    while not np.all(np.abs(grad) <= e) and i < k_limit:

        if i > 0:
            if direcao_iterativa == "gradiente":
                d = dir_gradiente(grad, hess)
            elif direcao_iterativa == "newton_modificado":
                d = dir_newton_mod(grad, hess)
            elif direcao_iterativa == "newton":
                d = dir_newton(grad, hess)
            else:
                raise ValueError(
                    "Direção inicial inválida. Use 'newton', "
                    "'newton_modificado' ou 'gradiente'."
                )


        # Busca de passo usando
        alpha, d = achar_passo(p, x, grad, d, hess, condicao_passo, alpha0, rho, c, sigma1, sigma2, limit, alpha_max)

        x = x + alpha * d
        grad = p.grad(x)
        hess = p.hess(x)

        i += 1

    if np.all(np.abs(grad) <= e):
        print(f"Convergiu para o problema {p.nome}!")
        print(f"Número de Iterações: {i}")
    else:
        print("Atingiu limite de iterações!")

    print(f"Coordenadas encontradas {x}")
    print(f"Valor da função: {p.f(x):.3f}")
    print(f"Gradiente: {grad}")

    return x