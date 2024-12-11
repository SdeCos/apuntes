# main.py
import os

from diferenciacion_numerica import diferenciacion_numerica
from integracion_numerica import integracion_numerica
from integracion_numerica_compuesta import integracion_numerica_compuesta
from runge_kutta_1_ecuacion import runge_kutta_1_ecuacion
from runge_kutta_sistema_ecuaciones import runge_kutta_sistema_ecuaciones
from taylor import taylor


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
        print("6. Metodo de Runge-Kutta 1 ecuacion")
        print("7. Metodo de Runge-Kutta sistema de ecuaciones")
        print("8. Exit")
        choice = input("Enter your choice (1-7): ")
        if choice == "1":
            clear_terminal()
            integracion_numerica()
            clear_terminal()
        elif choice == "2":
            clear_terminal()
            diferenciacion_numerica()
            clear_terminal()
        elif choice == "3":
            clear_terminal()
            integracion_numerica_compuesta()
            clear_terminal()
        elif choice == "4":
            clear_terminal()
            euler()
            clear_terminal()
        elif choice == "5":
            clear_terminal()
            taylor()
            clear_terminal()
        elif choice == "6":
            clear_terminal()
            runge_kutta_1_ecuacion()
            clear_terminal()
        elif choice == "7":
            clear_terminal()
            runge_kutta_sistema_ecuaciones()
            clear_terminal()
        elif choice == "8":
            print("\n==== Exiting the program. ====")
            break
        else:
            print("Elige un valor valido")


def clear_terminal():
    os.system("clear" if os.name != "nt" else "cls")


menu()
