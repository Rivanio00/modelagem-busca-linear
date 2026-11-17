import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import numpy as np
from base import Problema
from problemas import TP6

def gradiente_conjugado(
    p: Problema,
    x0: np.ndarray = None,
    err: float = 1e-5,
) -> dict:
    """
    Executa o Método do Gradiente Conjugado
    com Polak-Ribiere para atualização da direção
    """

    x = p.x0.copy() if x0 is None else np.array(x0, dtype=float).copy()

    f_atual = float(p.f(x))
    grad = p.grad(x)
    hess = p.hess(x)

    d = -grad
    n = len(x)

    trajetoria_x = [x.copy()]
    trajetoria_f = [f_atual]

    status = "Max Iter"
    i = 0

    while i < n:
        norma_grad = float(np.linalg.norm(grad))

        if norma_grad <= err:
            status = "Convergiu (Gradiente)"
            break

        A = hess

        # Cálculo do passo
        denominador = float(d.T @ A @ d)

        if denominador <= 0:
            status = "Falha (Direção não positiva)"
            break

        t = -float(grad.T @ d) / denominador

        x_prox = x + t * d

        f_prox = float(p.f(x_prox))
        grad_prox = p.grad(x_prox)

        trajetoria_x.append(x_prox.copy())
        trajetoria_f.append(f_prox)

        i += 1

        if float(np.linalg.norm(grad_prox)) <= err:
            x, f_atual, grad = x_prox, f_prox, grad_prox
            status = "Convergiu (Gradiente)"
            break

        # Cálculo de Polak-Ribiere
        dif_grad = grad_prox - grad

        denom_beta = float(grad.T @ grad)

        beta = float(grad_prox.T @ dif_grad) / denom_beta

        d_prox = -grad_prox + beta * d

        x, f_atual, grad, d = (
            x_prox,
            f_prox,
            grad_prox,
            d_prox
        )

    return {
        "metodo": "Gradiente Conjugado",
        "x_final": x,
        "f_final": f_atual,
        "norma_grad": float(np.linalg.norm(grad)),
        "iteracoes": i,
        "status": status,
        "trajetoria_x": trajetoria_x,
        "trajetoria_f": trajetoria_f,
    }

print(gradiente_conjugado(TP6))