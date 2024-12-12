import sympy as sp
from sympy import *
from tabulate import tabulate


def menu():
    """menu minimos cuadrados"""
    while True:
        print("Elige el tipo de minimo")
        print("1. Runge-Kutta 1 ecuacion")
        print("2. Runge-Kutta 2 ecuacion")
        print("3. Runge-Kutta 3 ecuacion")
        print("4. Salir")
        choice = input("Introduce un valor (1-6): ")
        if choice == "1":
            runge_kutta_1_ecuacion()
            input("Presiona intro para continuar")
            break
        elif choice == "2":
            runge_kutta_2_ecuaciones()
            input("Presiona intro para continuar")
            break
        elif choice == "3":
            runge_kutta_3_ecuaciones()
            input("Presiona intro para continuar")
            break
        elif choice == "4":
            break
        else:
            print("Elige un valor valido")


def runge_kutta_1_ecuacion():
    """metodo de runge kutta"""
    print("==== Metodo de Runge-Kutta ====")
    y, t = symbols("y t")
    i = 0
    equation = input("Introduce la ecuacion:")
    t_min = float(input("Introduce el valor minimo de t: "))
    t_max = float(input("Introduce el valor maximo de t: "))
    wi = float(input("Introduce el valor de y en t_min: "))
    h = float(input("Introduce el valor de h: "))
    f = sp.simplify(equation)
    f_lambified = sp.lambdify((t, y), f, "math")

    t_values = [t_min]
    y_values = [wi]
    k1_values = []
    k2_values = []
    k3_values = []
    k4_values = []
    first_iteration = True

    i_values = [i]

    while t_min <= t_max:

        k1 = h * f_lambified(t_min, wi)
        k2 = h * f_lambified(t_min + h / 2, wi + k1 / 2)
        k3 = h * f_lambified(t_min + h / 2, wi + k2 / 2)
        k4 = h * f_lambified(t_min + h, wi + k3)
        if first_iteration:
            print("=== Primera Iteracion ===")

            # Start with the original equation_string for each iteration
            equation_string = str(equation)

            # First iteration (k1)
            equation_k1 = equation_string
            # Replace t and y in one pass
            equation_k1 = equation_k1.replace(str(t), f"({t_min:.6f})").replace(
                str(y), f"({wi:.6f})"
            )
            print(f"k1 = {h} * ({equation_k1}) = {k1:.6f}")

            # Second iteration (k2)
            equation_k2 = equation_string
            # Replace t and y in one pass
            equation_k2 = equation_k2.replace(str(t), f"({t_min + h / 2:.6f})").replace(
                str(y), f"({wi + k1 / 2:.6f})"
            )
            print(f"k2 = {h} * ({equation_k2}) = {k2:.6f}")

            # Third iteration (k3)
            equation_k3 = equation_string
            # Replace t and y in one pass
            equation_k3 = equation_k3.replace(str(t), f"({t_min + h / 2:.6f})").replace(
                str(y), f"({wi + k2 / 2:.6f})"
            )
            print(f"k3 = {h} * ({equation_k3}) = {k3:.6f}")

            # Fourth iteration (k4)
            equation_k4 = equation_string
            # Replace t and y in one pass
            equation_k4 = equation_k4.replace(str(t), f"({t_min + h:.6f})").replace(
                str(y), f"({wi + k3:.6f})"
            )
            print(f"k4 = {h} * ({equation_k4}) = {k4:.6f}")

            equation_wi = f"wi = {wi:.6f} + ({k1:.6f} + 2 * {k2:.6f} + 2 * {k3:.6f} + {k4:.6f}) / 6"
            wi_value = wi + (k1 + 2 * k2 + 2 * k3 + k4) / 6
            print(f"Equation for wi: {equation_wi} = {wi_value:.6f}")

            first_iteration = False

        wi += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t_min += h
        i += 1
        i_values.append(i)
        k1_values.append(k1)
        k2_values.append(k2)
        k3_values.append(k3)
        k4_values.append(k4)

        t_values.append(t_min)
        y_values.append(wi)

    table = []
    for i, t, y, k1, k2, k3, k4 in zip(
        i_values, t_values, y_values, k1_values, k2_values, k3_values, k4_values
    ):
        table.append([i, t, y, k1, k2, k3, k4])

    # Imprimimos la tabla
    headers = ["i", "t", "y", "k1", "k2", "k3", "k4"]
    print("\nTabla:")
    print(tabulate(table, headers=headers, floatfmt=".6f", tablefmt="github"))
    # print("Resultados (t, y):")
    # for i, t, y, k1, k2, k3, k4 in zip(
    #     i_values, t_values, y_values, k1_values, k2_values, k3_values, k4_values
    # ):
    #     print(
    #         f"i = {i}, t = {t:.6f}, y = {y:.6f}, k1 = {k1:.6f}, k2 = {k2:.6f}, k3 = {k3:.6f}, k4 = {k4:.6f}"
    #     )
    input("Presiona intro para continuar")


def runge_kutta_2_ecuaciones():
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

    tabla = []

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

        tabla.append(
            [
                i,
                t_min,
                y1_inicial,
                y2_inicial,
                k1_1,
                k2_1,
                k3_1,
                k4_1,
                k1_2,
                k2_2,
                k3_2,
                k4_2,
            ]
        )

    # Imprimir los resultados
    headers = [
        "i",
        "t",
        "y1",
        "y2",
        "k1_1",
        "k2_1",
        "k3_1",
        "k4_1",
        "k1_2",
        "k2_2",
        "k3_2",
        "k4_2",
    ]
    print("\nResultados en forma de tabla:")
    print(tabulate(tabla, headers=headers, floatfmt=".6f", tablefmt="github"))
    input()


def runge_kutta_3_ecuaciones():
    """Método de Runge-Kutta para un sistema de tres ecuaciones diferenciales"""
    print("==== Método de Runge-Kutta para un sistema de tres ecuaciones ====")

    # Definir las variables
    y1, y2, y3, t = symbols("y1 y2 y3 t")

    # Ecuaciones del sistema
    ecuacion1 = input("Introduce la primera ecuación (dy1/dt): ")
    ecuacion2 = input("Introduce la segunda ecuación (dy2/dt): ")
    ecuacion3 = input("Introduce la tercera ecuación (dy3/dt): ")

    # Valores iniciales y parámetros
    t_min = float(input("Introduce el valor mínimo de t: "))
    t_max = float(input("Introduce el valor máximo de t: "))
    y1_inicial = float(input("Introduce el valor inicial de y1 en t_min: "))
    y2_inicial = float(input("Introduce el valor inicial de y2 en t_min: "))
    y3_inicial = float(input("Introduce el valor inicial de y3 en t_min: "))
    h = float(input("Introduce el valor de h: "))

    # Lambdify las ecuaciones para su evaluación numérica
    f1 = sp.simplify(ecuacion1)
    f2 = sp.simplify(ecuacion2)
    f3 = sp.simplify(ecuacion3)
    f1_lambified = sp.lambdify((t, y1, y2, y3), f1, "math")
    f2_lambified = sp.lambdify((t, y1, y2, y3), f2, "math")
    f3_lambified = sp.lambdify((t, y1, y2, y3), f3, "math")

    # Listas para almacenar los resultados
    t_values = [t_min]
    y1_values = [y1_inicial]
    y2_values = [y2_inicial]
    y3_values = [y3_inicial]

    k1_values_1, k2_values_1, k3_values_1, k4_values_1 = [], [], [], []
    k1_values_2, k2_values_2, k3_values_2, k4_values_2 = [], [], [], []
    k1_values_3, k2_values_3, k3_values_3, k4_values_3 = [], [], [], []

    # Iterador
    i = 0
    i_values = [i]

    tabla = []

    first_iteration = True

    while t_min <= (t_max + h / 2):
        # Calcular k1, k2, k3 y k4 para cada ecuación
        k1_1 = h * f1_lambified(t_min, y1_inicial, y2_inicial, y3_inicial)
        k1_2 = h * f2_lambified(t_min, y1_inicial, y2_inicial, y3_inicial)
        k1_3 = h * f3_lambified(t_min, y1_inicial, y2_inicial, y3_inicial)

        k2_1 = h * f1_lambified(
            t_min + h / 2,
            y1_inicial + k1_1 / 2,
            y2_inicial + k1_2 / 2,
            y3_inicial + k1_3 / 2,
        )
        k2_2 = h * f2_lambified(
            t_min + h / 2,
            y1_inicial + k1_1 / 2,
            y2_inicial + k1_2 / 2,
            y3_inicial + k1_3 / 2,
        )
        k2_3 = h * f3_lambified(
            t_min + h / 2,
            y1_inicial + k1_1 / 2,
            y2_inicial + k1_2 / 2,
            y3_inicial + k1_3 / 2,
        )

        k3_1 = h * f1_lambified(
            t_min + h / 2,
            y1_inicial + k2_1 / 2,
            y2_inicial + k2_2 / 2,
            y3_inicial + k2_3 / 2,
        )
        k3_2 = h * f2_lambified(
            t_min + h / 2,
            y1_inicial + k2_1 / 2,
            y2_inicial + k2_2 / 2,
            y3_inicial + k2_3 / 2,
        )
        k3_3 = h * f3_lambified(
            t_min + h / 2,
            y1_inicial + k2_1 / 2,
            y2_inicial + k2_2 / 2,
            y3_inicial + k2_3 / 2,
        )

        k4_1 = h * f1_lambified(
            t_min + h,
            y1_inicial + k3_1,
            y2_inicial + k3_2,
            y3_inicial + k3_3,
        )
        k4_2 = h * f2_lambified(
            t_min + h,
            y1_inicial + k3_1,
            y2_inicial + k3_2,
            y3_inicial + k3_3,
        )
        k4_3 = h * f3_lambified(
            t_min + h,
            y1_inicial + k3_1,
            y2_inicial + k3_2,
            y3_inicial + k3_3,
        )

        if first_iteration:
            print("=== Primera Iteracion ===")
            # Primera ecuación (dy1/dt)
            equation1_string = str(ecuacion1)
            equation1_k1 = (
                equation1_string.replace(str(t), f"({t_min:.6f})")
                .replace(str(y1), f"({y1_inicial:.6f})")
                .replace(str(y2), f"({y2_inicial:.6f})")
                .replace(str(y3), f"({y3_inicial:.6f})")
            )
            print(f"k1_1 = {h} * ({equation1_k1}) = {k1_1:.6f}")

            equation1_k2 = (
                equation1_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k1_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k1_2 / 2:.6f})")
                .replace(str(y3), f"({y3_inicial + k1_3 / 2:.6f})")
            )
            print(f"k2_1 = {h} * ({equation1_k2}) = {k2_1:.6f}")

            equation1_k3 = (
                equation1_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k2_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k2_2 / 2:.6f})")
                .replace(str(y3), f"({y3_inicial + k2_3 / 2:.6f})")
            )
            print(f"k3_1 = {h} * ({equation1_k3}) = {k3_1:.6f}")

            equation1_k4 = (
                equation1_string.replace(str(t), f"({t_min + h:.6f})")
                .replace(str(y1), f"({y1_inicial + k3_1:.6f})")
                .replace(str(y2), f"({y2_inicial + k3_2:.6f})")
                .replace(str(y3), f"({y3_inicial + k3_3:.6f})")
            )
            print(f"k4_1 = {h} * ({equation1_k4}) = {k4_1:.6f}")

            # Segunda ecuación (dy2/dt)
            equation2_string = str(ecuacion2)
            equation2_k1 = (
                equation2_string.replace(str(t), f"({t_min:.6f})")
                .replace(str(y1), f"({y1_inicial:.6f})")
                .replace(str(y2), f"({y2_inicial:.6f})")
                .replace(str(y3), f"({y3_inicial:.6f})")
            )
            print(f"k1_2 = {h} * ({equation2_k1}) = {k1_2:.6f}")

            equation2_k2 = (
                equation2_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k1_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k1_2 / 2:.6f})")
                .replace(str(y3), f"({y3_inicial + k1_3 / 2:.6f})")
            )
            print(f"k2_2 = {h} * ({equation2_k2}) = {k2_2:.6f}")

            equation2_k3 = (
                equation2_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k2_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k2_2 / 2:.6f})")
                .replace(str(y3), f"({y3_inicial + k2_3 / 2:.6f})")
            )
            print(f"k3_2 = {h} * ({equation2_k3}) = {k3_2:.6f}")

            equation2_k4 = (
                equation2_string.replace(str(t), f"({t_min + h:.6f})")
                .replace(str(y1), f"({y1_inicial + k3_1:.6f})")
                .replace(str(y2), f"({y2_inicial + k3_2:.6f})")
                .replace(str(y3), f"({y3_inicial + k3_3:.6f})")
            )
            print(f"k4_2 = {h} * ({equation2_k4}) = {k4_2:.6f}")

            # Tercera ecuación (dy3/dt)
            equation3_string = str(ecuacion3)
            equation3_k1 = (
                equation3_string.replace(str(t), f"({t_min:.6f})")
                .replace(str(y1), f"({y1_inicial:.6f})")
                .replace(str(y2), f"({y2_inicial:.6f})")
                .replace(str(y3), f"({y3_inicial:.6f})")
            )
            print(f"k1_3 = {h} * ({equation3_k1}) = {k1_3:.6f}")

            equation3_k2 = (
                equation3_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k1_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k1_2 / 2:.6f})")
                .replace(str(y3), f"({y3_inicial + k1_3 / 2:.6f})")
            )
            print(f"k2_3 = {h} * ({equation3_k2}) = {k2_3:.6f}")

            equation3_k3 = (
                equation3_string.replace(str(t), f"({t_min + h / 2:.6f})")
                .replace(str(y1), f"({y1_inicial + k2_1 / 2:.6f})")
                .replace(str(y2), f"({y2_inicial + k2_2 / 2:.6f})")
                .replace(str(y3), f"({y3_inicial + k2_3 / 2:.6f})")
            )
            print(f"k3_3 = {h} * ({equation3_k3}) = {k3_3:.6f}")

            equation3_k4 = (
                equation3_string.replace(str(t), f"({t_min + h:.6f})")
                .replace(str(y1), f"({y1_inicial + k3_1:.6f})")
                .replace(str(y2), f"({y2_inicial + k3_2:.6f})")
                .replace(str(y3), f"({y3_inicial + k3_3:.6f})")
            )
            print(f"k4_3 = {h} * ({equation3_k4}) = {k4_3:.6f}")

            first_iteration = False

        # Actualizar los valores de y1, y2 y y3
        y1_inicial += (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
        y2_inicial += (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6
        y3_inicial += (k1_3 + 2 * k2_3 + 2 * k3_3 + k4_3) / 6

        # Actualizar los valores en las listas
        t_min += h
        i += 1
        i_values.append(i)
        k1_values_1.append(k1_1)
        k2_values_1.append(k2_1)
        k3_values_1.append(k3_1)
        k4_values_1.append(k4_1)

        k1_values_2.append(k1_2)
        k2_values_2.append(k2_2)
        k3_values_2.append(k3_2)
        k4_values_2.append(k4_2)

        k1_values_3.append(k1_3)
        k2_values_3.append(k2_3)
        k3_values_3.append(k3_3)
        k4_values_3.append(k4_3)

        t_values.append(t_min)
        y1_values.append(y1_inicial)
        y2_values.append(y2_inicial)
        y3_values.append(y3_inicial)

        tabla.append(
            [
                i,
                t_min,
                y1_inicial,
                y2_inicial,
                y3_inicial,
                k1_1,
                k2_1,
                k3_1,
                k4_1,
                k1_2,
                k2_2,
                k3_2,
                k4_2,
                k1_3,
                k2_3,
                k3_3,
                k4_3,
            ]
        )

    # Imprimir los resultados
    headers = [
        "i",
        "t",
        "y1",
        "y2",
        "y3",
        "k1_1",
        "k2_1",
        "k3_1",
        "k4_1",
        "k1_2",
        "k2_2",
        "k3_2",
        "k4_2",
        "k1_3",
        "k2_3",
        "k3_3",
        "k4_3",
    ]
    print("\nResultados en forma de tabla:")
    print(tabulate(tabla, headers=headers, floatfmt=".6f", tablefmt="github"))
    input()
