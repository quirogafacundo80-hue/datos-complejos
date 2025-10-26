# ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# ejercicio 2

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# ejercicio 3
precios_frutas = {'Banana': 1330, 'Ananá': 2500, 'Melón': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

frutas = list(precios_frutas.keys())
print(frutas)

# ejercicio 4
contactos = {}

for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número de teléfono: ")
    contactos[nombre] = numero

consulta = input("Ingresá el nombre a consultar: ")

if consulta in contactos:
    print("Número:", contactos[consulta])
else:
    print("No existe ese contacto.")

# ejercicio 5

frase = input("Ingresá una frase: ").lower().split()

palabras_unicas = set(frase)
recuento = {}

for palabra in frase:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# ejercicio 6

alumnos = {}

for i in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(nombre, "promedio:", promedio)

# ejercicio 7

parcial1 = {1, 2, 3, 4, 5}  # ejemplo de IDs de estudiantes
parcial2 = {4, 5, 6, 7}

aprob_both = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", aprob_both)
print("Aprobaron solo uno de los parciales:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

# ejercicio 8

stock = {"Manzana": 10, "Banana": 5, "Leche": 20}

producto = input("Ingresá el producto: ")

if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = int(input("Ingresá unidades a agregar: "))
    stock[producto] += agregar
else:
    unidades = int(input("Producto nuevo. Ingresá cantidad: "))
    stock[producto] = unidades

print("Stock actualizado:", stock)

# ejercicio 9

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (HH:MM): ")

evento = agenda.get((dia, hora))
if evento:
    print("Evento:", evento)
else:
    print("No hay eventos en ese horario.")
# ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia"}

invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario invertido:", invertido)
