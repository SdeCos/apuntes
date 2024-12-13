# main.py
import os

from euler import main as euler

# Jkfrom euler import euler
from minimos_cuadrados import menu as mc_menu
from runge_kutta import menu as rk_menu


def menu():
    """menu principal"""
    clear_terminal()
    while True:
        print("Elige el tipo de problema")
        print("1. Minimos Cuadrados")
        print("2. Metodo de Runge-Kutta")
        print("3. Euler")
        print("5. Exit")
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
        elif choice == "5":
            print("\n==== Exiting the program. ====")
            break
        else:
            clear_terminal()
            print("Elige un valor valido")


def clear_terminal():
    """limpia la terminal"""
    os.system("clear" if os.name != "nt" else "cls")


menu()
