import time
def funcion_recursiva_fibonacci(Termino = "")->float:
    # funcion que calcula la serie de fibonacci de manera recursiva 
    # uso esta debido a que esta empieza a ser lenta mas rapido debido a la misma recursividad
    # la recursividad esta mal optimizada en largas series de calculos segun un post de stackoverflow
    if Termino <= 1:
        return Termino
    else:
        return funcion_recursiva_fibonacci(Termino - 1) + funcion_recursiva_fibonacci(Termino - 2)
def fibonacci_tiempo()->float:
    # calcula el tiempo que pasa entre cada termino de la serie de fibonacci
    bandera_10 = False
    Termino = 1
    while True:
        start_time = time.time() 
        funcion_recursiva_fibonacci(Termino) # se llama a la funcion que calcula la serie de fibonacci
        end_time = time.time() 
        timer = end_time - start_time
        Termino += 1
        print(f"El tiempo entre el termino {Termino - 1} y el {Termino} de la serie de fibonacci es: {timer} ")
        # la condicion de parada del while si el tiempo es mayor a 5 segundos la bandera se activa y se detiene el bucle
        if timer >= 5 and bandera_10 == False:
            bandera_10 = True
            break
if __name__ == "__main__":
    # se llama a la funcion fibonacci_tiempo y se imprime el resultado
    print("inicio el programa")
    fibonacci_tiempo() # se llama a la funcion que calcula el tiempo entre cada termino de la serie de fibonacci
    """ conclusiones : en el termino 17 y 18 de la serie de fibonacci el tiempo 
    de ejecucion deja de se 0.0 y apartir de la serie 33 y 34 el timer es de 1 segundo
        desde ahi el aumento entre termino y termino empieza a ser significativo"""