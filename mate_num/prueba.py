import numpy as np


def solicitar_datos():
    """
    Solicita los datos necesarios para calcular la integral usando la Regla de Simpson Compuesta.
    """
    # Para propósitos de prueba, se sustituyen los inputs por valores fijos
    print("\nMétodo para calcular la integral usando la Regla de Simpson Compuesta")

    # Datos de prueba (valores fijos)
    func_input = "cos(x)**2"  # La función a integrar
    a = -0.5  # Límite inferior
    b = 0.5  # Límite superior
    n = 4  # Número de divisiones (debe ser par)

    return func_input, a, b, n


# Definir la función matemática
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


# Implementar la Regla de Simpson Compuesta
def simpson_compuesto(f, a, b, n):
    """
    Aplica la regla de Simpson compuesta para calcular la integral de f en el intervalo [a, b] con n subintervalos.
    """
    # Si el número de divisiones no es par, lo ajustamos
    if n % 2 != 0:
        raise ValueError("El número de divisiones debe ser par.")

    # Calcular el valor de h
    h = (b - a) / n

    # Iniciar la integral con los valores en a y b
    integral = f(a) + f(b)

    print(f"Valor inicial: f({a}) = {f(a)} y f({b}) = {f(b)}")

    # Calcular los sumandos para los puntos impares (multiplicados por 4)
    suma_impares = 0
    for i in range(1, n, 2):  # Impares: 1, 3, 5, ..., n-1
        x_i = a + i * h
        f_x_i = f(x_i)
        suma_impares += 4 * f_x_i
        print(f"f({x_i}) = {f_x_i}, multiplicado por 4: 3 * {f_x_i} = {4 * f_x_i}")

    # Calcular los sumandos para los puntos pares (multiplicados por 2)
    suma_pares = 0
    for i in range(2, n, 2):  # Pares: 2, 4, 6, ..., n-2
        x_i = a + i * h
        f_x_i = f(x_i)
        suma_pares += 2 * f_x_i
        print(f"f({x_i}) = {f_x_i}, multiplicado por 2: 2 * {f_x_i} = {2 * f_x_i}")

    # Mostrar las sumas intermedias
    print(f"Suma de los términos impares (multiplicados por 4): {suma_impares}")
    print(f"Suma de los términos pares (multiplicados por 2): {suma_pares}")

    # Calcular la integral final
    integral += suma_impares + suma_pares
    integral *= h / 3

    return integral


# Solicitar los datos
func_input, a, b, n = solicitar_datos()

# Validar que el número de divisiones sea par
if n % 2 != 0:
    print("Error: El número de divisiones debe ser par.")
else:
    # Convertir la entrada de la función a una función evaluable
    f = get_function(func_input)

    # Calcular el valor de la integral usando la Regla de Simpson Compuesta
    resultado = simpson_compuesto(f, a, b, n)

    # Mostrar el resultado final
    print(f"\nEl valor de la integral es: {resultado}")
