import numpy as np


def dir_gradiente(grad: np.ndarray, hess: np.ndarray = None) -> np.ndarray:
  return -grad