"""Roda os testes.

  python -m testes              # todos
  python -m testes direcoes     # so os modulos cujo nome contem "direcoes"
"""
import importlib
import sys
import time

from testes.utils import CONTAGEM

MODULOS = [
    "testes.teste_problemas",
    "testes.teste_phi",
    "testes.teste_direcoes",
    "testes.teste_derivadas",
]


def main():
    filtros = sys.argv[1:]
    modulos = [m for m in MODULOS if not filtros or any(f in m for f in filtros)]
    total, falhas = 0, []
    inicio = time.perf_counter()

    for nome_mod in modulos:
        curto = nome_mod.split(".")[-1]
        mod = importlib.import_module(nome_mod)
        print("\n" + "=" * 64)
        print(f" {curto}")
        print("=" * 64)
        for nome, fn in vars(mod).items():
            if not (nome.startswith("test_") and callable(fn)):
                continue
            total += 1
            print(f"\n  > {nome}")
            try:
                fn()
            except AssertionError:
                falhas.append(f"{curto}::{nome}")
                print("  -> FALHOU")
            except Exception as e:
                falhas.append(f"{curto}::{nome}")
                print(f"  -> ERRO ({type(e).__name__}): {e}")
            else:
                print("  -> passou")

    tempo = time.perf_counter() - inicio
    print("\n" + "=" * 64)
    print(f" {total - len(falhas)}/{total} testes passaram"
          f" | verificacoes: {CONTAGEM['ok']} OK, {CONTAGEM['falha']} falharam"
          f" | {tempo:.2f}s")
    if falhas:
        print(" Falharam:")
        for f in falhas:
            print(f"   - {f}")
    print("=" * 64)
    sys.exit(1 if falhas else 0)


if __name__ == "__main__":
    main()