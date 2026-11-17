# Resultados dos Experimentos — Métodos Multidimensionais e Simetria Refletida

| Problema   | Ponto Inicial    | x0                 | Método                  |   Iterações | x_final            |     f(x_final) |    ||grad f|| | Status                        |
|------------|------------------|--------------------|-------------------------|-------------|--------------------|----------------|---------------|-------------------------------|
| TP6        | Padrão (x0_A)    | [-4.0000, -2.0000] | Gradiente Clássico      |           2 | [1.0000, 0.0000]   |   -0.5         |      0        | Convergiu (Gradiente)         |
| TP6        | Padrão (x0_A)    | [-4.0000, -2.0000] | SR1                     |           2 | [1.0000, 0.0000]   |   -0.5         |      0        | Convergiu (Gradiente)         |
| TP6        | Padrão (x0_A)    | [-4.0000, -2.0000] | Gradiente Conjugado PR+ |           2 | [1.0000, 0.0000]   |   -0.5         |      6.66e-16 | Convergiu (Gradiente)         |
| TP6        | Refletido (x0_B) | [4.0000, 2.0000]   | Gradiente Clássico      |           2 | [1.0000, 0.0000]   |   -0.5         |      0        | Convergiu (Gradiente)         |
| TP6        | Refletido (x0_B) | [4.0000, 2.0000]   | SR1                     |           2 | [1.0000, 0.0000]   |   -0.5         |      0        | Convergiu (Gradiente)         |
| TP6        | Refletido (x0_B) | [4.0000, 2.0000]   | Gradiente Conjugado PR+ |           2 | [1.0000, 0.0000]   |   -0.5         |      2.22e-16 | Convergiu (Gradiente)         |
| TP7        | Padrão (x0_A)    | [15.0000, -2.0000] | Gradiente Clássico      |        1000 | [5.7261, 3.9880]   |    0.764258    |      2.97     | Max Iter                      |
| TP7        | Padrão (x0_A)    | [15.0000, -2.0000] | SR1                     |          12 | [5.0000, 4.0000]   |    1.92518e-16 |      1.2e-06  | Convergiu (Gradiente)         |
| TP7        | Padrão (x0_A)    | [15.0000, -2.0000] | Gradiente Conjugado PR+ |           2 | [14.9517, -0.8791] |   70.8283      |    173        | Max Iter                      |
| TP7        | Refletido (x0_B) | [-15.0000, 2.0000] | Gradiente Clássico      |        1000 | [5.1605, 3.9974]   |    0.037428    |      0.77     | Max Iter                      |
| TP7        | Refletido (x0_B) | [-15.0000, 2.0000] | SR1                     |          10 | [5.0000, 4.0000]   |    1.59422e-21 |      2.18e-09 | Convergiu (Gradiente)         |
| TP7        | Refletido (x0_B) | [-15.0000, 2.0000] | Gradiente Conjugado PR+ |           0 | [-15.0000, 2.0000] | 4000           |    506        | Falha (Hessiana não positiva) |
| TP12       | Padrão (x0_A)    | [1.0000, 1.0000]   | Gradiente Clássico      |          14 | [3.0000, 2.0000]   |    1.82335e-08 |      0.00168  | Convergiu (f)                 |
| TP12       | Padrão (x0_A)    | [1.0000, 1.0000]   | SR1                     |           8 | [3.0000, 2.0000]   |    6.23804e-18 |      2.99e-08 | Convergiu (Gradiente)         |
| TP12       | Padrão (x0_A)    | [1.0000, 1.0000]   | Gradiente Conjugado PR+ |           0 | [1.0000, 1.0000]   |  106           |     59.7      | Falha (Hessiana não positiva) |
| TP12       | Refletido (x0_B) | [-1.0000, -1.0000] | Gradiente Clássico      |          11 | [-3.7793, -3.2832] |    2.86104e-10 |      0.000276 | Convergiu (f)                 |
| TP12       | Refletido (x0_B) | [-1.0000, -1.0000] | SR1                     |          10 | [-3.7793, -3.2832] |    2.30307e-13 |      6.15e-06 | Convergiu (Gradiente)         |
| TP12       | Refletido (x0_B) | [-1.0000, -1.0000] | Gradiente Conjugado PR+ |           0 | [-1.0000, -1.0000] |  170           |     30.6      | Falha (Hessiana não positiva) |
| TP15       | Padrão (x0_A)    | [-1.2000, 1.0000]  | Gradiente Clássico      |         429 | [1.0000, 1.0000]   |    9.0737e-05  |  14700        | Convergiu (f)                 |
| TP15       | Padrão (x0_A)    | [-1.2000, 1.0000]  | SR1                     |          40 | [1.0000, 1.0000]   |    1.66957e-05 | 129000        | Convergiu (f)                 |
| TP15       | Padrão (x0_A)    | [-1.2000, 1.0000]  | Gradiente Conjugado PR+ |           2 | [-4.7901, 1.8535]  |    5.16213     |      1.15     | Max Iter                      |
| TP15       | Refletido (x0_B) | [1.2000, -1.0000]  | Gradiente Clássico      |         399 | [1.0000, -1.0000]  |    7.10407e-05 |  19200        | Convergiu (f)                 |
| TP15       | Refletido (x0_B) | [1.2000, -1.0000]  | SR1                     |          42 | [1.0000, -1.0000]  |    5.31212e-07 |      1.02e+06 | Convergiu (f)                 |
| TP15       | Refletido (x0_B) | [1.2000, -1.0000]  | Gradiente Conjugado PR+ |           0 | [1.2000, -1.0000]  |    0.814448    |      4.23     | Falha (Hessiana não positiva) |
