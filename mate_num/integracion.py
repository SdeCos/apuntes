import os

from newton_cotes_cerrada import main as newton_cotes_cerrada
from punto_medio_compuesta import main as punto_medio_compuesta
from simpson import main as simpson
from simpson_3_8 import main as simpson_3_8
from trapezoidal_compuesta import main as trapezoidal_compuesta


def clear_terminal():
    """limpia la terminal"""
    os.system("clear" if os.name != "nt" else "cls")


def menu():
    """menu principal"""
    clear_terminal()
    while True:
        print("Elige el tipo de problema")
        print("1. Simpson")
        print("2. Trapezoidal")
        print("3. Newton Cotes Cerrada (Regla de Simpson 3/8)")
        print("4. Newton Cotes Cerrada")
        print("6. Exit")
        choice = input("Introduce un valor (1-X): ")
        if choice == "1":
            clear_terminal()
            simpson()
            input("Presiona intro para continuar")
            clear_terminal()
        elif choice == "2":
            clear_terminal()
            trapezoidal_compuesta()
            input("Presiona intro para continuar")
            clear_terminal()
        elif choice == "3":
            clear_terminal()
            simpson_3_8()
            input("Presiona intro para continuar")
            clear_terminal()
        elif choice == "4":
            clear_terminal()
            newton_cotes_cerrada()
            input("Presiona intro para continuar")
            clear_terminal()
        elif choice == "5":
            clear_terminal()
            punto_medio_compuesta()
            input("Presiona intro para continuar")
            clear_terminal()
        elif choice == "6":
            print("\n==== Exiting the program. ====")
            break
        else:
            clear_terminal()
            print("Elige un valor valido")
