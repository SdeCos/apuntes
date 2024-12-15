import numpy as np


def solicitar_datos_nc4():
    """
    Solicita los datos necesarios para calcular la integral usando la regla de Newton-Cotes cerrada (n=4).
    """
    print(
        "\nMétodo para calcular la integral usando la Regla de Newton-Cotes cerrada (n = 4)"
    )

    # Datos de prueba (valores fijos)
    func_input = input("Introduce la ecuacion: ")  # La función a integrar
    a = float(input("Introduce el limite inferior: "))  # Límite inferior
    b = float(input("Introduce el limite superior: "))  # Límite inferior

    return func_input, a, b


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


# Implementar la regla de Newton-Cotes cerrada (n=4)
def newton_cotes_n4(f, a, b):
    """
    Aplica la regla de Newton-Cotes cerrada (n=4) para calcular la integral de f en el intervalo [a, b].
    """
    print("\nPaso 1: Calcular el tamaño del paso (h)")
    h = (b - a) / 4
    print(f"h = (b - a) / 4 = ({b} - {a}) / 4 = {h}")

    print("\nPaso 2: Evaluar la función en los puntos clave")
    f_a = f(a)
    print(f"f(a) = f({a}) = {f_a}")

    f_a_h = f(a + h)
    print(f"f(a + h) = f({a} + {h}) = f({a + h}) = {f_a_h}")

    f_a_2h = f(a + 2 * h)
    print(f"f(a + 2h) = f({a} + 2*{h}) = f({a + 2 * h}) = {f_a_2h}")

    f_a_3h = f(a + 3 * h)
    print(f"f(a + 3h) = f({a} + 3*{h}) = f({a + 3 * h}) = {f_a_3h}")

    f_b = f(b)
    print(f"f(b) = f({b}) = {f_b}")

    print("\nPaso 3: Sustituir los valores en la fórmula")
    print("I = (2h / 45) * [7f(a) + 32f(a+h) + 12f(a+2h) + 32f(a+3h) + 7f(b)]")
    integral = (2 * h / 45) * (
        7 * f_a + 32 * f_a_h + 12 * f_a_2h + 32 * f_a_3h + 7 * f_b
    )
    print(
        f"I = (2 * {h} / 45) * (7*{f_a} + 32*{f_a_h} + 12*{f_a_2h} + 32*{f_a_3h} + 7*{f_b})"
    )

    return integral


def main():
    # Solicitar los datos
    func_input, a, b = solicitar_datos_nc4()

    # Convertir la entrada de la función a una función evaluable
    f = get_function(func_input)

    # Calcular el valor de la integral usando la Regla de Newton-Cotes cerrada (n=4)
    resultado = newton_cotes_n4(f, a, b)

    # Mostrar el resultado final
    print(
        f"\nEl valor de la integral usando la Regla de Newton-Cotes cerrada (n=4) es: {resultado}"
    )
