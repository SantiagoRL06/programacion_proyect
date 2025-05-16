# ------------------------------
# PROYECTO FINAL - CONTROL DE CONSUMO DE AGUA
# ------------------------------

# Lista donde se almacenan los registros diarios
consumos = []

# Función para mostrar el menú principal
def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar consumo")
    print("2. Ver estadísticas")
    print("3. Editar un dato")
    print("4. Eliminar un dato")
    print("5. Ver historial")
    print("6. Salir")

# Función para registrar un nuevo consumo
def registrar_consumo():
    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
    try:
        litros = float(input("Ingrese los litros consumidos: "))
        consumos.append([fecha, litros])
        print("✅ Registro guardado con éxito.")
    except ValueError:
        print("⚠ Error: debe ingresar un número válido.")

# Función para mostrar estadísticas básicas
def mostrar_estadisticas():
    if not consumos:
        print("⚠ No hay datos registrados.")
        return

    total = sum([dato[1] for dato in consumos])
    promedio = total / len(consumos)
    maximo = max(consumos, key=lambda x: x[1])
    minimo = min(consumos, key=lambda x: x[1])

    print("\n--- ESTADÍSTICAS ---")
    print(f"Total de consumo: {total:.2f} litros")
    print(f"Promedio diario: {promedio:.2f} litros")
    print(f"Día de mayor consumo: {maximo[0]} con {maximo[1]} litros")
    print(f"Día de menor consumo: {minimo[0]} con {minimo[1]} litros")

# Función para editar un consumo existente
def editar_dato():
    fecha = input("Ingrese la fecha del registro a editar: ")
    for dato in consumos:
        if dato[0] == fecha:
            try:
                nuevo = float(input(f"Ingrese el nuevo valor para {fecha}: "))
                dato[1] = nuevo
                print("✅ Registro actualizado.")
                return
            except ValueError:
                print("⚠ Error: debe ingresar un número válido.")
                return
    print("⚠ Registro no encontrado.")



