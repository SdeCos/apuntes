# Miembros de Clase

| Instancia                                                                                                             | Clase                                                                                                                                      |
| --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Los miembros de instancia asumen los aspectos, datos y operaciones, particulares/locales de/a cada objeto de la clase | Los miembros de clase o estáticos asumen los aspectos, datos y operaciones, compartidos/globales por/a la comunidad de objetos de la clase |
| **Atributos de instancia** presentes en cada uno de los objetos de la clase                                           | **Atributos de clase** compartidos por la globalidad de objetos de la clase                                                                |
| _Ej.: día, mes y año de una fecha concreta._                                                                          | _Ej.: los nombres y duración de los meses de cualquier fecha, excepto en Febrero de años bisiestos..._                                     |
| Si no hay objetos, no hay atributos de instancia                                                                      | Si no hay objetos, **sí** hay atributos de clase                                                                                           |
| **Métodos de instancia** cuyos mensajes se lanzan sobre un objeto particular de la clase                              | **Métodos de clase** cuyos mensajes NO se lanzan sobre objetos particulares                                                                |
| _Ej.: si una fecha concreta está dentro de la primavera, si una fecha concreta se encuentra en un año bisiesto​_      | _Ej.: si un año (de cualquier fecha, no de una fecha particular) es bisiesto_                                                              |

## Atributos y métodos estáticos

Caracterizados por la palabra `static` tras su visibilidad
|||
|-|-|
|**Atributo**|`<Visibilidad> static <Tipo> <atributoEstático> = <Valor>`|
|**Método**|`<Visibilidad> static <TipoDevuelto> <métodoEstático>([<argumento> { <argumento>, }])`|
||

### Atributos estáticos

- Su reserva de memoria e inicialización obligatoria se realiza al principio de la ejecución del programa.
- En orden dentro de las declaraciones de la clase pero en desorden entre las distintas clases.
- Accesible desde cualquier método, de instancia o estático, de la clase.

## Ejemplo

```java
public class Alumno {
    private static String nombreUniversidad = "UNEATLANTICO";
    private String nombre;
    private int edad;

    public Alumno(String nombre, int edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    public void presentarse() {
        System.out.println("Hola, me llamo " + nombre + " y tengo " + edad + " años.");
    }

    public static void cambiarUniversidad(String nombreUniversidad) {
        this.nombreUniversidad = nombreUniversidad;
    }

    public static String getNombreUniversidad() {
        return nombreUniversidad;
    }

    public void mostrarUniversidad() {
        System.out.println(nombre + " estudia en: " + nombreUniversidad);
    }

    public static void main(String[] args) {

        Alumno alumno1 = new Alumno("Juan", 15);
        Alumno alumno2 = new Alumno("María", 16);

        alumno1.presentarse();
        alumno2.presentarse();

        Alumno.cambiarUniversidad("UNINI");

        System.out.println(Alumno.getNombreUniversidad());

        alumno1.mostrarUniversidad();
        alumno2.mostrarUniversidad();
    }
}

```
