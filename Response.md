# Proyecto de Modelos de Optimización

## Introducción
En este proyecto, presentamos el análisis de problemas de optimización no lineal. Para ello, hemos seleccionado ciertos métodos basándonos en fundamentos sólidos. Nuestra elección se justifica en la eficacia de estos métodos para resolver problemas complejos de optimización.

### Algoritmos Seleccionados:

#### Sequential Least Squares Programming:
El método Sequential Least Squares Programming (SLSQP) es un método de optimización no lineal versátil y eficiente que se puede aplicar a una amplia gama de problemas, tanto con restricciones como sin restricciones. Es una buena opción para problemas que requieren una combinación de eficiencia y versatilidad. Entre sus bondades se encuentran su versatilidad, eficiencia y facilidad de implementación. Sin embargo, también tiene algunas limitaciones, como no ser tan robusto como otros métodos y requerir la evaluación de la función objetivo y sus derivadas en cada paso del algoritmo de optimización. Algunos casos de uso típicos del SLSQP incluyen la optimización de funciones no lineales con restricciones, la resolución de problemas de programación lineal con restricciones no lineales y la optimización de problemas de ingeniería.

#### L-BFGS-B :
L-BFGS-B es un método de optimización no lineal que funciona bien en problemas con restricciones. Es una versión modificada del método BFGS que permite incluir restricciones en las variables. Las principales ventajas de este método son que es rápido, eficiente y robusto. El método funciona construyendo una matriz hessiana inversa aproximada, que se utiliza para calcular la dirección de descenso de la función objetivo. La matriz hessiana inversa aproximada se construye utilizando información de la función objetivo y de los puntos de búsqueda anteriores. El proceso se repite hasta que la función objetivo converge a un mínimo. L-BFGS-B es adecuado para problemas no lineales porque no requiere información sobre las derivadas de la función objetivo. También es robusto y eficiente, lo que significa que puede funcionar bien en una amplia gama de problemas.

#### Nelder-Mead:
El método Nelder-Mead es un método de optimización no lineal sin restricciones que utiliza una búsqueda por coordenadas para encontrar el mínimo de una función. Las principales ventajas de este método son que es simple de implementar y puede converger rápidamente a una solución óptima local. El método funciona construyendo un simplex, que es una figura geométrica con N+1 vértices. El simplex se mueve a través del espacio de búsqueda mediante cuatro operaciones básicas: reflexión, expansión, contracción y shrinking. La reflexión mueve el simplex a través del punto más alejado de la función objetivo. La expansión mueve el simplex aún más lejos de este punto. La contracción mueve el simplex hacia el punto más cercano a la función objetivo. El shrinking contrae uniformemente el simplex. El proceso se repite hasta que el simplex converge a un punto que se considera una solución óptima local. Este método es adecuado para problemas no lineales porque no requiere información sobre las derivadas de la función objetivo; lo cual corresponde con el tipo de problemas que estamos analizando. También es robusto y eficiente, lo que significa que puede funcionar bien en una amplia gama de problemas.

### Particularidades comunes de los problemas:
1. Problemas de Optimización no lineales.
2. Las restricciones son lineales.
3. Las restricciones son únicamente con respecto al valor máximo y/o mínimo de cada variable.

## Resultados:
### Ejercicio 21:

#### SLSQP:
Encontró un mínimo que satisface el conjunto de restricciones y númericamente es el mismo que el esperado (0) , las razones por las que difieren los valores de las variables con los esperados pueden ser por errores númericos de la aritmética al trabajar con valores tan cercanos a cero dado que para valores cercanos a $(1,10,1)$ converge rápidamente a la solución óptima. Se mantiene el mismo criterio para todo valor de N. El número de iteraciones se mantuvo entorno a los 13 siendo 14 para $N=10$
esta disminución se debe a que por la misma naturaleza de los valores de
$g(x)$  hayan valores que no aporten a la suma por los errores numéricos.


#### L-BFGS-B: 
Encuentra una soluciones óptimas en varios puntos, los valores de las variables no satisfacen las restricciones. Esto se debe a que no trabajan sobre el conjunto de restricciones.

#### Nelder-Mead:
Encuentra una soluciones óptimas en varios puntos, los valores de las variables no satisfacen las restricciones. Esto se debe a que no trabajan sobre el conjunto de restricciones.





### Ejercicio 34:
#### SLSQP:
Para $N=10$ encontró un mínimo que satisface el conjunto de restricciones y númericamente es el mismo que el esperado (0), el número de iteraciones fue de 52. Para valores mayores que 100 no ecuentra el óptimo, los problemas para converger pueden estar dado por la misma función que apartir de ciertos valores tiende con gran velocidad a infinito por su misma naturaleza cuadrática. Por tanto no es confiable el uso de este algoritmo para localizar los óptimos de esta función. 

#### L-BFGS-B:



