# HOOD

Cada objeto de un programa debe asumir directamente cierta parte de sus responsabilidades y saber delegar otras en otros objetos colaboradore: no se trata de que un objeto asuma y "controle todo" y el resto se dispongan a darle información.\
Una aplicación es un único ojbeto. Para ejecutarla se envía un único mensaje a la clase principal.

|                       | Aplicacion | Gestor   | Simulador  | Juego  |
| --------------------- | ---------- | -------- | ---------- | ------ |
| **Clase prinpal**     | App        | Manager  | Simulator  | Game   |
| **Método disparador** | execute()  | manage() | simulate() | play() |
