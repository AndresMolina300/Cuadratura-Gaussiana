# Tutorial de uso (paso a paso, con LaTeX)

Este proyecto implementa **cuadratura gaussiana de Legendre** para aproximar la integral

\[
I=\int_{1}^{3}\bigl(x^6 - x^2\sin(2x)\bigr)\,dx.
\]

A continuación se muestra el flujo completo que sigue el programa.

## 1) Definir la función a integrar
Sea
\[
f(x)=x^6 - x^2\sin(2x).
\]

En el código de Python, se implementa como una función `f(x)`.

## 2) Transformar el intervalo \([1,3]\) a \([-1,1]\)
La cuadratura de Gauss-Legendre trabaja de forma canónica en \([-1,1]\). Para un intervalo \([a,b]\) usamos el cambio de variable
\[
x(t)=\frac{b-a}{2}\,t+\frac{a+b}{2},\qquad t\in[-1,1],
\]
con
\[
dx=\frac{b-a}{2}\,dt.
\]
En nuestro caso \(a=1,\; b=3\), por lo que
\[
x(t)=\frac{3-1}{2}\,t+\frac{3+1}{2}=t+2,\qquad dx=\frac{3-1}{2}\,dt=1\,dt.
\]

## 3) Fórmula de cuadratura
La aproximación con \(N\) puntos (nodos \(t_i\) y pesos \(w_i\) de Legendre en \([-1,1]\)) es
\[
\int_a^b f(x)\,dx \;\approx\; \frac{b-a}{2}\sum_{i=1}^{N} w_i\, f\!\bigl(x(t_i)\bigr).
\]
Para \([1,3]\) esto queda
\[
I \;\approx\; \frac{3-1}{2}\sum_{i=1}^{N} w_i\, f\!\bigl(t_i+2\bigr)\;=\;\sum_{i=1}^{N} w_i\, f(t_i+2).
\]

## 4) Algoritmo (qué hace el script)
1. **Calcula** nodos \(\{t_i\}_{i=1}^N\) y pesos \(\{w_i\}_{i=1}^N\) de Legendre en \([-1,1]\).
2. **Evalúa** \(f\) en los puntos transformados \(x_i=t_i+2\).
3. **Acumula** la suma \(\displaystyle \sum_{i=1}^{N} w_i\, f(x_i)\).
4. **Imprime** el valor aproximado de \(I\) para el \(N\) usado.
