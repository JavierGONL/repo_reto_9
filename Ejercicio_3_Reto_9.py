def potencia_recursiva(base, exponente):
    # si el exponente es 0 el resultado es 1
    if exponente == 0:
        return 1
    else:
        # se multiplica la base por la funcion potencia_recursiva con la misma base y exponente - 1
        return base * potencia_recursiva(base, exponente - 1)
if __name__ == '__main__':
    # se pide al usuario la base y el exponente y se imprime el resultado de la potencia
    base = int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))
    print(f"el resultado de la potencia utilizando la funcion recursiva es {potencia_recursiva(base, exponente)}")