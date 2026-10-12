"""Auxiliares dos testes: verificacao com print e diferencas finitas."""
import numpy as np

CONTAGEM = {"ok": 0, "falha": 0}


def checar(condicao, descricao, detalhe=""):
    """Imprime o resultado de uma verificacao e levanta AssertionError se falhar."""
    if condicao:
        CONTAGEM["ok"] += 1
        print(f"    [OK]     {descricao}")
    else:
        CONTAGEM["falha"] += 1
        print(f"    [FALHOU] {descricao}")
        for linha in str(detalhe).splitlines():
            print(f"             {linha}")
        raise AssertionError(descricao)


def mostrar(rotulo, valor):
    """Imprime um valor (numero, vetor ou matriz) com formatacao limpa."""
    txt = np.array2string(np.asarray(valor), precision=6, suppress_small=True)
    print(f"    {rotulo} = {txt}")


def grad_numerico(f, x, h=1e-6):
    """Gradiente por diferenca central: (f(x+h e_i) - f(x-h e_i)) / (2h)."""
    x = np.asarray(x, dtype=float)
    g = np.zeros_like(x)
    for i in range(len(x)):
        e = np.zeros_like(x)
        e[i] = h
        g[i] = (f(x + e) - f(x - e)) / (2 * h)
    return g


def hess_numerica(grad, x, h=1e-5):
    """Hessiana por diferenca central DO GRADIENTE."""
    x = np.asarray(x, dtype=float)
    n = len(x)
    H = np.zeros((n, n))
    for i in range(n):
        e = np.zeros(n)
        e[i] = h
        H[:, i] = (grad(x + e) - grad(x - e)) / (2 * h)
    return H


def pontos_de_teste(p, quantidade=20, semente=42):
    """x0 do problema + pontos aleatorios em [-5, 5]^n (reproduzivel)."""
    rng = np.random.default_rng(semente)
    n = len(p.x0)
    return [p.x0] + [rng.uniform(-5, 5, size=n) for _ in range(quantidade)]