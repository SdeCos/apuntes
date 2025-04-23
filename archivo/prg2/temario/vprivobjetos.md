# Vista privada de los objetos

## Desencadenamiento de instanciaciones

Se crea un objeto (instancia), por lo que:

- Se crean los atributos definidos en la clase.
- Se ejecuta la inicialización de los atributos.
- Se ejecuta el constructor en la creación del objeto.

## Desencadenamiento de mensajes

Se lanza un mensaje a un objeto:

- Se crean las declaraciones locales con su inicialización y se ejecuta el cuerpo del método.
- Se pueden lanzar nuevos mensajes a objetos que sean atributo de su clase.
  |El desencadenamiento de instanciaciones| El desencadenamiento de mensajes|
  |-|-|
  |Puede provocar un desencadenamiento de mensajes a través de la ejecución de los constructores que pueden lanzar mensajes|Puede provocar un desencadenamiento de instanciaciones a través de la creación de objetos en la definición de los métodos.|
