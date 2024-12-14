def runge_kutta_2_midpoint(f, t0, y0, t_end, h, ecuacion):
    """
    Resuelve una ecuación diferencial ordinaria usando el método de Runge-Kutta de orden 2 (punto medio).

    Parámetros:
        f: función que representa la EDO (f(t, y)).
        t0: tiempo inicial.
        y0: valor inicial de la solución en t0.
        t_end: tiempo final.
        h: tamaño del paso.

    Retorna:
        t_values: lista de los valores de t.
        y_values: lista de las aproximaciones de y.
    """
    # Inicializar listas para almacenar los resultados
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        # Asegurarse de que el último paso no exceda t_end
        if t + h > t_end:
            h = t_end - t

        # Paso 1: Calcular k1
        k1 = f(t, y)

        # Paso 2: Calcular k2 usando el punto medio
        k2 = f(t + h / 2, y + h / 2 * k1)

        # Imprimir paso a paso para la primera iteración
        if t == t0:
            f_string = str(ecuacion)
            f_replaced = f_string.replace("y", f"({y:.6f})").replace("t", f"({t:.6f})")
            print("\nPrimera Iteración (Paso a Paso):")
            print(
                f"1. Calcular f(ti,wi) =  f({t:.5f}, {y:.7f}) = {f_replaced} = {k1:.7f}"
            )
            t_mid = t + h / 2
            y_mid = y + (h / 2) * k1
            print(f"2. Calcular punto medio: t + h/2 = {t} + {h}/2 = {t_mid:.5f}")
            print(f"   wi + h/2 * f(ti,wi) = {y} + {h}/2 * {k1:.7f} = {y_mid:.7f}")
            print(
                f"3. Calcular f(ti + h/2, wi + h/2 * f(ti, wi)) = f({t_mid:.5f}, {y_mid:.7f})"
            )
            print(f"   f(ti + h/2, wi + h/2 * f(ti, wi)) = {k2:.7f}")
            y_new = y + h * k2
            print(
                f"4. Actualizar wi+1: wi + h * k2 = {y} + {h} * {k2:.7f} = {y_new:.7f}"
            )
            print("")

        # Actualizar y usando k2
        y = y + h * k2

        # Actualizar t
        t = t + h

        # Almacenar resultados
        t_values.append(t)
        y_values.append(y)

    return t_values, y_values


# Función principal que solicita los datos al usuario
def main():
    print("Método de Runge-Kutta de Orden 2 (Punto Medio) para resolver una EDO")

    # Solicitar al usuario la definición de la función f(t, y)
    print("\nDefine la función f(t, y):")
    print("Por ejemplo, si f(t, y) = t - y, escribe: t - y")
    ##### TODO: eliminar comentario func_input = input("f(t, y) = ")
    func_input = "y - t**2 + 1"

    # Definir la función con `eval`
    def f(t, y):
        return eval(func_input)

    # Solicitar al usuario los parámetros
    ##### TODO: eliminar comentario t0 = float(input("Ingresa el tiempo inicial t0: "))
    ##### TODO: eliminar comentario y0 = float(input("Ingresa el valor inicial y0: "))
    ##### TODO: eliminar comentario t_end = float(input("Ingresa el tiempo final t_end: "))
    ##### TODO: eliminar comentario h = float(input("Ingresa el tamaño del paso h: "))

    t0 = 0
    t_end = 2
    y0 = 0.5
    h = 0.2
    # Resolver la EDO usando Runge-Kutta de orden 2
    t_values, y_values = runge_kutta_2_midpoint(f, t0, y0, t_end, h, func_input)

    # Imprimir los resultados
    print(f"\n{'Iter':>5} {'t':>10} {'y':>15}")
    for i, (t, y) in enumerate(zip(t_values, y_values), start=1):
        print(f"{i:>5} {t:>10.5f} {y:>15.7f}")
    input("Presiona intro para continuar")


# Llamar a la función principal
if __name__ == "__main__":
    main()
