import numpy as np
from tabulate import tabulate


def menu():
    """menu minimos cuadrados"""
    while True:
        print("Elige el tipo de minimo")
        print("1. Lineal")
        print("2. Polinomial")
        print("3. Exponencial")
        print("4. Potencial")
        print("5. Salir")
        choice = input("Introduce un valor (1-5): ")
        if choice == "1":
            lineal()
            input("Presiona intro para continuar")
            break
        elif choice == "2":
            polinomial()
            input("Presiona intro para continuar")
            break
        elif choice == "3":
            exponencial()
            input("Presiona intro para continuar")
            break
        elif choice == "4":
            potencial()
            input("Presiona intro para continuar")
            break
        elif choice == "5":
            break
        else:
            print("Elige un valor valido")


def pedir_datos():
    """Solicita al usuario los valores de n, x y y para los cálculos."""
    # Solicitar la cantidad de puntos
    #    n = int(input("¿Cuántos puntos deseas ingresar? "))

    n = 10
    # Inicializar listas vacías para x y y
    x = [4, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
    y = [102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

    # print("Introduce los puntos (x, y):")
    # for i in range(n):
    # Solicitar cada punto en formato x,y
    #    punto = input(f"Punto {i+1} (formato x,y): ")
    #    xi, yi = map(float, punto.split(","))
    #    x.append(xi)
    #    y.append(yi)

    return n, x, y


def exponencial():
    """minimos cuadrados exponencial"""
    # Datos predefinidos para pruebas

    n, x, y = pedir_datos()
    # Convertir listas a arrays de numpy
    x = np.array(x)
    y = np.array(y)

    # Transformar y a ln(y)
    ln_y = np.log(y)

    # Calcular valores adicionales
    x2 = x**2
    x_ln_y = x * ln_y

    # Crear la tabla de datos
    data = [
        ["----", x[i], y[i], round(ln_y[i], 5), round(x2[i], 5), round(x_ln_y[i], 5)]
        for i in range(n)
    ]
    data.append(["-" * 4, "-" * 5, "-" * 5, "-" * 5, "-" * 5, "-" * 5])
    data.append(
        [
            "SUMA",
            round(np.sum(x), 5),
            round(np.sum(y), 5),
            round(np.sum(ln_y), 5),
            round(np.sum(x2), 5),
            round(np.sum(x_ln_y), 5),
        ]
    )
    headers = ["----", "x", "y", "ln(y)", "x^2", "x * ln(y)"]

    print("\n=== Tabla de Datos ===")
    print(tabulate(data, headers=headers, floatfmt=".5f", tablefmt="pretty"))

    # Cálculos paso a paso
    print("\n=== Cálculos Paso a Paso ===")
    sum_x = round(np.sum(x), 5)
    sum_ln_y = round(np.sum(ln_y), 5)
    sum_x2 = round(np.sum(x2), 5)
    sum_x_ln_y = round(np.sum(x_ln_y), 5)

    # Fórmulas para a1 (b) y a0 (ln(a))
    print("\n=== Cálculo de la pendiente a1 ===")
    num_b = round(n * sum_x_ln_y - sum_x * sum_ln_y, 5)
    den = round(n * sum_x2 - sum_x**2, 5)
    b = round(num_b / den, 5)
    print(
        f"a1 = ({n} * {sum_x_ln_y:.5f} - {sum_x:.5f} * {sum_ln_y:.5f}) / ({n} * {sum_x2:.5f} - ({sum_x:.5f})^2) = {b:.5f}"
    )

    print("\n=== Cálculo de a0 ===")
    num_ln_a = round(sum_ln_y * sum_x2 - sum_x * sum_x_ln_y, 5)
    ln_a = round(num_ln_a / den, 5)
    print(
        f"a0 = ({sum_ln_y:.5f} * {sum_x2:.5f} - {sum_x:.5f} * {sum_x_ln_y:.5f}) / ({n} * {sum_x2:.5f} - ({sum_x:.5f})^2) = {ln_a:.5f}"
    )

    print("\n=== Cálculo de b ===")
    print(f"b = e^a0 = e ^ {ln_a:.5f} = {b:.5f}")

    # Convertir ln(a) a a
    a = round(np.exp(ln_a), 5)

    # Mostrar la ecuación de la curva
    print("\n=== Resultados ===")
    print(f"Ecuación de la curva: y = {a:.5f} * e^({b:.5f} * x)")


def polinomial():
    """minimos cuadrados polinomial"""
    n, x, y = pedir_datos()
    # Convertir listas a arrays de numpy
    x = np.array(x)
    y = np.array(y)

    # Calcular valores adicionales
    x2 = x**2
    x3 = x**3
    x4 = x**4
    x_y = x**0 * y
    x2_y = x2 * y

    # Crear la tabla de datos en el orden solicitado
    data = [
        ["----", 1, x[i], x2[i], x3[i], x4[i], y[i], x_y[i], x[i] * y[i], x2_y[i]]
        for i in range(n)
    ]
    data.append(
        [
            "-" * 4,
            "-" * 5,
            "-" * 5,
            "-" * 5,
            "-" * 5,
            "-" * 5,
            "-" * 5,
            "-" * 5,
            "-" * 5,
            "-" * 5,
        ]
    )
    data.append(
        [
            "SUMA",
            round(np.sum(x**0), 5),  # Suma de x^0 (que es simplemente n)
            round(np.sum(x), 5),
            round(np.sum(x2), 5),
            round(np.sum(x3), 5),
            round(np.sum(x4), 5),
            round(np.sum(y), 5),
            round(np.sum(x_y), 5),
            round(np.sum(x * y), 5),
            round(np.sum(x2 * y), 5),
        ]
    )
    headers = [
        "----",
        "x^0",
        "x^1",
        "x^2",
        "x^3",
        "x^4",
        "y",
        "x^0*y",
        "x^1*y",
        "x^2*y",
    ]

    print("\n=== Tabla de Datos ===")
    print(tabulate(data, headers=headers, floatfmt=".5f", tablefmt="pretty"))

    # Formar la matriz para resolver el sistema
    A = np.array(
        [
            [n, np.sum(x), np.sum(x2)],
            [np.sum(x), np.sum(x2), np.sum(x3)],
            [np.sum(x2), np.sum(x3), np.sum(x4)],
        ]
    )

    B = np.array([np.sum(y), np.sum(x * y), np.sum(x2 * y)])

    # Mostrar la matriz A y el vector B
    print("\nMatriz:")
    for i in range(len(B)):
        # Imprimir la fila de la matriz A y luego el valor correspondiente de B a la derecha
        print(
            " ".join([f"{A[i, j]:>10.5f}" for j in range(A.shape[1])])
            + f" | {B[i]:>10.5f}"
        )

    # Resolver el sistema de ecuaciones
    coef = np.linalg.solve(A, B)

    a2, a1, a0 = coef

    print(f"\na0 = {a2:.5f}")
    print(f"a1 = {a1:.5f}")
    print(f"a2 = {a0:.5f}")

    # Mostrar la ecuación del polinomio
    print("\n=== Resultados ===")
    print(f"Ecuación del polinomio: y = {a0:.5f} * x^2 + {a1:.5f} * x + {a2:.5f}")


def potencial():
    """minimos cuadrados potencial"""
    # Datos predefinidos para pruebas
    n, x, y = pedir_datos()
    # Convertir listas a arrays de numpy
    x = np.array(x)
    y = np.array(y)

    # Transformar x e y a ln(x) y ln(y)
    ln_x = np.log(x)
    ln_y = np.log(y)

    # Calcular valores adicionales
    x2 = ln_x**2
    x_ln_y = ln_x * ln_y

    # Crear la tabla de datos
    data = [
        [
            "----",
            x[i],
            y[i],
            round(ln_x[i], 5),
            round(ln_y[i], 5),
            round(x2[i], 5),
            round(x_ln_y[i], 5),
        ]
        for i in range(n)
    ]
    data.append(["-" * 4, "-" * 5, "-" * 5, "-" * 5, "-" * 5, "-" * 5, "-" * 5])
    data.append(
        [
            "SUMA",
            round(np.sum(x), 5),
            round(np.sum(y), 5),
            round(np.sum(ln_x), 5),
            round(np.sum(ln_y), 5),
            round(np.sum(x2), 5),
            round(np.sum(x_ln_y), 5),
        ]
    )
    headers = ["----", "x", "y", "ln(x)", "ln(y)", "ln(x)^2", "ln(x) * ln(y)"]

    print("\n=== Tabla de Datos ===")
    print(tabulate(data, headers=headers, floatfmt=".5f", tablefmt="pretty"))

    # Cálculos paso a paso
    print("\n=== Cálculos Paso a Paso ===")
    sum_x = round(np.sum(ln_x), 5)
    sum_y = round(np.sum(ln_y), 5)
    sum_x2 = round(np.sum(x2), 5)
    sum_x_ln_y = round(np.sum(x_ln_y), 5)

    # Fórmulas para b y ln(a)
    print("\n=== Cálculo de la pendiente a1 ===")
    num_b = round(n * sum_x_ln_y - sum_x * sum_y, 5)
    den = round(n * sum_x2 - sum_x**2, 5)
    a = round(num_b / den, 5)
    print(
        f"a1 = ({n} * {sum_x_ln_y:.5f} - {sum_x:.5f} * {sum_y:.5f}) / ({n} * {sum_x2:.5f} - ({sum_x:.5f})^2) = {a:.5f}"
    )

    print("\n=== Cálculo de a0 ===")
    num_ln_a = round(sum_y * sum_x2 - sum_x * sum_x_ln_y, 5)
    ln_a = round(num_ln_a / den, 5)
    print(
        f"a0 = ({sum_y:.5f} * {sum_x2:.5f} - {sum_x:.5f} * {sum_x_ln_y:.5f}) / ({n} * {sum_x2:.5f} - ({sum_x:.5f})^2) = {ln_a:.5f}"
    )

    b = round(np.exp(ln_a), 5)
    print("\n=== Cálculo de b ===")
    print(f"b = e^a0 = e ^ {ln_a:.5f} = {b:.5f}")

    # Mostrar la ecuación de la curva
    print("\n=== Resultados ===")
    print(f"Ecuación de la curva: y = {b:.5f} * x^{a:.5f}")


def lineal():
    """minimos cuadrados lineal"""
    # Solicitar datos al usuario
    n, x, y = pedir_datos()

    # Convertir las listas a arrays de numpy
    x = np.array(x)
    y = np.array(y)

    # Calcular valores adicionales
    x2 = x**2
    xy = x * y

    # Crear la tabla de datos
    data = [["----", x[i], y[i], x2[i], xy[i]] for i in range(n)]
    data.append(["-" * 4, "-" * 5, "-" * 5, "-" * 5, "-" * 5])
    data.append(["SUMA", np.sum(x), np.sum(y), np.sum(x2), np.sum(xy)])
    headers = ["----", "x", "y", "x^2", "x*y"]

    print("\n=== Tabla de Datos ===")
    print(tabulate(data, headers=headers, floatfmt=".4f", tablefmt="pretty"))

    # Cálculos paso a paso
    print("\n=== Cálculos Paso a Paso ===")
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(xy)
    sum_x2 = np.sum(x2)

    # Fórmulas para m y b
    print("\n=== Cálculo de la pendiente (a1) ===")
    num_m = n * sum_xy - sum_x * sum_y
    den = n * sum_x2 - sum_x**2
    m = num_m / den
    print(
        f"a1 = {n} * {sum_xy:.4f} - {sum_x:.4f} * {sum_y:.4f} / {n} * {sum_x2:.4f} - ({sum_x:.4f})^2 = {m:.4f}"
    )

    print("\n=== Cálculo de la intersección (a0) ===")
    num_b = sum_y * sum_x2 - sum_x * sum_xy
    b = num_b / den  # El mismo denominador que m
    print(
        f"a0 = {sum_y:.4f} * {sum_x2:.4f} - {sum_x:.4f} * {sum_xy:.4f} / {n} * {sum_x2:.4f} - ({sum_x:.4f})^2 = {b:.4f}"
    )

    # Mostrar la ecuación de la recta
    print("\n=== Resultados ===")
    print(f"Ecuación de la recta: y = a1 * x + a0 = {m:.4f}x + {b:.4f}")
