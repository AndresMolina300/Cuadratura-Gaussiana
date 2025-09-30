# Referencia de funciones (C++)

En esta parte quiero documentar las funciones que utilicé en mi código
`Lab_7_AndresMolina.cpp`. Aquí explico para qué sirve cada una y cómo se conectan entre sí.

---

## `double Integrando(double x)`

Esta es la función que yo definí para integrar.  
Básicamente lo que hace es calcular:
\[
f(x) = x^6 - x^2 \sin(2x)
\]

Cada vez que necesito evaluar la integral en un punto, llamo a `Integrando(x)` y me devuelve el valor.

---

## `double sumRiemman(int N, double a, double b)`

Esta función es la que realmente hace el cálculo de la integral.  
Recibe tres parámetros:

- `N`: la cantidad de nodos que uso en la cuadratura gaussiana.  
- `a`: el límite inferior.  
- `b`: el límite superior.  

Dentro de la función aplico el **cambio de variable** para llevar el intervalo `[a,b]` al estándar `[-1,1]`, y luego voy sumando los valores de la función con los pesos. Al final me devuelve una aproximación de la integral en `[a,b]`.

---

## `int main()`

En `main` es donde junto todo:  
- Defino los límites de integración `a=1` y `b=3`.  
- Llamo a `sumRiemman` para distintos valores de `N`.  
- Imprimo en pantalla los resultados de cada aproximación.

De esa forma puedo ver cómo cambia la precisión cuando aumento el número de nodos.

---

**Nota personal:** Esta documentación corresponde a mi implementación en C++ del método de cuadratura gaussiana, que usé en el laboratorio.
