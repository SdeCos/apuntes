# Complejidad temporal

## ¿Por qué?

La eficiencia es crucial en la programación. Además de funcionar, un programa debe hacerlo rápidamente y no debe consumir más recursos de los necesarios.\
La complejidad temporal y espacial nos proporciona una herramienta para evaluar y comparar la eficiencia de las operaciones y algoritmos.

## ¿Qué?

| Complejidad temporal                                                                            | Complejidad espacial                                                                              |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Se refiere al tiempo que tarda un algoritmo en completarse en función del tamaño de la entrada. | Se refiere a la cantidad de memorai que un algoritmo utiliza en función del tamaño de la entrada. |
| Medida de la rapidez con la que se ejecuta un algoritmo.                                        | Es una medida de cuánto espacio en memoria consume un algoritmo.                                  |

## ¿Para qué?

- **Optimización**: al entender la complejidad, podemos elegir o diseñar algoritmos que sean más eficientes para un problema.
- **Comparación**: Nos permite comparar diferentes algoritmos o estructuras de datos y elegir el más adecuado.
- **Previsión**: Ayuda a prever cómo se comportará un algoritmo.

## ¿Cómo?

La complejidad se suele expresar mediante la notación Big O (O grande). Denotada como **(O(f(n)))**, es una notación matemática que describe el límite superior del tiempo de ejecución.
|Notación|Complejidad|Descripción|Ejemplo|
|-|-|-|-|
|O(1)|Constante|Se ejecuta en un tiempo constante, independiente del tamaño de entrada.|Acceder a un elemento de un array indicando su índice.|
|O(log n)| Logarítmica| El tiempo de ejecución crece logarítmicamente con el tamaño de la entrada.| Búsqueda binaria en un array ordenado.|
|O(n)|Lineal|El tiempo de ejecución crece linealmente con el tamaño de la entrada.|Buscar un elemento en un array no ordenado.|
|O(n log n)| |A menudo se ve en algoritmos de ordenación eficientes como el mergesort o el heapsort.| |
|O(n^2), O(n^3), ...|Polinómica|Se ven en algoritmos con bucles anidados.| Algoritmos de ordenación como el bubble sort (para (O(n^2)).|
|O(2^n)|Exponencial|El tiempo de ejecución dobla con cada adición a la entrada.|Algoritmos de fuerza bruta para el problema del viajante.|
