import os

import sympy as sp


def clear_terminal():
    """limpia la terminal"""
    os.system("clear" if os.name != "nt" else "cls")


def regla_trapezoidal_compuesta_sympy(func_input, a, b, n):
    """
    Calcula la integral definida de una función usando la regla trapezoidal compuesta,
    mostrando los pasos del cálculo, con SymPy para el manejo simbólico.

    Parámetros:
        func_input: función a integrar como texto (string).
        a: límite inferior de la integral.
        b: límite superior de la integral.
        n: número de subintervalos.

    Retorna:
        Aproximación de la integral en el intervalo [a, b].
    """
    # Definir la variable simbólica y la función
    x = sp.symbols("x")
    f = sp.sympify(func_input)

    # Calcular el tamaño del paso (h)
    h = (b - a) / n
    print(f"Tamaño del paso (h): {h:.6f}\n")

    # Evaluar los extremos
    #    print("Paso 1: Evaluar los extremos de la integral:")
    f_a = f.subs(x, a)
    f_b = f.subs(x, b)
    #    print(f"  f({a}) = {f} = {f_a:.6f}")
    #    print(f"  f({b}) = {f} = {f_b:.6f}\n")
    suma = f_a + f_b

    # Evaluar los puntos intermedios
    #    print("Paso 2: Evaluar los puntos intermedios y multiplicar por 2:")
    for i in range(1, n):
        x_i = a + i * h
        f_xi = f.subs(x, x_i)
        print(
            f"  x_{i} = {x_i:.6f}, f(x_{i}) = {f} = {f_xi:.6f}\n      Multiplicado por 2 = 2 * f(x_{i}) = {2 * f_xi:.6f}"
        )
        suma += 2 * f_xi

    #    print(
    #        f"\nSuma total (incluyendo extremos y puntos intermedios multiplicados por 2): {suma:.6f}"
    #    )

    # Aplicar la fórmula de la regla trapezoidal compuesta
    integral = (h / 2) * suma
    #    print(f"\nPaso 3: Aplicar la fórmula de la regla trapezoidal compuesta:")
    #    print(
    #        f"  Integral ≈ (h / 2) * Suma = ({h:.6f} / 2) * {suma:.6f} = {integral:.6f}\n"
    #    )

    return float(integral)


# Ejemplo de uso
def main():
    # Definir los datos de entrada
    print("Cálculo de la regla trapezoidal compuesta paso a paso (usando SymPy):\n")
    func_input = input("Introduce la funcion a integrar: ")  # Función como string
    a = int(input("Introduce el limite inferior de la integral: "))  # Límite inferior
    b = int(input("Introduce el limite superior de la integral: "))  # Límite superior
    n = int(
        input(
            "Introduce el numero de divisiones (1 para newton cotes-cerrada / regla trapezoidal): "
        )
    )  # Número de subintervalos

    # Calcular la integral
    resultado = regla_trapezoidal_compuesta_sympy(func_input, a, b, n)
    print(f"El valor aproximado de la integral es: {resultado:.6f}")

    solucion_real = sp.integrate(sp.sympify(func_input), (sp.symbols("x"), a, b))
    integral_indicada = str(sp.integrate(sp.simplify(func_input)))
    print(f"Integral indicada {integral_indicada}")
    print(f"La solución real de la integral es: {float(solucion_real):.6f}")
    input("Presiona intro para continuar")
