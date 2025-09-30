# Explicación del método

La **cuadratura gaussiana** es un método numérico para aproximar integrales
definidas mediante una combinación lineal de los valores de la función en
ciertos puntos especiales (llamados *nodos*). Estos nodos y los coeficientes
de ponderación (*pesos*) se obtienen a partir de los polinomios de Legendre.

La idea principal es transformar una integral en un intervalo arbitrario
\([a, b]\) a la integral estándar en \([-1, 1]\), usando el cambio de variable:

\[
x = \frac{b-a}{2} \, t + \frac{b+a}{2}
\]

donde \(t \in [-1, 1]\). Con esta transformación, la integral queda:

\[
\int_a^b f(x) \, dx = \frac{b-a}{2} \int_{-1}^1 f\!\left(\tfrac{b-a}{2}t + \tfrac{b+a}{2}\right) dt
\]

y luego se aproxima con:

\[
\int_a^b f(x)\,dx \approx \frac{b-a}{2} \sum_{i=1}^N w_i f(x_i)
\]

donde:
- \(x_i\) son los nodos de Legendre transformados al intervalo \([a,b]\),
- \(w_i\) son los pesos correspondientes,
- \(N\) es el número de puntos de cuadratura.

Este método es especialmente eficiente porque con relativamente pocos puntos
logra una alta precisión en la aproximación de integrales polinómicas y de
otras funciones suaves.
