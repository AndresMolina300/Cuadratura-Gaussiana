import numpy as np

def integrando(x: float) -> float:
    """
    Calcula el valor de la función a integrar.

    La función es:
    f(x) = x^6 - x^2 * sin(2x)

    Args:
        x (float): Punto donde se evalúa la función.

    Returns:
        float: Valor de f(x).

    Examples:
        >>> integrando(1.0)
        1.0 - 1.0 * sin(2.0)
    """
    return x**6 - x**2 * np.sin(2*x)


def sum_riemann(N: int, a: float, b: float) -> float:
    """
    Calcula la aproximación de la integral definida usando
    cuadratura gaussiana con N nodos de Legendre.

    Args:
        N (int): Número de nodos de cuadratura.
        a (float): Límite inferior del intervalo.
        b (float): Límite superior del intervalo.

    Returns:
        float: Aproximación numérica de la integral en [a,b].

    Examples:
        >>> sum_riemann(2, 1.0, 3.0)
        Aproximación numérica (valor aproximado).
    """
    # Obtener nodos y pesos de Legendre en [-1, 1]
    t, w = np.polynomial.legendre.leggauss(N)

    # Cambio de variable para llevar [a,b] a [-1,1]
    x = 0.5 * (b - a) * t + 0.5 * (a + b)
    dx = 0.5 * (b - a)

    # Suma ponderada
    return np.sum(w * integrando(x)) * dx
