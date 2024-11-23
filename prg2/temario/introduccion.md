# Vistas

Determinan el ámbito donde se puede referenciar la declaración de un miembro de la clase: atributo o método.

- **Pública**: conocido en cualquier punto de la aplicación.
- **Privada**: conocido en cualquier punto de la clase.

|               | Clases                                                                                                 | Objetos                                                             |
| ------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Vista pública | [INTERFAZ](temario/vpubclases.md):<br> Nombre de la Clase<br>Cabecera de los métodos                   | Creación de Objetos <br> Paso de Mensajes<br>Destrucción de Objetos |
| Vista privada | [IMPLEMENTACIÓN](temario/vprivclases.md):<br> Definición de atributos<br> Desencadenamiemto de objetos | Definición de Métodos<br> Desencadenamiento de Mensajes             |

## Dependencias

- Al crear objetos y lanzarles mensajes, hay que respetar la interfaz de sus clases =>
  - 1º **[Vista pública de las Clases](temario/vpubclases.md)**
  - 2º **[Vista pública de los Objetos](temario/vpubobjetos.md)** Al definir atributos de una clase y sus métodos se debe respetar la interfaz de otras clases =>
  - 3º **[Vista privada de las Clases](temario/vprivclases.md)**
- Al crear un objeto se produce un desencadenamiento de instanciaciones y al lanzar un mensaje se produce un desencadenamiento de mensajes, acorde a la definición de atributos y métodos de la clase del objeto =>
  - 4º **[Vista privada de Objetos](temario/vprivobjetos.md)**

## Mecanismos de comprensión

|                |                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------- |
| Abstracción    | Proceso de extracción de las características esenciales de algo, ignorando detalles superfluos              |
| Encapsulación  | Proceso por el que se oclutan los detalles del soporte de las características esenciales de una abstracción |
| Modularización | Proceso de descomposición de un sistema en un conjunto de piezas poco acopladas y cohesivas                 |
| Jerarquización | Proceso de estructuración por el que se produce un organización en grados de responsabilidad                |
