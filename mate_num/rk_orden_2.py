def menu():
    """Menú principal para seleccionar el método"""
    while True:
        print("Elige el tipo de método:")
        print("1. Runge-Kutta (Punto Medio)")
        print("2. Runge-Kutta Modificado (Euler Mejorado)")
        print("3. Salir")
        choice = input("Introduce un valor (1-3): ")
        if choice == "1":
            datos = solicitar_datos()
            punto_medio(datos)
            input("Presiona intro para continuar")
            break
        elif choice == "2":
            datos = solicitar_datos()
            modificado_euler(datos)
            input("Presiona intro para continuar")
            break
        elif choice == "3":
            break
        else:
            print("Elige un valor válido")


def solicitar_datos():
    """
    Solicita al usuario los datos necesarios para resolver la EDO.

    Retorna:
        Una tupla con:
        - La ecuación como string.
        - t0: tiempo inicial.
        - y0: valor inicial.
        - t_end: tiempo final.
        - h: tamaño del paso.
    """
    print("\nMétodo para resolver una EDO")
    func_input = input("Define f(t, y) (ejemplo: t - y): ")
    t0 = float(input("Ingresa el tiempo inicial t0: "))
    y0 = float(input("Ingresa el valor inicial y0: "))
    t_end = float(input("Ingresa el tiempo final t_end: "))
    h = float(input("Ingresa el tamaño del paso h: "))
    return func_input, t0, y0, t_end, h


def runge_kutta_2_midpoint(f, t0, y0, t_end, h, ecuacion):
    """
    Resuelve una ecuación diferencial ordinaria usando el método de Runge-Kutta de orden 2 (punto medio).

    Parámetros:
        f: función que representa la EDO (f(t, y)).
        t0: tiempo inicial.
        y0: valor inicial de la solución en t0.
        t_end: tiempo final.
        h: tamaño del paso.
        ecuacion: ecuación como string para imprimir pasos.

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
            print(f"2. Calcular punto medio: ti + h/2 = {t} + {h}/2 = {t_mid:.5f}")
            print(
                f"3. Calcular wi + h/2 * f(ti,wi) = {y} + {h}/2 * {k1:.7f} = {y_mid:.7f}"
            )
            f_replaced = f_string.replace("t", f"({t_mid:.6f})").replace(
                "y", f"({y_mid:.6f})"
            )
            print(
                f"4. Calcular f(ti + h/2, wi + h/2 * f(ti, wi)) = {f_replaced} = {k2}"
            )
            y_new = y + h * k2
            print(
                f"5. Actualizar wi+1: wi + h * k2 = {y} + {h} * {k2:.7f} = {y_new:.7f}"
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


def punto_medio(datos):
    """
    Método de Runge-Kutta de Orden 2 (Punto Medio) para resolver una EDO.
    """
    func_input, t0, y0, t_end, h = datos

    # Definir la función con `eval`
    def f(t, y):
        return eval(func_input)

    # Resolver la EDO usando Runge-Kutta de orden 2
    t_values, y_values = runge_kutta_2_midpoint(f, t0, y0, t_end, h, func_input)

    # Imprimir los resultados
    print(f"\n{'Iter':>5} {'t':>10} {'y':>15}")
    for i, (t, y) in enumerate(zip(t_values, y_values), start=1):
        print(f"{i:>5} {t:>10.5f} {y:>15.7f}")


def modificado_euler(datos):
    """
    Método de Euler Modificado para resolver una EDO.
    """
    func_input, t0, y0, t_end, h = datos

    # Definir la función con `eval`
    def f(t, y):
        return eval(func_input)

    # Inicializar listas para almacenar los resultados
    t_values = [t0]
    y_values = [y0]

    t = t0
    y = y0

    while t < t_end:
        # Asegurarse de que el último paso no exceda t_end
        if t + h > t_end:
            h = t_end - t

        # Calcular predictor (Euler hacia adelante)
        k1 = f(t, y)
        y_predictor = y + h * k1

        # Calcular corrector (promedio entre pendiente inicial y pendiente del predictor)
        k2 = f(t + h, y_predictor)
        y_corrector = y + (h / 2) * (k1 + k2)

        # Mostrar paso a paso para la primera iteración
        if t == t0:
            print("\nPrimera Iteración (Paso a Paso):")
            f_string = str(func_input)
            f_replaced_k1 = f_string.replace("y", f"({y:.6f})").replace(
                "t", f"({t:.6f})"
            )
            print(
                f"1. Calcular f(ti, wi) = f({t:.5f}, {y:.7f}) = {f_replaced_k1} = {k1:.7f}"
            )
            print(
                f"2. Calcular predictor: wi + h * f(ti, wi) = {y:.7f} + {h:.2f} * {k1:.7f} = {y_predictor:.7f}"
            )
            t_next = t + h
            f_replaced_k2 = f_string.replace("t", f"({t_next:.6f})").replace(
                "y", f"({y_predictor:.6f})"
            )
            print(
                f"3. Calcular f(ti + h, wi_predictor) = f({t_next:.5f}, {y_predictor:.7f}) = {f_replaced_k2} = {k2:.7f}"
            )
            print(
                f"4. Calcular corrector: wi + h/2 * (k1 + k2) = {y:.7f} + {h}/2 * ({k1:.7f} + {k2:.7f}) = {y_corrector:.7f}"
            )
            print("")

        # Actualizar valores
        y = y_corrector
        t = t + h

        # Almacenar resultados
        t_values.append(t)
        y_values.append(y)

    # Imprimir los resultados
    print(f"\n{'Iter':>5} {'t':>10} {'y':>15}")
    for i, (t, y) in enumerate(zip(t_values, y_values), start=1):
        print(f"{i:>5} {t:>10.5f} {y:>15.7f}")
