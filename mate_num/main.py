# main.py
import os

from euler import main as euler

# Jkfrom euler import euler
from integracion import menu as in_menu
from minimos_cuadrados import menu as mc_menu
from rk_orden_2 import menu as rk_orden_2_menu
from runge_kutta import menu as rk_menu
from taylor import main as taylor


def menu():
    """menu principal"""
    clear_terminal()
    while True:
        print("Elige el tipo de problema")
        print("1. Minimos Cuadrados")
        print("2. Runge-Kutta de Orden 4")
        print("3. Euler")
        print("4. Taylor")
        print("5. Runge-Kutta de Orden 2")
        print("6. Integracion Numerica")
        print("7. Exit")
        choice = input("Introduce un valor (1-X): ")
        if choice == "1":
            clear_terminal()
            mc_menu()
            clear_terminal()
        elif choice == "2":
            clear_terminal()
            rk_menu()
            clear_terminal()
        elif choice == "3":
            clear_terminal()
            euler()
            clear_terminal()
        elif choice == "4":
            clear_terminal()
            taylor()
            clear_terminal()
        elif choice == "5":
            clear_terminal()
            rk_orden_2_menu()
            clear_terminal()
        elif choice == "6":
            clear_terminal()
            in_menu()
            clear_terminal()
        elif choice == "7":
            print("\n==== Exiting the program. ====")
            break
        else:
            clear_terminal()
            print("Elige un valor valido")


def clear_terminal():
    """limpia la terminal"""
    os.system("clear" if os.name != "nt" else "cls")


menu()
