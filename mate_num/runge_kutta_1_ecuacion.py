import sympy as sp
from sympy import exp, symbols


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

    print("Resultados (t, y):")
    for i, t, y, k1, k2, k3, k4 in zip(
        i_values, t_values, y_values, k1_values, k2_values, k3_values, k4_values
    ):
        print(
            f"i = {i}, t = {t:.6f}, y = {y:.6f}, k1 = {k1:.6f}, k2 = {k2:.6f}, k3 = {k3:.6f}, k4 = {k4:.6f}"
        )
    input("Presiona intro para continuar")
