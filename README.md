<div align='center'>
<figure> <img src="https://res.cloudinary.com/dm0p2ljin/image/upload/v1714416338/error-418_dtb3ak.png" alt="" width="300" height="auto"/></br>
<figcaption><b></b></figcaption></figure>
</div>

# Reto 9
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_9 en slack.

### 1. De los retos anteriores selecione 3 funciones y escribalas en forma de lambdas.
```python
# primera funcion
def rango_de_error(numero_real,aproximacion):
    # funcion normal
    aproximacion = int
    numero_real = int
    error_relativo = (numero_real - aproximacion) / numero_real
    porcentaje_error = abs(error_relativo) * 100
    return porcentaje_error

# version lambda de la funcion rango_de_error
rango_de_error_lambda = lambda numero_real,aproximacion : round(abs((numero_real - aproximacion)/numero_real)*100,5)

# segunda funcion
def cuadrados(numero : int) -> int:
    # funcion normal
    return numero ** 2

# version lamda del a funcion cuadrados
cuadrados_lambda = lambda numero : numero**2

# tercera funcion

def calcular_volumen_esfera(radio:float, PI = 3.14159)->float:
    # funcion normal
    return (4/3) * PI * radio ** 3

# version lambda de la funcion calcular_volumen_esfera
calcular_volumen_esfera_lambda = lambda radio , PI = 3.14159: (4/3) * PI * radio**3
```
### 2. De los retos anteriores selecione 3 funciones y escribalas con argumentos no definidos (*args).
```python
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
```
### 3. Escriba una función recursiva para calcular la operación de la potencia.
```python
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
```

### 4. Utilice la siguiente plantilla de code para contar el tiempo:
```python
import time

start_time = time.time()
# instrucciones sobre las cuales se quiere medir tiempo de ejecución
end_time = time.time()

timer = end_time - start_time
print(timer)
```

Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
**Importante:** Revisar este [hilo](https://stackoverflow.com/questions/8220801/how-to-use-timeit-module).
```python
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
```

### 5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo
![image](https://github.com/JavierGONL/repo_reto_9/assets/159032556/761b58df-c476-451d-b269-23d38161b4f5)
### 6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
enlace a mi [linkedin](https://www.linkedin.com/in/kevin-javier-gonzalez-l-41854527a/)
