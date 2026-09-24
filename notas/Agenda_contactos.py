# Tarea practica: Guardad datos;nombre y numero telefonico
# Estudiante: Joel Alexander Zavala Pachay
# Problema: tengo los numeros de mis companeros y familiares regados en varios lados, asi que hice una agenda sencilla para guardarlos.
# Uso un diccionario donde la clave es el nombre y el valor es el telefono.

# Diccionario donde se guardan los contactos
# Empieza vacio, los contactos se ingresan por consola
agenda = {}

def agregar_contacto():
    nombre = input("Nombre del contacto: ").strip().capitalize()
    telefono = input("Numero de telefono: ").strip()

    if nombre == "" or telefono == "":
        print("No puedes dejar campos vacios.")
        return

    # el telefono solo debe tener numeros
    if not telefono.isdigit():
        print("El telefono solo debe tener numeros.")
        return

    # si el nombre ya existe solo se actualiza el numero
    if nombre in agenda:
        print(nombre, "ya estaba en la agenda, se actualizo su numero.")
    else:
        print("Contacto guardado.")
    agenda[nombre] = telefono


def mostrar_contactos():
    if len(agenda) == 0:
        print("La agenda esta vacia.")
        return

    print("\n--- Mis contactos ---")
    # recorro el diccionario y muestro cada contacto
    numero = 1
    for nombre, telefono in agenda.items():
        print(f"{numero}. {nombre}: {telefono}")
        numero += 1
    print("Total de contactos:", len(agenda))


def buscar_contacto():
    nombre = input("Nombre a buscar: ").strip().capitalize()
    if nombre in agenda:
        print("El numero de", nombre, "es", agenda[nombre])
    else:
        print("No encontre a", nombre, "en la agenda.")


def eliminar_contacto():
    nombre = input("Nombre a eliminar: ").strip().capitalize()
    if nombre in agenda:
        del agenda[nombre]
        print(nombre, "fue eliminado.")
    else:
        print("Ese contacto no existe.")


# ---------- Menu principal ----------

opcion = ""
while opcion != "5":
    print("\n===== AGENDA DE CONTACTOS =====")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Elige una opcion: ").strip()

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contactos()
    elif opcion == "3":
        buscar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Saliendo de la agenda. Hasta luego!")
    else:
        print("Opcion no valida, intenta otra vez.")