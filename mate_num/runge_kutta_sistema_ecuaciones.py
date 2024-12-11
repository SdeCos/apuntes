import sympy as sp
from sympy import *


def runge_kutta_sistema_ecuaciones():
    """Metodo de Runge-Kutta para un sistema de dos ecuaciones"""
    print("==== Metodo de Runge-Kutta para un sistema de ecuaciones ====")

    # Definir las variables
    y1, y2, t = symbols("y1 y2 t")

    # Ecuaciones del sistema (dy1/dt y dy2/dt)
    ecuacion1 = input("Introduce la primera ecuacion: ")
    ecuacion2 = input("Introduce la segunda ecuacion: ")

    # Valores iniciales y parámetros
    t_min = float(input("Introduce el valor minimo de t: "))
    t_max = float(input("Introduce el valor maximo de t: "))
    y1_inicial = float(input("Introduce el valor de y1 en t_min: "))
    y2_inicial = float(input("Introduce el valor de y1 en t_min: "))
    h = float(input("Introduce el valor de h: "))

    # Lambdify las ecuaciones para su evaluación numérica
    f1 = sp.simplify(ecuacion1)
    f2 = sp.simplify(ecuacion2)
    f1_lambified = sp.lambdify((t, y1, y2), f1, "math")
    f2_lambified = sp.lambdify((t, y1, y2), f2, "math")

    # Listas para almacenar los resultados
    t_values = [t_min]
    y1_values = [y1_inicial]
    y2_values = [y2_inicial]

    k1_values = []
    k2_values = []
    k3_values = []
    k4_values = []

    k1_values_2 = []
    k2_values_2 = []
    k3_values_2 = []
    k4_values_2 = []

    # Iterador
    i = 0
    i_values = [i]

    first_iteration = True

    while t_min <= (t_max + h / 2):
        # Calcular k1, k2, k3 y k4 para cada ecuación
        k1_values_temp = []
        k2_values_temp = []
        k3_values_temp = []
        k4_values_temp = []

        # Para la primera ecuación (dy1/dt)
        k1_1 = h * f1_lambified(t_min, y1_inicial, y2_inicial)
        k1_2 = h * f2_lambified(t_min, y1_inicial, y2_inicial)
        k2_1 = h * f1_lambified(
            t_min + h / 2, y1_inicial + k1_1 / 2, y2_inicial + k1_2 / 2
        )
        k2_2 = h * f2_lambified(
            t_min + h / 2, y1_inicial + k1_1 / 2, y2_inicial + k1_2 / 2
        )
        k3_1 = h * f1_lambified(
            t_min + h / 2, y1_inicial + k2_1 / 2, y2_inicial + k2_2 / 2
        )
        k3_2 = h * f2_lambified(
            t_min + h / 2, y1_inicial + k2_1 / 2, y2_inicial + k2_2 / 2
        )
        k4_1 = h * f1_lambified(t_min + h, y1_inicial + k3_1, y2_inicial + k3_2)

        # Para la segunda ecuación (dy2/dt)
        k4_2 = h * f2_lambified(t_min + h, y1_inicial + k3_1, y2_inicial + k3_2)

        # Almacenar los valores de k1, k2, k3 y k4 para ambas ecuaciones
        k1_values_temp.append(k1_1)
        k2_values_temp.append(k2_1)
        k3_values_temp.append(k3_1)
        k4_values_temp.append(k4_1)

        k1_values_temp.append(k1_2)
        k2_values_temp.append(k2_2)
        k3_values_temp.append(k3_2)
        k4_values_temp.append(k4_2)

        if first_iteration:
            print("=== Primera Iteracion ===")

            # Primera ecuación (dy1/dt)
            equation1_string = str(ecuacion1)
            equation1_k1 = (
                equation1_string.replace(str(t), f"({t_min:.6f})")
                .replace(str(y1), f"({y1_inicial:.6f})")
                .replace(str(y2), f"({y2_inicial:.6f})")
            )
            print(f"k1_1 = {h} * ({equation1_k1}) = {k1_1:.6f}")

            equation1_k2 = (
                equation1_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k1_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k1_1 / 2:.6f})")
            )
            print(f"k2_1 = {h} * ({equation1_k2}) = {k2_1:.6f}")

            equation1_k3 = (
                equation1_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k2_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k2_1 / 2:.6f})")
            )
            print(f"k3_1 = {h} * ({equation1_k3}) = {k3_1:.6f}")

            equation1_k4 = (
                equation1_string.replace(str(t), f"({t_min + h:.6f})")
                .replace(str(y1), f"({y1_inicial + k3_1:.6f})")
                .replace(str(y2), f"({y2_inicial + k3_1:.6f})")
            )
            print(f"k4_1 = {h} * ({equation1_k4}) = {k4_1:.6f}")

            # Segunda ecuación (dy2/dt)
            equation2_string = str(ecuacion2)
            equation2_k1 = (
                equation2_string.replace(str(t), f"({t_min:.6f})")
                .replace(str(y1), f"({y1_inicial:.6f})")
                .replace(str(y2), f"({y2_inicial:.6f})")
            )
            print(f"k1_2 = {h} * ({equation2_k1}) = {k1_2:.6f}")

            equation2_k2 = (
                equation2_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k1_2 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k1_2 / 2:.6f})")
            )
            print(f"k2_2 = {h} * ({equation2_k2}) = {k2_2:.6f}")

            equation2_k3 = (
                equation2_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k2_2 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k2_2 / 2:.6f})")
            )
            print(f"k3_2 = {h} * ({equation2_k3}) = {k3_2:.6f}")

            equation2_k4 = (
                equation2_string.replace(str(t), f"({t_min + h:.6f})")
                .replace(str(y1), f"({y1_inicial + k3_2:.6f})")
                .replace(str(y2), f"({y2_inicial + k3_2:.6f})")
            )
            print(f"k4_2 = {h} * ({equation2_k4}) = {k4_2:.6f}")

            first_iteration = False

        # Actualizar los valores de y1 y y2
        y1_inicial += (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
        y2_inicial += (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6

        # Actualizar los valores en las listas
        t_min += h
        i += 1
        i_values.append(i)
        k1_values.append(k1_values_temp[0])
        k2_values.append(k2_values_temp[0])
        k3_values.append(k3_values_temp[0])
        k4_values.append(k4_values_temp[0])

        # Añadir los valores de la segunda ecuación (dy2/dt)
        k1_values_2.append(k1_values_temp[1])
        k2_values_2.append(k2_values_temp[1])
        k3_values_2.append(k3_values_temp[1])
        k4_values_2.append(k4_values_temp[1])

        t_values.append(t_min)
        y1_values.append(y1_inicial)
        y2_values.append(y2_inicial)

    # Imprimir los resultados
    print("Resultados (t, y1, y2):")
    for i, t, y1, y2, k1_1, k2_1, k3_1, k4_1, k1_2, k2_2, k3_2, k4_2 in zip(
        i_values,
        t_values,
        y1_values,
        y2_values,
        k1_values,
        k2_values,
        k3_values,
        k4_values,
        k1_values_2,
        k2_values_2,
        k3_values_2,
        k4_values_2,
    ):
        print(
            f"i = {i}, t = {t:.6f}, y1 = {y1:.6f}, y2 = {y2:.6f}, "
            f"k1_1 = {k1_1:.6f}, k2_1 = {k2_1:.6f}, k3_1 = {k3_1:.6f}, k4_1 = {k4_1:.6f}, "
            f"k1_2 = {k1_2:.6f}, k2_2 = {k2_2:.6f}, k3_2 = {k3_2:.6f}, k4_2 = {k4_2:.6f}"
        )
    input()
