import numpy as np
from tabulate import tabulate
from problemas import TP6, TP7, TP12, TP15
from metodos import gradiente_classico, sr1

try:
    from metodos.gradiente_conjugado import gradiente_conjugado
    METODOS = [gradiente_classico, sr1, gradiente_conjugado]
except ImportError:
    METODOS = [gradiente_classico, sr1]


def gerar_ponto_refletido(x0_a: np.ndarray) -> np.ndarray:
    """
    Aplica a regra de simetria refletida (Seção 3.1):
    x0_B = -x0_A, ou (-1, ..., -1)^T caso x0_A seja a origem nula.
    """
    x0_flat = np.ravel(x0_a).astype(float)
    if np.allclose(x0_flat, 0.0):
        return -np.ones_like(x0_flat, dtype=float)
    return -x0_flat


def formatar_vetor(v: np.ndarray) -> str:
    """Achata o vetor e garante saída em linha única sem quebras."""
    v_flat = np.ravel(v)
    return "[" + ", ".join(f"{float(val):.4f}" for val in v_flat) + "]"


def limpar_celula(valor) -> str:
    """Remove quebras de linha e escapa pipes para não quebrar tabelas Markdown."""
    return str(valor).replace("\n", " ").replace("\r", " ").replace("|", "/").strip()


def executar_bateria():
    problemas = [TP6, TP7, TP12, TP15]
    resultados_tabela = []

    print("=" * 105)
    print("EXECUTANDO BATERIA DE EXPERIMENTOS — SIMETRIA REFLETIDA (BACIAS DE ATRAÇÃO)")
    print("=" * 105)

    for prob in problemas:
        pontos_iniciais = [
            ("Padrão (x0_A)", np.ravel(prob.x0).copy()),
            ("Refletido (x0_B)", gerar_ponto_refletido(prob.x0)),
        ]

        for rotulo_ponto, x0 in pontos_iniciais:
            for metodo_fn in METODOS:
                res = metodo_fn(prob, x0=x0)

                linha = [
                    prob.nome,
                    rotulo_ponto,
                    formatar_vetor(x0),
                    res["metodo"],
                    res["iteracoes"],
                    formatar_vetor(res["x_final"]),
                    f"{float(res['f_final']):.6e}",
                    f"{float(res['norma_grad']):.2e}",
                    res["status"],
                ]
                resultados_tabela.append([limpar_celula(c) for c in linha])

    cabecalhos = [
        "Problema",
        "Ponto Inicial",
        "x0",
        "Método",
        "Iterações",
        "x_final",
        "f(x_final)",
        "‖grad f‖",
        "Status",
    ]

    tabela_md = tabulate(resultados_tabela, headers=cabecalhos, tablefmt="github")
    print("\n" + tabela_md + "\n")

    caminho_saida = "docs/tabela_24_experimentos.md"
    with open(caminho_saida, "w", encoding="utf-8", newline="\n") as f:
        f.write("# Resultados dos Experimentos — Métodos Multidimensionais e Simetria Refletida\n\n")
        f.write(f"Total de execuções realizadas: **{len(resultados_tabela)}**\n\n")
        f.write(tabela_md)
        f.write("\n")

    print(f"[OK] Tabela salva em '{caminho_saida}' ({len(resultados_tabela)} execuções concluídas).")


if __name__ == "__main__":
    executar_bateria()