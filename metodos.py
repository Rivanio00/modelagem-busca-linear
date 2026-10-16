import numpy as np
from base import Problema
from condicoes import armijo
from problemas import TP6, TP7, TP12, TP15
from direcoes import dir_gradiente, dir_newton, dir_newton_mod

E = 1e-4
K_LIMIT = 100

def newton(p: Problema, e: float = E, k_limit: int = K_LIMIT):
    x = p.x0
    grad = p.grad(x)
    hess = p.hess(x)
    d = dir_newton(grad, hess)
    mod = True if np.dot(grad, d) >= 0 else False
    if mod: d = dir_newton_mod(grad, hess)

    i = 0

    while not (np.all(np.abs(grad) <= e)) or i > k_limit:

        if i > 0:
            #se fora da vizinhança de convexidade, usar newton modificado
            d = dir_newton_mod(grad, hess) if mod else dir_newton(grad, hess)

        #Procurando passo usando Armijo
        alpha = armijo(p, x, grad, d)
        x = x + alpha * d
        grad = p.grad(x)
        hess = p.hess(x)
        i += 1

    if i <= k_limit:
        print(f"Método convergiu para o problema {p.nome}!")
        print(f"Número de Iterações: {i}")
    else:
        print("Método atingiu limite de iterações!")
    print(f"Coordenadas encontradas {x}")
    print(f"Valor da função: {p.f(x):.3f}")
    print(f"Gradiente: {grad}")

def f_teste(x):
    return x[0]**2 + 2*x[1]**2

def g_teste(x):
    return np.array([2*x[0], 4*x[1]])

def h_teste(x):
    return np.array([[2, 0],
                     [0, 4]])

p_teste = Problema(
    nome="TESTE",
    f=f_teste,
    grad=g_teste,
    hess=h_teste,
    x0=np.array([100.0, -100.0])
)

newton(TP7)