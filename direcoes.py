import numpy as np

# Parametros da busca por mu
MU_INICIAL = 1e-3
FATOR = 10.0
MU_MAX = 1e8


def dir_gradiente(g, H):
    """d_G = -grad f(x0) hessiana nao e usada"""
    return -g


def dir_newton(g, H):
    """d_N = -H^{-1} g. retorna None se H for singular"""
    try:
        return -np.linalg.solve(H, g)
    except np.linalg.LinAlgError:
        return None


def escolher_mu(H):
    """Menor mu da sequencia 0, 1e-3, 1e-2, ... para q H + mu*I seja definida positiva

    o teste e a fatoracao de Cholesky: ela so existe para matrizes definidas positivas
    """
    n = H.shape[0]
    mu = 0.0
    while mu <= MU_MAX:
        try:
            np.linalg.cholesky(H + mu * np.eye(n))
            return mu
        except np.linalg.LinAlgError:
            mu = MU_INICIAL if mu == 0.0 else mu * FATOR
    raise ValueError("Nao foi possivel tornar H + mu*I definida positiva")


def dir_newton_mod(g, H):
    """d_M = -(H + mu*I)^{-1} g, com mu escolhido por escolher_mu"""
    mu = escolher_mu(H)
    n = H.shape[0]
    return -np.linalg.solve(H + mu * np.eye(n), g)


def eh_descida(g, d):
    """True se g^T d < 0 uma direcao indefinida (None) conta como falha"""
    if d is None:
        return False
    return (g @ d) < 0