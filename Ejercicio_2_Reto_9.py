def suma_de_lista(*args)->float:
    # utilizando el *args para meter una lista de numeros y sumarlos
    suma_lista = 0
    for n in args:
        suma_lista += n
    return suma_lista 
def elevar_un_numero_al_cuadrado(*args)->float:
    # utilizando el *args para meter una lista de numeros y elevarlos al cuadrado
    for n in args:
        print(f"El numero {n} elevado al cuadrado es: {n**2}")
def multilicar_nuemeros(*args)->float:
    # utilizando el *args para meter una lista de numeros y multiplicarlos
    multiplicacion_lista = 1
    for n in args:
        multiplicacion_lista *= n
    return multiplicacion_lista