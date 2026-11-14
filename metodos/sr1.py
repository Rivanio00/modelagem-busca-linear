import numpy as np
from base import Problema
from condicoes import achar_passo


def sr1(
    p: Problema,
    x0: np.ndarray = None,
    tol_grad: float = 1e-5,
    tol_f: float = 1e-7,
    k_limit: int = 1000,
    r_salvaguarda: float = 1e-8,
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
    Executa o Método Quase-Newton SR1 com Salvaguarda.
    """
    x = p.x0.copy() if x0 is None else np.array(x0, dtype=float).copy()
    n = len(x)
    B = np.eye(n, dtype=float)

    f_atual = float(p.f(x))
    grad = p.grad(x)

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

        # Resolve B_k * d_k = -grad_k para obter a direção Quase-Newton
        try:
            d = np.linalg.solve(B, -grad)
            # Checagem de descida: se B_k perdeu definibilidade positiva, reinicia
            if np.dot(grad, d) >= -1e-12 * norma_grad * np.linalg.norm(d):
                B = np.eye(n, dtype=float)
                d = -grad
        except np.linalg.LinAlgError:
            B = np.eye(n, dtype=float)
            d = -grad

        # Busca linear
        try:
            alpha, d = achar_passo(
                p, x, grad, d, B,
                condicao_passo, alpha0, rho, c, sigma1, sigma2, limit, alpha_max
            )
        except RuntimeError:
            status = "Falha (Busca Linear)"
            break

        x_prox = x + alpha * d
        f_prox = float(p.f(x_prox))
        grad_prox = p.grad(x_prox)

        if not np.isfinite(f_prox) or not np.all(np.isfinite(grad_prox)):
            status = "Falha (Overflow/NaN)"
            break

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

        # Atualização SR1 com Salvaguarda
        s_k = x_prox - x
        y_k = grad_prox - grad
        diff = y_k - B @ s_k

        norm_s = float(np.linalg.norm(s_k))
        norm_diff = float(np.linalg.norm(diff))
        denom = float(np.dot(s_k, diff))

        if norm_s > 0 and norm_diff > 0 and abs(denom) >= r_salvaguarda * norm_s * norm_diff:
            B = B + np.outer(diff, diff) / denom

        x, f_atual, grad = x_prox, f_prox, grad_prox

    return {
        "metodo": "SR1",
        "x_final": x,
        "f_final": f_atual,
        "norma_grad": float(np.linalg.norm(grad)),
        "iteracoes": i,
        "status": status,
        "trajetoria_x": trajetoria_x,
        "trajetoria_f": trajetoria_f,
    }