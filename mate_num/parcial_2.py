import os

import sympy as sp
from sympy import *


def integracion_numerica():
    """integracion numerica"""
    print("==== Integracion Numerica ====")


def diferenciacion_numerica():
    """diferenciacion numerica"""
    print("==== Diferenciacion Numerica ====")


def integracion_numerica_compuesta():
    """integracion numerica compuesta"""
    print("==== Integracion Numerica Compuesta ====")


def taylor():
    """metodo de taylor"""
    print("==== Metodo de Taylor ====")


def runge_kutta():
    """metodo de runge kutta"""
    print("==== Metodo de Runge-Kutta ====")
    y, t = symbols("y t")
    equation = exp(t) + y + 1
    t_min = 0.0
    t_max = 1
    wi = 1
    h = 0.5
    #    equation = input("Introduce la ecuacion:")
    #    t_min = float(input("Introduce el valor minimo de t: "))
    #    t_max = float(input("Introduce el valor maximo de t: "))
    #    wi = float(input("Introduce el valor de y en t_min: "))
    #    h = float(input("Introduce el valor de h: "))
    f = sp.simplify(equation)
    f_lambified = sp.lambdify((t, y), f, "math")

    t_values = [t_min]
    y_values = [wi]
    k1_values = []
    k2_values = []
    k3_values = []
    k4_values = []
    first_iteration = true

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
            equation_k1 = equation_k1.replace(str(t), f"({t_min})").replace(
                str(y), f"({wi})"
            )
            print(f"k1 = {h} * {equation_k1} = {k1}")

            # Second iteration (k2)
            equation_k2 = equation_string
            # Replace t and y in one pass
            equation_k2 = equation_k2.replace(str(t), f"({t_min + h / 2})").replace(
                str(y), f"({wi + k1 / 2})"
            )
            print(f"k2 = {h} * {equation_k2} = {k2}")

            # Third iteration (k3)
            equation_k3 = equation_string
            # Replace t and y in one pass
            equation_k3 = equation_k3.replace(str(t), f"({t_min + h / 2})").replace(
                str(y), f"({wi + k2 / 2})"
            )
            print(f"k3 = {h} * {equation_k3} = {k3}")

            # Fourth iteration (k4)
            equation_k4 = equation_string
            # Replace t and y in one pass
            equation_k4 = equation_k4.replace(str(t), f"({t_min + h})").replace(
                str(y), f"({wi + k3})"
            )
            print(f"k4 = {h} * {equation_k4} = {k4}")

            first_iteration = False

        wi += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t_min += h

        k1_values.append(k1)
        k2_values.append(k2)
        k3_values.append(k3)
        k4_values.append(k4)

        t_values.append(t_min)
        y_values.append(wi)

    print("Resultados (t, y):")
    for t, y, k1, k2, k3, k4 in zip(
        t_values, y_values, k1_values, k2_values, k3_values, k4_values
    ):
        print(
            f"t = {t:.6f}, y = {y:.6f}, k1 = {k1:.6f}, k2 = {k2:.6f}, k3 = {k3:.6f}, k4 = {k4:.6f}"
        )
    input("Presiona intro para continuar")
    clear_terminal()


def menu():
    """menu principal"""
    clear_terminal()
    while True:
        print("Elige el tipo de problema")
        print("1. Integracion numerica")
        print("2. Diferenciacion numerica")
        print("3. Integracion Numerica Compuesta")
        print("4. Metodo de Euler")
        print("5. Metodo de Taylor")
        print("6. Metodo de Runge-Kutta")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            clear_terminal()
            integracion_numerica()
        elif choice == "2":
            clear_terminal()
            diferenciacion_numerica()
        elif choice == "3":
            clear_terminal()
            integracion_numerica_compuesta()
        elif choice == "4":
            clear_terminal()
            euler()
        elif choice == "5":
            clear_terminal()
            taylor()
        elif choice == "6":
            clear_terminal()
            runge_kutta()
        elif choice == "7":
            print("\n==== Exiting the program. ====")
            break
        else:
            print("Elige un valor valido")


def clear_terminal():
    os.system("clear" if os.name != "nt" else "cls")


menu()
