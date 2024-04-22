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