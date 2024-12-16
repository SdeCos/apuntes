import numpy as np


def solicitar_datos_punto_medio():
    """
    Solicita los datos necesarios para calcular la integral usando la Regla del Punto Medio Compuesta.
    """
    print(
        "\nMétodo para calcular la integral usando la Regla del Punto Medio Compuesta"
    )

    # Datos de prueba (valores fijos)
    func_input = input("Introduce la ecuacion: ")  # La función a integrar
    a = float(input("Introduce el limite inferior: "))  # Límite inferior
    b = float(input("Introduce el limite superior: "))  # Límite inferior
    n = float(input("Introduce el paso:"))  # Número de subintervalos

    return func_input, a, b, n


# Definir la función matemática
def get_function(func_input):
    """
    Convierte la cadena de la función ingresada por el usuario a una función evaluable.
    """
    return lambda x: eval(
        func_input,
        {
            "x": x,
            "cos": np.cos,
            "sin": np.sin,
            "exp": np.exp,
            "tan": np.tan,
            "log": np.log,
        },
    )


# Implementar la regla del Punto Medio Compuesta
def punto_medio_compuesta(f, a, b, n):
    """
    Aplica la regla del Punto Medio Compuesta para calcular la integral de f en el intervalo [a, b].
    """
    # print("\nPaso 1: Calcular el tamaño del paso (h)")
    h = (b - a) / n
    # print(f"h = (b - a) / n = ({b} - {a}) / {n} = {h}")

    # print("\nPaso 2: Calcular los puntos medios de cada subintervalo y evaluarlos")
    suma = 0
    for i in range(n):
        x_medio = a + (i + 0.5) * h
        f_x_medio = f(x_medio)
        # print(
        #    f"Subintervalo {i+1}: x_medio = {a} + ({i} + 0.5)*{h} = {x_medio}, f({x_medio}) = {f_x_medio}"
        # )
        suma += f_x_medio

    # print("\nPaso 3: Sustituir los valores en la fórmula")
    # print("I = h * sum(f(x_medio))")
    integral = h * suma
    # print(f"I = {h} * {suma} = {integral}")

    return integral


def main():
    # Solicitar los datos
    func_input, a, b, n = solicitar_datos_punto_medio()

    # Convertir la entrada de la función a una función evaluable
    f = get_function(func_input)

    # Calcular el valor de la integral usando la Regla del Punto Medio Compuesta
    resultado = punto_medio_compuesta(f, a, b, n)

    # Mostrar el resultado final
    print(
        f"\nEl valor de la integral usando la Regla del Punto Medio Compuesta es: {resultado}"
    )
