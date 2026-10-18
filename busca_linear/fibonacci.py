import numpy as np


def enquadrar_intervalo(phi, step_inicial=0.01, fator=2.0, max_iter=50):
  """Encontra um intervalo [0, b] inicial onde phi apresente reducao."""
  a = 0.0 # ponto inicial
  h = step_inicial # tamamnho do passo
  b = a + h # primeiro ponto a partir do passo

  if phi(b) >= phi(a): # passo muito longo ultrapassou a região de queda da função
    return a, b

  phi_atual = phi(b) # temos que phi(b) < phi(a)
  for _ in range(max_iter):
    b_proximo = b + h * fator # calculamos a cada iteração um novo ponto
    phi_proximo = phi(b_proximo)
    if phi_proximo > phi_atual: # mínimo local está inserido no intervalo
      return a, b_proximo

    # trocamos para o novo ponto
    b = b_proximo
    phi_atual = phi_proximo
    h *= fator # mudamos o tamanho do passo

  return a, b


def busca_fibonacci(phi, tol=1e-4, max_eval=30):
  """Método de busca linear direta via Sequência de Fibonacci."""
  # intervalo inicial [a, b]
  a, b = enquadrar_intervalo(phi)
  L0 = b - a # tamanmho do intervalo

  # Gerar a sequencia até cobrir a tolerancia (ou >= max_eval)
  F = [1, 1]
  while (L0 / F[-1]) > tol and len(F) < max_eval:
    # F[-1] == ultimo elemento do vetor
    # F[-2] == penultimo elemento do vetor
    F.append(F[-1] + F[-2]) # Adiciona no final do vetor mais um termo da sequencia

  N = len(F) - 1 # Índice do último elemento F[N]

  # Caso o intervalo inicial seja menor que a tolerância
  if N < 2:
    return (a + b) / 2.0, {
        "a_final": a,
        "b_final": b,
        "num_iter": 0,
        "phi_star": phi((a + b) / 2.0),
    }

  # Pontos internos iniciais
  lambda_k = a + (F[N - 2] / F[N]) * (b - a)
  mu_k = a + (F[N - 1] / F[N]) * (b - a)

  f_lambda = phi(lambda_k)
  f_mu = phi(mu_k)

# Redução do intervalo de busca
  for k in range(1, N - 1):
    if f_lambda > f_mu:  # O ponto de mínimo está no intervalo [lambda_k, b]
      a = lambda_k  # O novo limite esquerdo passa a ser lambda_k
      lambda_k = mu_k  # O mu_k antigo é reaproveitado como novo lambda_k
      f_lambda = f_mu
      mu_k = a + (
          F[N - k - 1] / F[N - k]
      ) * (
          b - a
      )  # Calculamos apenas o novo ponto mu_k
      f_mu = phi(mu_k)
    else:  # O ponto de mínimo está no intervalo [a, mu_k]
      b = mu_k  # O novo limite direito passa a ser mu_k
      mu_k = lambda_k  # O lambda_k antigo é reaproveitado como novo mu_k
      f_mu = f_lambda
      lambda_k = a + (
          F[N - k - 2] / F[N - k]
      ) * (
          b - a
      )  # Calculamos apenas o novo ponto lambda_k
      f_lambda = phi(lambda_k)

  alpha_star = (a + b) / 2.0
  return alpha_star, {
      "a_final": a,
      "b_final": b,
      "num_iter": N - 1,
      "phi_star": phi(alpha_star),
  }