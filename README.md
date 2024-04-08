<div align='center'>
<figure> <img src="https://i.postimg.cc/ZYLWq9xH/error-418.png" alt="" width="300" height="auto"/></br>
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
### 3. Escriba una función recursiva para calcular la operación de la potencia.
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

### 5. Crear cuenta en [stackoverflow](https://stackoverflow.com/) y adjuntar imagen en el repo
![image](https://github.com/JavierGONL/repo_reto_9/assets/159032556/761b58df-c476-451d-b269-23d38161b4f5)
### 6. Cosas de adultos....ir a [linkedin](https://www.linkedin.com/) y crear perfil....NO IMPORTA que estén iniciando, si tienen tiempo para redes poco útiles como fb, insta, o tiktok tienen tiempo para crear un perfil mamalón. Dejar enlace en el repo.
enlace a mi [linkedin](https://www.linkedin.com/in/kevin-javier-gonzalez-l-41854527a/)
