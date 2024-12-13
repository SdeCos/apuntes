import numpy as np
import sympy as sp


def obtener_funcion_usuario():
    """
    Función para solicitar la ecuación de la forma 'f(t, y)' al usuario.
    """
    # Puedes cambiar esta ecuación para probar
    ecuacion = input("Introduce la ecuacion: ")  # Ecuación por defecto
    return ecuacion


def convertir_a_funcion(ecuacion):
    """
    Convierte la cadena de texto con la ecuación a una función simbólica.
    """
    t, y = sp.symbols("t y")
    ecuacion = ecuacion.replace("exp", "sp.exp")
    f = sp.sympify(ecuacion)  # Convertimos la ecuación a una expresión simbólica
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

    # Mostrar la primera iteración paso a paso
    print("\nPrimera iteración paso a paso:")
    t_0 = t_values[0]
    y_0 = y_values[0]
    print("===================================")
    print(f"Paso 1: t_0 = {t_0}, w_0 = {y_0}")

    # Evaluar f en el punto inicial
    f_value = f.subs({t: t_0, y: y_0})
    f_string = str(f)
    f_subs = f_string.replace(str(y), f"({y_0:.6f})").replace(str(t), f"({t_0:.6f})")
    print(f"f(t_0, w_0) = f({t_0}, {y_0}) = {f_subs} = {f_value:.6f}")

    # Evaluar la derivada total en el punto inicial
    f_prime_value = f_prime.subs({t: t_0, y: y_0})
    f_prime_string = str(f)
    f_prime_subs = f_prime_string.replace(str(y), f"({y_0:.6f})").replace(
        str(t), f"({t_0:.6f})"
    )
    print(f"f'(t_0, w_0) = f'({t_0}, {y_0}) = {f_prime_subs} = {f_prime_value:.6f}")

    # Usar la fórmula de Taylor de orden 2 para calcular el siguiente valor
    w_1 = y_0 + h * f_value + (h**2 / 2) * f_prime_value
    print(f"\nCálculo de w_1:")
    print(f"w_1 = w_0 + h * f(t_0, y_0) + (h^2 / 2) * f'(t_0, y_0)")
    print(f"w_1 = {y_0} + {h} * {f_value} + ({h**2} / 2) * {f_prime_value}")
    print(f"w_1 = {w_1}\n")

    # Guardar el resultado de la primera iteración
    y_values[1] = w_1

    # Iterar para el resto de los pasos
    for i in range(1, len(t_values) - 1):
        t_i = t_values[i]
        y_i = y_values[i]

        # Evaluar f y su derivada total
        f_value = f.subs({t: t_i, y: y_i})
        f_prime_value = f_prime.subs({t: t_i, y: y_i})

        # Calcular el siguiente valor usando Taylor de orden 2
        y_values[i + 1] = y_i + h * f_value + (h**2 / 2) * f_prime_value

    return t_values, y_values


def main():
    # Obtener la ecuación de la forma 'f(t, y)'
    ecuacion = obtener_funcion_usuario()

    # Parámetros del problema
    tmin = float(input("Introduce el valor minimo de t: "))
    tmax = float(input("Introduce el valor maximo de t: "))
    h = float(input("Introduce el valor de h: "))
    w0 = float(input("Introduce el valor de w0: "))

    # Resolver la ecuación diferencial usando el método de Taylor
    t_values, y_values = taylor_order_2(ecuacion, tmin, tmax, h, w0, ecuacion)

    # Mostrar resultados
    print("\nResultados:")
    for t, y in zip(t_values, y_values):
        print(f"t = {t:.2f}, y ≈ {y:.6f}")

    input("Presiona intro para continuar")
