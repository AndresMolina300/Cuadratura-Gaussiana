# Introducción

## Contexto
La cuadratura gaussiana es un método numérico de integración que se utiliza
para aproximar integrales definidas de manera eficiente. A diferencia de
otros métodos, como la regla del trapecio o Simpson, la cuadratura gaussiana
logra una mayor precisión utilizando menos puntos de evaluación, gracias a
que los nodos y los pesos se eligen de forma óptima a partir de los polinomios
de Legendre.

## Objetivo del proyecto
El objetivo de este trabajo es resolver la integral

\[
I = \int_1^3 \left( x^6 - x^2 \sin(2x) \right) dx
\]

empleando el método de cuadratura gaussiana, e identificar con qué valor de
`N` se alcanza el resultado exacto.

## Organización de la documentación
Esta documentación está organizada en varias secciones:
- **Explicación**: descripción del método numérico utilizado.
- **Tutorial**: un ejemplo práctico de ejecución del código.
- **Referencia**: documentación automática de las funciones implementadas.
