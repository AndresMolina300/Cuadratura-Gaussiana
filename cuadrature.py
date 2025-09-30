"""Módulo de cuadratura gaussiana de Legendre para integrar en [a,b]."""

from typing import Callable, Tuple
import math
import numpy as np

def gauss_legendre_nodes_weights(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """Devuelve los nodos y pesos de Gauss-Legendre en [-1, 1].

    Examples:
        >>> nodes, weights = gauss_legendre_nodes_weights(3)
        >>> len(nodes), len(weights)
        (3, 3)

    Args:
        N (int): Número de puntos de cuadratura (N >= 1).

    Returns:
        Tuple[np.ndarray, np.ndarray]: Arreglos con nodos y pesos.
    """
    if N < 1:
        raise ValueError("N debe ser >= 1")
    nodes, weights = np.polynomial.legendre.leggauss(N)
    return nodes, weights


def scale_interval(a: float, b: float,
                   nodes: np.ndarray,
                   weights: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Escala nodos y pesos de [-1,1] al intervalo [a,b].

    Examples:
        >>> n, w = scale_interval(1.0, 3.0, np.array([-1.0, 1.0]), np.array([1.0, 1.0]))
        >>> float(n.min()) >= 1.0 and float(n.max()) <= 3.0
        True

    Args:
        a (float): Límite inferior del intervalo.
        b (float): Límite superior del intervalo.
        nodes (np.ndarray): Nodos en [-1,1].
        weights (np.ndarray): Pesos en [-1,1].

    Returns:
        Tuple[np.ndarray, np.ndarray]: Nodos y pesos re-escalados a [a,b].
    """
    half = 0.5 * (b - a)
    mid  = 0.5 * (a + b)
    new_nodes = half * nodes + mid
    new_weights = half * weights
    return new_nodes, new_weights


def gaussian_quadrature(f: Callable[[float], float],
                        a: float, b: float, N: int) -> float:
    """Aproxima \\(\\int_a^b f(x)\\,dx\\) usando cuadratura gaussiana de N puntos.

    Examples:
        >>> f = lambda x: x**2
        >>> round(gaussian_quadrature(f, 0.0, 1.0, 2), 6)
        0.333333

    Args:
        f (Callable[[float], float]): Función escalar a integrar.
        a (float): Límite inferior.
        b (float): Límite superior.
        N (int): Número de puntos de cuadratura.

    Returns:
        float: Aproximación de la integral en [a,b].
    """
    nodes, weights = gauss_legendre_nodes_weights(N)
    nodes, weights = scale_interval(a, b, nodes, weights)
    # Evaluamos de forma segura si f no está vectorizada
    vals = np.array([f(float(x)) for x in nodes], dtype=float)
    return float(np.sum(weights * vals))


if __name__ == "__main__":
    # Ejemplo mínimo: integra f(x) = x^6 - x^2 sin(2x) en [1,3]
    def f(x: float) -> float:
        return x**6 - x**2 * math.sin(2.0*x)

    a, b = 1.0, 3.0
    for N in [2, 3, 4, 5, 6, 8, 10]:
        I = gaussian_quadrature(f, a, b, N)
        print(f"N={N:2d}  I≈ {I:.12f}")
