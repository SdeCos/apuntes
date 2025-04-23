import numpy as np


def solicitar_datos():
    """
    Solicita al usuario los datos necesarios para calcular la integral usando la regla de Simpson compuesta.
    Aquí hemos comentado las líneas de entrada del usuario y colocado valores fijos para la prueba.

    Retorna:
        Una tupla con:
        - La ecuación de la función como string.
        - Los límites de integración (a, b).
        - El número de divisiones (n).
    """
    print("\nMétodo para calcular la integral usando la Regla de Simpson Compuesta")
    func_input = input(
        "Define la función a integrar en términos de x (ejemplo: cos(x)**2): "
    )
    a = float(input("Ingresa el límite inferior a: "))
    b = float(input("Ingresa el límite superior b: "))
    n = int(
        input(
            "Ingresa el número de divisiones n (debe ser par) n = 2 para hacer la regla de simpson: "
        )
    )

    return func_input, a, b, n


# Definir las funciones matemáticas sin necesidad de np.
def get_function(func_input):
    """
    Convierte la cadena de la función ingresada por el usuario a una función evaluable.
    """
    return lambda x: eval(
        func_input,
        {
            "x": x,
            "cos": np.cos,
            "sin": np.sin,
            "exp": np.exp,
            "tan": np.tan,
            "log": np.log,
        },
    )


# Implementar la regla de Simpson compuesta
def simpson_compuesto(f, a, b, n, func_input):
    # Si el número de divisiones no es par, lo ajustamos
    if n % 2 != 0:
        raise ValueError("El número de divisiones debe ser par.")

    # Calcular el valor de h
    h = (b - a) / n

    # Calcular el valor inicial de la integral
    integral = f(a) + f(b)
    f_string = str(func_input)
    f_a = f_string.replace("x", f"{a}")
    f_b = f_string.replace("x", f"{b}")
    #    print(
    #        f"Valores iniciales:\n   f({a}) = {f_a} = {f(a)}\n   f({b} = {f_b}) = {f(b)}\n"
    #    )

    # Calcular los sumandos para los puntos impares (multiplicados por 4)
    suma_impares = 0
    for i in range(1, n, 2):  # Impares: 1, 3, 5, ..., n-1
        x_i = a + i * h
        f_x_i = f(x_i)
        f_xi_indicada = f_string.replace("x", f"{x_i}")
        suma_impares += 4 * f_x_i
    #        print(
    #            f"f({x_i}) = {f_xi_indicada} = {f_x_i}, multiplicado por 4: 4 * {f_x_i} = {4 * f_x_i}"
    #        )

    # Calcular los sumandos para los puntos pares (multiplicados por 2)
    suma_pares = 0
    for i in range(2, n, 2):  # Pares: 2, 4, 6, ..., n-2
        x_i = a + i * h
        f_x_i = f(x_i)
        f_xi_indicada = f_string.replace("x", f"{x_i}")
        suma_pares += 2 * f_x_i
    #        print(
    #            f"f({x_i}) = {f_xi_indicada} = {f_x_i}, multiplicado por 2: 2 * {f_x_i} = {2 * f_x_i}"
    #        )

    # Mostrar las sumas intermedias
    print(f"Suma de los términos impares (multiplicados por 4): {suma_impares}")
    print(f"Suma de los términos pares (multiplicados por 2): {suma_pares}")

    # Calcular la integral final
    integral += suma_impares + suma_pares
    integral *= h / 3

    return integral


def main():
    # Solicitar los datos al usuario
    func_input, a, b, n = solicitar_datos()

    # Validar que el número de divisiones sea par
    if n % 2 != 0:
        print("Error: El número de divisiones debe ser par.")
    else:
        # Convertir la entrada de la función a una función evaluable
        f = get_function(func_input)

        # Calcular el valor de la integral usando la Regla de Simpson Compuesta
        resultado = simpson_compuesto(f, a, b, n, func_input)

        # Mostrar el resultado final
        print(f"\nEl valor de la integral es: {resultado}")
    input("Presiona intro para continuar")
