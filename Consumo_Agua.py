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

