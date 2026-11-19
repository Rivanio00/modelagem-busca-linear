import numpy as np
from base import Problema
from condicoes import achar_passo


def gradiente_conjugado(
    p: Problema,
    x0: np.ndarray = None,
    err: float = 1e-5,
) -> dict:
    """
    Executa o Método do Gradiente Conjugado
    com Polak-Ribiere Plus (PR+).
    """

    x = p.x0.copy() if x0 is None else np.array(x0, dtype=float).copy()

    f_atual = float(p.f(x))
    grad = p.grad(x)

    d = -grad

    trajetoria_x = [x.copy()]
    trajetoria_f = [f_atual]

    status = "Max Iter"
    i = 0

    while i < 1000:  # limite de itreações
        norma_grad = float(np.linalg.norm(grad))

        if norma_grad <= err:
            status = "Convergiu (Gradiente)"
            break

        # Busca linear
        if float(grad.T @ d) >= 0:
            d = -grad
        t, d = achar_passo(p, x, grad, d, None, "armijo", 1.0, 0.5, 1e-4, 1e-4, 0.9, 100, 1e6)

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

        # Critério de parada por variação relativa de f
        if abs(f_prox - f_atual) / max(1.0, abs(f_atual)) <= 1e-7:
            x, f_atual, grad = x_prox, f_prox, grad_prox
            status = "Convergiu (f)"
            break

        # Cálculo de Polak-Ribiere
        dif_grad = grad_prox - grad

        denom_beta = float(grad.T @ grad)

        beta_pr = float(grad_prox.T @ dif_grad) / denom_beta

        beta = max(0.0, beta_pr)

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