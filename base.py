from dataclasses import dataclass
from typing import Callable
import numpy as np


@dataclass
class Problema:
    nome: str
    f: Callable[[np.ndarray], float]    # funcao + numero, ex: f6
    grad: Callable[[np.ndarray], np.ndarray]    # vetor gradiente
    hess: Callable[[np.ndarray], np.ndarray]    # vetor hessiana
    x0: np.ndarray  # ponto inicial


def make_phi(p, x0, d):
    """Devolve (phi, dphi, d2phi), funcoes de alpha ao longo de x0 + alpha*d"""
    x0 = np.asarray(x0, dtype=float)   # ponto inicial 
    d = np.asarray(d, dtype=float)  # direcao de descida

    def phi(a):
        return p.f(x0 + a * d)  # f no ponto seguinte

    def dphi(a):
        return p.grad(x0 + a * d) @ d   #  gradiente no ponto seguinte

    def d2phi(a):
        return d @ p.hess(x0 + a * d) @ d   # hessiana no ponto seguinte

    return phi, dphi, d2phi