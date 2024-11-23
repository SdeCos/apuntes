# Entrada por consola

## ¿Por qué?

Para que el usuario pueda interaccionar en tiempo real con la aplicación, es necesario que esta pueda recibir datos, para ello se utiliza la entrada por consola.

## ¿Qué?

Es la capacidad que tiene una aplicación para aceptar infromación proporcionada en tiempo real mientras se está ejecutando.

## ¿Para qué?

|                      |                                                                                                                        |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Interactividad       | Mejora la experiencia ya quer permite la comunicación bidireccional entre el programa y el usuario                     |
| Flexibilidad         | Permite al programa adaptarse y tomar decisiones basadas en la entrada proporcionada                                   |
| Aprendizaje          | Permite una comprensión directa de la relación entre el código y sus efectos                                           |
| Pruebas y Depuración | Sirve como herramienta para probar y depurar, permitiendo experimentar con diferentes entradas sin modificar el código |

## ¿Cómo?

La entrada en java se facilita mediante la clase Scanner del paquete java.util.

### Importación de la Clase Scanner:

```java
import java.util.Scanner;
```

### Creación de Objeto Scanner:

```java
Scanner scanner = new Scanner(System.in);
```

### Lectura de Entrada:

La clase scanner proporciona varios métodos para leer diferentes tipos de datos, como:

- `nextInt()` para enteros.
- `nextLine()` para cadenas.
- `nexDouble()` para números decimales.

### Finalización

Para cerrar el objeto Scanner cuando ya no es necesario.

```java
scanner.close();
```
