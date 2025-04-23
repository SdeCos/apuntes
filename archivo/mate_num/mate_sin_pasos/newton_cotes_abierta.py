import numpy as np


def solicitar_datos_nc_abierta():
    """
    Solicita los datos necesarios para calcular la integral usando las reglas de Newton-Cotes abiertas.
    """
    print(
        "\nMétodo para calcular la integral usando las reglas de Newton-Cotes abiertas"
    )

    # Datos de prueba (valores fijos)
    func_input = input("Introduce la funcion a integrar: ")  # La función a integrar
    a = float(input("Introduce el limite inferior: "))  # Límite inferior
    b = float(input("Introduce el limite superior: "))  # Límite superior
    n = float(input("Introduce el grado: "))  # Grado de la regla (0, 1, 2 o 3)

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


# Implementar las reglas de Newton-Cotes abiertas
def newton_cotes_abierta(f, a, b, n):
    """
    Aplica las reglas de Newton-Cotes abiertas (n=0, 1, 2, 3) para calcular la integral de f en el intervalo [a, b].
    """
    # print("\nPaso 0: Calcular el tamaño del paso (h)")
    h = (b - a) / (n + 2)
    # print(f"h = (b - a) / (n + 2) = ({b} - {a}) / ({n + 2}) = {h}")

    if n == 0:  # Regla del Punto Medio Abierta

        print("\nUsando la Regla de Newton-Cotes Abierta (n=0):")
        x0 = a + h
        # print(f"x0 = a + h = {a} + {h} = {x0}")
        f_x0 = f(x0)
        # print(f"f(x0) = f({x0}) = {f_x0}")
        integral = 2 * h * f_x0
        print(f"I = 2 * h * f(x0) = 2 * {h} * {f_x0} = {integral}")

    elif n == 1:

        print("\nUsando la Regla de Newton-Cotes Abierta (n=1):")
        x0 = a + h
        x1 = a + 2 * h
        # print(f"x0 = a + h = {a} + {h} = {x0}")
        # print(f"x1 = a + 2h = {a} + 2*{h} = {x1}")
        f_x0 = f(x0)
        f_x1 = f(x1)
        print(f"f(x0) = f({x0}) = {f_x0}")
        print(f"f(x1) = f({x1}) = {f_x1}")
        integral = (3 * h / 2) * (f_x0 + f_x1)
        print(
            f"I = (3 * h / 2) * (f(x0) + f(x1)) = (3 * {h} / 2) * ({f_x0} + {f_x1}) = {integral}"
        )

    elif n == 2:

        print("\nUsando la Regla de Newton-Cotes Abierta (n=2):")
        x0 = a + h
        x1 = a + 2 * h
        x2 = a + 3 * h
        # print(f"x0 = a + h = {a} + {h} = {x0}")
        # print(f"x1 = a + 2h = {a} + 2*{h} = {x1}")
        # print(f"x2 = a + 3h = {a} + 3*{h} = {x2}")
        f_x0 = f(x0)
        f_x1 = f(x1)
        f_x2 = f(x2)
        print(f"f(x0) = f({x0}) = {f_x0}")
        print(f"f(x1) = f({x1}) = {f_x1}")
        print(f"f(x2) = f({x2}) = {f_x2}")
        integral = (4 * h / 3) * (2 * f_x0 - f_x1 + 2 * f_x2)
        print(
            f"I = (4 * h / 3) * [2*f(x0) - f(x1) + 2*f(x2)] = ({4 * h} / 3) * (2*{f_x0} - {f_x1} + 2*{f_x2}) = {integral}"
        )

    elif n == 3:
        print("\nUsando la Regla de Newton-Cotes Abierta (n=3):")
        x0 = a + h
        x1 = a + 2 * h
        x2 = a + 3 * h
        x3 = a + 4 * h
        # print(f"x0 = a + h = {a} + {h} = {x0}")
        # print(f"x1 = a + 2h = {a} + 2*{h} = {x1}")
        # print(f"x2 = a + 3h = {a} + 3*{h} = {x2}")
        # print(f"x3 = a + 4h = {a} + 4*{h} = {x3}")
        f_x0 = f(x0)
        f_x1 = f(x1)
        f_x2 = f(x2)
        f_x3 = f(x3)
        # print(f"f(x0) = f({x0}) = {f_x0}")
        # print(f"f(x1) = f({x1}) = {f_x1}")
        # print(f"f(x2) = f({x2}) = {f_x2}")
        # print(f"f(x3) = f({x3}) = {f_x3}")
        integral = (5 * h / 24) * (11 * f_x0 + f_x1 + f_x2 + 11 * f_x3)
        # print(f"I = (5 * h / 24) * [11*f(x0) + f(x1) + f(x2) + 11*f(x3)]")
        print(
            f"I = (5 * {h} / 24) * [11*{f_x0} + {f_x1} + {f_x2} + 11*{f_x3}] = {integral}"
        )

    else:
        raise ValueError("El valor de n debe ser 0, 1, 2 o 3")

    return integral


def main():
    # Solicitar los datos
    func_input, a, b, n = solicitar_datos_nc_abierta()

    # Convertir la entrada de la función a una función evaluable
    f = get_function(func_input)

    # Calcular el valor de la integral usando Newton-Cotes Abierta
    resultado = newton_cotes_abierta(f, a, b, n)

    # Mostrar el resultado final
    print(
        f"\nEl valor de la integral usando la Regla de Newton-Cotes Abierta (n={n}) es: {resultado}"
    )
