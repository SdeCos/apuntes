import os

from simpson import main as simpson
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
        print("2. Trapezoidal compuesta")
        print("6. Exit")
        choice = input("Introduce un valor (1-X): ")
        if choice == "1":
            clear_terminal()
            simpson()
            clear_terminal()
        elif choice == "2":
            clear_terminal()
            trapezoidal_compuesta()
            clear_terminal()
        elif choice == "3":
            clear_terminal()
            clear_terminal()
        elif choice == "4":
            clear_terminal()
            clear_terminal()
        elif choice == "5":
            clear_terminal()
            clear_terminal()
        elif choice == "6":
            print("\n==== Exiting the program. ====")
            break
        else:
            clear_terminal()
            print("Elige un valor valido")
