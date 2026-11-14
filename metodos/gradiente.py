import numpy as np
from base import Problema
from condicoes import achar_passo


def gradiente_classico(
    p: Problema,
    x0: np.ndarray = None,
    tol_grad: float = 1e-5,
    tol_f: float = 1e-7,
    k_limit: int = 1000,
    condicao_passo: str = "armijo",
    alpha0: float = 1.0,
    rho: float = 0.5,
    c: float = 1e-4,
    sigma1: float = 1e-4,
    sigma2: float = 0.9,
    limit: int = 100,
    alpha_max: float = 1e6,
) -> dict:
    """
    Executa o Método do Gradiente Clássico
    """
    x = p.x0.copy() if x0 is None else np.array(x0, dtype=float).copy()
    f_atual = float(p.f(x))
    grad = p.grad(x)
    hess = p.hess(x)

    trajetoria_x = [x.copy()]
    trajetoria_f = [f_atual]
    status = "Max Iter"
    i = 0

    while i < k_limit:
        norma_grad = float(np.linalg.norm(grad))

        # Critério 1: Norma Euclidiana do gradiente <= 1e-5
        if norma_grad <= tol_grad:
            status = "Convergiu (Gradiente)"
            break

        # Direção de descida
        d = -grad

        # Busca linear
            alpha, d = achar_passo(
                p, x, grad, d, hess,
                condicao_passo, alpha0, rho, c, sigma1, sigma2, limit, alpha_max
            )
        except RuntimeError:
            status = "Falha (Busca Linear)"
            break

        x_prox = x + alpha * d
        f_prox = float(p.f(x_prox))
        grad_prox = p.grad(x_prox)

        trajetoria_x.append(x_prox.copy())
        trajetoria_f.append(f_prox)
        i += 1

        # Critério 1 pós-passo
        if float(np.linalg.norm(grad_prox)) <= tol_grad:
            x, f_atual, grad = x_prox, f_prox, grad_prox
            status = "Convergiu (Gradiente)"
            break

        # Critério 2: Variação relativa de f <= 1e-7
        if abs(f_prox - f_atual) / max(1.0, abs(f_atual)) <= tol_f:
            x, f_atual, grad = x_prox, f_prox, grad_prox
            status = "Convergiu (f)"
            break

        x, f_atual, grad = x_prox, f_prox, grad_prox
        hess = p.hess(x)

    return {
        "metodo": "Gradiente Clássico",
        "x_final": x,
        "f_final": f_atual,
        "norma_grad": float(np.linalg.norm(grad)),
        "iteracoes": i,
        "status": status,
        "trajetoria_x": trajetoria_x,
        "trajetoria_f": trajetoria_f,
    }