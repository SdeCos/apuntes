import numpy as np
import sympy as sp


def obtener_funcion_usuario():
    """
    Solicita al usuario una ecuación en términos de t y y.
    """
    ecuacion = input(
        "Introduce la ecuación en términos de t y y (por ejemplo: exp(t-y)): "
    )
    return ecuacion


def convertir_a_funcion(ecuacion):
    """
    Convierte la cadena de texto con la ecuación a una función simbólica.
    Maneja funciones comunes como exp, sin, cos, log, etc.
    """
    t, y = sp.symbols("t y")

    # Diccionario con funciones matemáticas soportadas
    funciones_permitidas = {
        "exp": sp.exp,
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "log": sp.log,
    }

    try:
        # sympify con funciones matemáticas explícitas
        f = sp.sympify(ecuacion, locals=funciones_permitidas)
    except Exception as e:
        raise ValueError(f"Error al interpretar la ecuación: {ecuacion}\n{e}")

    return f, t, y


def calcular_derivada_parcial(f, t, y):
    """
    Calcula la derivada total de la función f.
    """
    return sp.diff(f, t) + f * sp.diff(f, y)


def taylor_order_2(f, tmin, tmax, h, y0, ecuacion_original):
    """
    Método de Taylor de orden 2 para resolver ecuaciones diferenciales.

    Parámetros:
    - f: función que define la ecuación diferencial
    - tmin: valor mínimo de t
    - tmax: valor máximo de t
    - h: tamaño del paso
    - y0: valor inicial de y en t = tmin
    - ecuacion_original: ecuación original en formato de texto
    """
    # Inicializar los valores de t y y
    t_values = np.arange(tmin, tmax + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0  # Condición inicial

    # Convertir la ecuación a una función simbólica
    t, y = sp.symbols("t y")
    f, t, y = convertir_a_funcion(ecuacion_original)

    # Calcular la derivada total necesaria para Taylor de orden 2
    f_prime = calcular_derivada_parcial(f, t, y)

    # Mostrar las derivadas calculadas
    print("\nEcuaciones derivadas:")
    print(f"y' = {f}")
    print(f"y'' = {f_prime}\n")

    # Iterar para calcular los valores aproximados de y
    for i in range(len(t_values) - 1):
        t_i = t_values[i]
        y_i = y_values[i]

        # Evaluar f y su derivada total en el punto actual
        f_value = float(f.subs({t: t_i, y: y_i}))
        f_prime_value = float(f_prime.subs({t: t_i, y: y_i}))

        # Usar la fórmula de Taylor de orden 2 para calcular el siguiente valor
        y_values[i + 1] = y_i + h * f_value + (h**2 / 2) * f_prime_value

        # Mostrar los pasos para cada iteración
        print(f"\nPaso {i + 1}:")
        print(f"t_{i} = {t_i:.6f}, y_{i} = {y_i:.6f}")
        print(f"f(t_{i}, y_{i}) = {f_value:.6f}")
        print(f"f'(t_{i}, y_{i}) = {f_prime_value:.6f}")
        print(f"y_{i+1} = y_{i} + h * f + (h^2 / 2) * f'")
        print(
            f"y_{i+1} = {y_i:.6f} + {h:.6f} * {f_value:.6f} + ({h**2:.6f} / 2) * {f_prime_value:.6f}"
        )
        print(f"y_{i+1} ≈ {y_values[i + 1]:.6f}")

    return t_values, y_values


def main():
    # Obtener la ecuación de la forma 'f(t, y)'
    ecuacion = obtener_funcion_usuario()

    # Parámetros del problema
    tmin = float(input("Introduce el valor mínimo de t (tmin): "))
    tmax = float(input("Introduce el valor máximo de t (tmax): "))
    h = float(input("Introduce el valor de h (tamaño del paso): "))
    y0 = float(input("Introduce el valor inicial y0: "))

    # Resolver la ecuación diferencial usando el método de Taylor
    t_values, y_values = taylor_order_2(ecuacion, tmin, tmax, h, y0, ecuacion)

    # Mostrar resultados
    print("\nResultados:")
    for t, y in zip(t_values, y_values):
        print(f"t = {t:.2f}, y ≈ {y:.6f}")
    input("Presiona intro para continuar")


if __name__ == "__main__":
    main()
