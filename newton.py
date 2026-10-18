import numpy as np
from base import Problema
from condicoes import armijo, wolfe
from problemas import TP6, TP7, TP12, TP15
from direcoes import dir_gradiente, dir_newton, dir_newton_mod

E = 1e-4
K_LIMIT = 100

def newton(
    p: Problema,
    e: float = E,
    k_limit: int = K_LIMIT,
    direcao_inicial: str = "newton"
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
            d = dir_newton(grad, hess)

        # Busca de passo usando Armijo
        alpha, d = armijo(p, x, grad, d, hess)

        x = x + alpha * d
        grad = p.grad(x)
        hess = p.hess(x)

        i += 1

    if np.all(np.abs(grad) <= e):
        print(f"Newton convergiu para o problema {p.nome}!")
        print(f"Número de Iterações: {i}")
    else:
        print("Newton atingiu limite de iterações!")

    print(f"Coordenadas encontradas {x}")
    print(f"Valor da função: {p.f(x):.3f}")
    print(f"Gradiente: {grad}")

    return x

newton(TP7, direcao_inicial="gradiente")