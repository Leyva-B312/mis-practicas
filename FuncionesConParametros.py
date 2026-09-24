#Ejemplo 1: Cálculo matemático sencillo
#Recibe un número como parámetro y calcula su valor final aplicándole un porcentaje de impuesto.
def calcular_precio_total(precio_base):
    impuesto = precio_base * 0.16
    total = precio_base + impuesto
    print(f"El precio base es ${precio_base} y con impuestos es ${total}")

# Llamamos a la función pasándole diferentes valores:
calcular_precio_total(100)
calcular_precio_total(250)
print("//////////////////////////////////////")
# Ejemplo 2: Múltiples parámetros y retorno de datos
#Recibe dos parámetros (nombre y edad) y utiliza la instrucción return para devolver el resultado del texto procesado en lugar de solo imprimirlo.
def crear_saludo(nombre, edad):
    return f"Hola {nombre}, tienes {edad} años."

# Guardamos el resultado devuelto en una variable:
mensaje = crear_saludo("Carlos", 28)
print(mensaje)
print("//////////////////////////////////////")
#Ejemplo 3: Parámetros con valores por defecto (opcionales)
#Puedes asignar un valor predeterminado a un parámetro por si el usuario olvida o prefiere no enviarlo al llamar a la función
def enviar_mensaje(texto, destinatario="Usuario de la plataforma"):
    print(f"Enviando a {destinatario}: {texto}")

# Si pasas ambos datos:
enviar_mensaje("Tu paquete ha llegado", "Ana")

# Si solo pasas el primer parámetro, usa el valor por defecto:
enviar_mensaje("Bienvenido al sistema")