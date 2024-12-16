import numpy as np


def euler_method(f, y0, tmin, tmax, h, ecuacion):
    """
    Resuelve una ecuación diferencial utilizando el método de Euler.
    Parámetros:
    f : función - La ecuación diferencial en forma f(t, y)
    y0 : float - Condición inicial para y en t = tmin
    tmin : float - Valor mínimo de t
    tmax : float - Valor máximo de t
    h : float - Tamaño del paso (step size)
    Devuelve:
    t_values : array - Los valores de t
    y_values : array - Los valores aproximados de y
    f_values : array - Los valores de f(t, y) en cada paso
    """
    # Inicializar valores
    t_values = np.arange(tmin, tmax + h, h)
    y_values = np.zeros(len(t_values))
    f_values = np.zeros(len(t_values))
    y_values[0] = y0
    # Aplicar el método de Euler
    for i in range(1, len(t_values)):
        f_values[i - 1] = f(t_values[i - 1], y_values[i - 1])  # Evaluamos f(t_i, w_i)
        # if i == 1:
        # print(f"\nPrimera iteración:")
        # print(f"  t_{i-1} = {t_values[i-1]:.7f}  ")
        # print(f"  w_{i-1} = {y_values[i-1]:.7f}  ")
        # ecuacion_con_valores = ecuacion.replace(
        #    "t", f"{t_values[i-1]:.7f}"
        # ).replace("y", f"{y_values[i-1]:.7f}")
        # print(
        #    f"  f(t_{i-1}, w_{i-1}) = {ecuacion_con_valores} = {f_values[i-1]:.7f}  "
        # )
        # print(f"  Cálculo de w_{i} = w_{i-1} + h * f(t_{i-1}, w_{i-1})")
        # y_result_primera_iteracion = y_values[i - 1] + h * f_values[i - 1]
        # print(
        #    f"  w_{i} = {y_values[i-1]:.7f} + {h:.7f} * {f_values[i-1]:.7f} = {y_result_primera_iteracion:.7f}"
        # )
        y_values[i] = y_values[i - 1] + h * f_values[i - 1]  # Método de Euler
    # Evaluamos f en el último valor
    f_values[-1] = f(t_values[-1], y_values[-1])
    return t_values, y_values, f_values


# Solicitar los datos al usuario
def obtener_funcion_usuario():
    print("Introduce la ecuación diferencial en formato 'f(t, y)'.")
    print("Por ejemplo, si la ecuación es dy/dt = y - t, escribe: 'y - t'")
    print("Nota: Usa 't' para la variable independiente y 'y' para la dependiente.")
    print("Puedes usar funciones como 'exp(t)', 'np.sin(t)', 'np.cos(t)', etc.")
    ecuacion = input("Ecuación: ")
    return ecuacion


def convertir_a_funcion(ecuacion):
    """
    Convierte una cadena de texto de una ecuación a una función de Python.
    Asume que el usuario usa 't' y 'y' como variables.
    Sustituye 'exp' por 'np.exp' para que sea válido.
    """
    # Sustituir 'exp' por 'np.exp' en la ecuación
    ecuacion = ecuacion.replace("exp", "np.exp")

    # Convierte la ecuación a una función utilizando eval
    # Definimos 'np' como el entorno para la ejecución de las funciones matemáticas
    def f(t, y):
        return eval(ecuacion, {"np": np, "t": t, "y": y})

    return f


# Función principal
def main():
    # Obtener la ecuación de la forma 'f(t, y)'
    ecuacion = obtener_funcion_usuario()
    # Convertir la ecuación a una función de Python
    f = convertir_a_funcion(ecuacion)
    # Solicitar los valores de tmin, tmax, h y y0
    tmin = float(input("Introduce el valor mínimo de t (tmin): "))
    tmax = float(input("Introduce el valor máximo de t (tmax): "))
    h = float(input("Introduce el tamaño del paso h: "))
    y0 = float(input("Introduce el valor inicial de y (y0): "))
    # Resolver la ecuación diferencial utilizando el método de Euler
    t_values, y_values, f_values = euler_method(f, y0, tmin, tmax, h, ecuacion)
    # Imprimir los resultados
    print("\nResultados:")
    print(f"{'ti':>10} {'wi':>15} {'f(ti, wi)':>15}")
    print("-" * 45)
    for t, y, f_val in zip(t_values, y_values, f_values):
        print(f"{t:>10.7f} {y:>15.7f} {f_val:>15.7f}")

    input("Presiona intro para continuar")


# Ejecutar el programa
if __name__ == "__main__":
    main()
