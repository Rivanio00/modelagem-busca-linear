import numpy as np
from tabulate import tabulate
from problemas import TP6, TP7, TP12, TP15
from metodos import gradiente_classico, sr1

try:
    from metodos import polak_ribiere
    METODOS = [gradiente_classico, sr1, polak_ribiere]
except ImportError:
    METODOS = [gradiente_classico, sr1]


def gerar_ponto_refletido(x0_a: np.ndarray) -> np.ndarray:
    """
    Aplica a regra de simetria refletida
    x0_B = -x0_A, ou (-1, ..., -1)^T caso x0_A seja a origem nula
    """
    if np.allclose(x0_a, 0.0):
        return -np.ones_like(x0_a, dtype=float)
    return -x0_a.astype(float)


def formatar_vetor(v: np.ndarray) -> str:
    return "[" + ", ".join(f"{val:.4f}" for val in v) + "]"


def executar_bateria():
    problemas = [TP6, TP7, TP12, TP15]
    resultados_tabela = []

    print("=" * 105)
    print("EXECUTANDO BATERIA DE EXPERIMENTOS — SIMETRIA REFLETIDA (BACIAS DE ATRAÇÃO)")
    print("=" * 105)

    for prob in problemas:
        pontos_iniciais = [
            ("Padrão (x0_A)", prob.x0.copy()),
            ("Refletido (x0_B)", gerar_ponto_refletido(prob.x0)),
        ]

        for rotulo_ponto, x0 in pontos_iniciais:
            for metodo_fn in METODOS:
                res = metodo_fn(prob, x0=x0)

                resultados_tabela.append([
                    prob.nome,
                    rotulo_ponto,
                    formatar_vetor(x0),
                    res["metodo"],
                    res["iteracoes"],
                    formatar_vetor(res["x_final"]),
                    f"{res['f_final']:.6e}",
                    f"{res['norma_grad']:.2e}",
                    res["status"],
                ])

    cabecalhos = [
        "Problema",
        "Ponto Inicial",
        "x0",
        "Método",
        "Iterações",
        "x_final",
        "f(x_final)",
        "||grad f||",
        "Status",
    ]

    tabela_md = tabulate(resultados_tabela, headers=cabecalhos, tablefmt="github")
    print("\n" + tabela_md + "\n")

    caminho_saida = "docs/tabela_24_experimentos.md"
    with open(caminho_saida, "w", encoding="utf-8") as f:
        f.write("# Resultados dos Experimentos — Métodos Multidimensionais e Simetria Refletida\n\n")
        f.write(tabela_md + "\n")

    print(f"[OK] Tabela salva em '{caminho_saida}' ({len(resultados_tabela)} execuções concluídas).")


if __name__ == "__main__":
    executar_bateria()