# Vista privada de las clases

## Definición de Atributos

- **Datos constantes**
- **Variables de tipos primitivos**
- **Referencias a objetos y/o vectores de objetos**

Se declaran variables y/o constantes de tipos primitivos, referencias a objetos o vectores de éstos, anteponiendo la palabra **private**.\
En cualquier punto de la implementación de la clase, pero lo lógico es **al principio de la declaración de la clase**.

```java
class <class> {
    private <declaration>;
    private <declaration>;
    ...
}
```

```java
class Interval{
    private double min;
    private double max;
    ...
}
```

## Definición de Constructores

**Inicialización de los atributos de la clase**\
Reservado para las tareas de inicialización de los atributos del objetos.\
A falta de inicialización, **no recomendado**, se inicializan a valores por defecto.

```java
    class Interval {

        private double min;
        private double max;

        public Interval(){
            min = 0;
            max = 0;
        }

        public Interval(double maximum){
            min = 0;
            max = maximum;
        }

        public Interval(double minimum, double maximum){
            min = minimum;
            max = maximum;
        }
        ...
    }

```

## Definicion de Métodos

**Operacoines con sentencias secuenciales, alternativos, iterativas, expresiones (asignación) y/o de retorno**

```java
    clase <class> {

        public <methodHeader> <sequentialSentence>
        public <methodHeader> <sequentialSentence>
        ...
    }
```

```java
    class Interval {

        private double min;
        private double max;

        public void shift (double amount) {
            min += amount;
            max += amount;
        }

        public Interval(Interval interval){
            min = interval.min;
            max = interval.max;
        }

        public boolean equals(Intervalo interval) {
            return min == interval.min && max == interval.max;
        }
        ...
    }
```
