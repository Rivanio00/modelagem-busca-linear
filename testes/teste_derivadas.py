import numpy as np
from base import make_phi
from problemas import TP6, TP12
from testes.utils import (checar, grad_numerico, hess_numerica,
                          pontos_de_teste)

PROBLEMAS = [TP6, TP12]


def test_gradiente_vs_diferencas_finitas():
    for p in PROBLEMAS:
        pontos = pontos_de_teste(p)
        pior, falha = 0.0, None
        for x in pontos:
            g_an, g_num = p.grad(x), grad_numerico(p.f, x)
            pior = max(pior, np.max(np.abs(g_an - g_num)))
            if falha is None and not np.allclose(g_an, g_num, rtol=1e-5, atol=1e-4):
                falha = (x, g_an, g_num)
        print(f"    {p.nome}: {len(pontos)} pontos, maior erro absoluto = {pior:.2e}")
        detalhe = "" if falha is None else (
            f"x = {falha[0]}\nanalitico = {falha[1]}\nnumerico  = {falha[2]}")
        checar(falha is None, f"{p.nome}: gradiente analitico = numerico", detalhe)


def test_hessiana_vs_diferencas_finitas():
    for p in PROBLEMAS:
        pontos = pontos_de_teste(p)
        pior, falha = 0.0, None
        for x in pontos:
            H_an, H_num = p.hess(x), hess_numerica(p.grad, x)
            pior = max(pior, np.max(np.abs(H_an - H_num)))
            if falha is None and not np.allclose(H_an, H_num, rtol=1e-5, atol=1e-4):
                falha = (x, H_an, H_num)
        print(f"    {p.nome}: {len(pontos)} pontos, maior erro absoluto = {pior:.2e}")
        detalhe = "" if falha is None else (
            f"x = {falha[0]}\nanalitica =\n{falha[1]}\nnumerica =\n{falha[2]}")
        checar(falha is None, f"{p.nome}: Hessiana analitica = numerica", detalhe)


def test_hessiana_simetrica():
    for p in PROBLEMAS:
        pontos = pontos_de_teste(p)
        simetrica = all(np.allclose(p.hess(x), p.hess(x).T) for x in pontos)
        checar(simetrica, f"{p.nome}: Hessiana simetrica em {len(pontos)} pontos")


def test_derivadas_de_phi():
    rng = np.random.default_rng(7)
    for p in PROBLEMAS:
        pior = 0.0
        ok = True
        for _ in range(10):
            d = rng.uniform(-1, 1, size=len(p.x0))
            phi, dphi, d2phi = make_phi(p, p.x0, d)
            a, h = 0.05, 1e-6
            num1 = (phi(a + h) - phi(a - h)) / (2 * h)
            num2 = (dphi(a + h) - dphi(a - h)) / (2 * h)
            pior = max(pior, abs(dphi(a) - num1), abs(d2phi(a) - num2))
            ok = ok and np.isclose(dphi(a), num1, rtol=1e-5, atol=1e-4) \
                    and np.isclose(d2phi(a), num2, rtol=1e-5, atol=1e-4)
        print(f"    {p.nome}: 10 direcoes aleatorias, maior erro absoluto = {pior:.2e}")
        checar(ok, f"{p.nome}: phi' e phi'' analiticas = numericas")


def test_controle_detecta_gradiente_errado():
    """Controle: um gradiente propositalmente errado TEM que ser reprovado."""
    def grad12_errado(x):
        u = x[0]**2 + x[1] - 11
        v = x[0] + x[1]**2 - 7
        return np.array([4 * x[0] * u + 2 * v,
                         2 * u + 2 * x[1] * v])   # erro plantado: 2*x2*v em vez de 4*x2*v

    x = TP12.x0
    g_err, g_num = grad12_errado(x), grad_numerico(TP12.f, x)
    print(f"    gradiente errado = {g_err}, numerico = {g_num}")
    checar(not np.allclose(g_err, g_num, rtol=1e-5, atol=1e-4),
           "o teste reprova um gradiente errado (plantado de proposito)")