import numpy as np
import sympy as sp


def obtener_funcion_usuario():
    """
    Función para solicitar la ecuación de la forma 'f(t, y)' al usuario.
    El usuario debe introducir la ecuación de la derivada en términos de t e y.
    """
    # Comentado para pruebas automáticas
    # print("Introduce la ecuación diferencial de la forma f(t, y).")
    # print("Ejemplo: dy/dt = y - t, escribe: y - t")
    # print("Puedes usar funciones como 'exp(t)', 'np.sin(t)', etc.")
    # ecuacion = input("Ecuación (f(t, y)): ")
    ecuacion = "1 + y/t"  # Ecuación por defecto
    return ecuacion


def convertir_a_funcion(ecuacion):
    """
    Convierte la cadena de texto con la ecuación a una función simbólica.
    La ecuación debe estar en términos de 't' y 'y'.
    """
    t, y = sp.symbols("t y")
    # Reemplazar 'exp' por 'sp.exp' para que se utilicen las funciones de sympy
    ecuacion = ecuacion.replace("exp", "sp.exp")
    f = sp.sympify(ecuacion)  # Convertimos la ecuación a una expresión simbólica
    return f, t, y


def calcular_derivadas_parciales(f, t, y):
    """
    Calcula las derivadas parciales de f(t, y) con respecto a t y con respecto a y.
    """
    f_prime_t = sp.diff(f, t)  # Derivada de f con respecto a t
    f_prime_y = sp.diff(f, y)  # Derivada de f con respecto a y
    return f_prime_t, f_prime_y


def taylor_method(f, tmin, tmax, h, y0, n, ecuacion_original):
    """
    Resuelve la ecuación diferencial usando el método de Taylor de orden n.

    Parámetros:
    - f: función que define la ecuación diferencial
    - tmin: valor mínimo de t
    - tmax: valor máximo de t
    - h: tamaño del paso
    - y0: valor inicial de y en t = tmin
    - n: orden del método de Taylor (n)
    - ecuacion_original: ecuación original en formato de texto

    Devuelve:
    - t_values: arreglo con los valores de t
    - y_values: arreglo con los valores aproximados de y
    """
    # Inicializar los valores de t y y
    t_values = np.arange(tmin, tmax + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0  # El valor inicial de y

    # Convertir la ecuación a una función simbólica
    t, y = sp.symbols("t y")
    f, t, y = convertir_a_funcion(ecuacion_original)

    # Calcular las derivadas parciales
    f_prime_t, f_prime_y = calcular_derivadas_parciales(f, t, y)

    # Mostrar la derivada parcial con respecto a y
    print("\nEcuaciones derivadas:")
    print(f"y' = {f}")
    print(f"y'' = {f_prime_y}\n")  # Derivada con respecto a y

    # Realizar la iteración paso a paso
    print("\nIteraciones:")
    for i in range(1, len(t_values)):
        t_0 = t_values[i - 1]
        y_0 = y_values[i - 1]

        print("===================================")
        print(f"Paso {i}: t_{i-1} = {t_0}, y_{i-1} = {y_0}")

        f_string = str(f)
        f_sustituida = f_string.replace(str(t), f"({t_0:.6f})").replace(
            str(y), f"({y_0:.6f})"
        )
        # Evaluación de f(t_0, y_0)
        f_value = f.subs({t: t_0, y: y_0})
        print(f"f(t_0, y_0) = f({t_0}, {y_0}) = {f_sustituida}  =>  {f_value}")
        print(f"f({t_0}, {y_0}) = {f.subs({t: t_0, y: y_0})}")

        # Evaluación de la derivada parcial de f con respecto a y (f'_y)
        f_prime_y_value = f_prime_y.subs({t: t_0, y: y_0})
        print(f"f'_y({t_0}, {y_0}) = {f_prime_y_value}")

        # Fórmula de Taylor para la iteración
        wi = y_0 + h * f_value + (h**2 / 2) * f_prime_y_value
        print(
            f"\nCálculo de w_{i}: w_{i} = y_{i-1} + h * f(t_{i-1}, y_{i-1}) + (h^2 / 2) * f'_y(t_{i-1}, y_{i-1})"
        )
        print(
            f"w_{i} = {y_0} + {h} * {f_value} + ({h**2} / 2) * {f_prime_y_value} = {wi}"
        )
        print(f"w_{i} = {wi}\n")

        # Guardar el valor calculado de w_i
        y_values[i] = wi

    return t_values, y_values


def main():
    # Obtener la ecuación de la forma 'f(t, y)'
    ecuacion = obtener_funcion_usuario()

    # Asignar valores por defecto para las pruebas
    tmin = 1.0  # Valor mínimo de t
    tmax = 2.0  # Valor máximo de t
    h = 0.25  # Tamaño del paso
    y0 = 2.0  # Valor inicial de y (y(1) = 2)
    n = 3  # Orden del método de Taylor

    # Resolver la ecuación diferencial usando el método de Taylor
    t_values, y_values = taylor_method(ecuacion, tmin, tmax, h, y0, n, ecuacion)


# Ejecutar el programa
if __name__ == "__main__":
    main()
