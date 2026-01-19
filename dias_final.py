





from datetime import date, datetime, timedelta

# --- FUNCIÓN A ---
def calcular_dias_vividos(fecha_nacimiento):
    hoy = date.today()
    diferencia = hoy - fecha_nacimiento
    return diferencia.days

# --- FUNCIÓN B ---
def calcular_fecha_8000_dias(fecha_nacimiento):
    return fecha_nacimiento + timedelta(days=8000)

# --- PROGRAMA C ---
# 1. Pedir datos
entrada = input("Introduce tu fecha de nacimiento (AAAA-MM-DD): ")
fecha_nac = datetime.strptime(entrada, "%Y-%m-%d").date()

# 2. Usar las funciones
total_dias = calcular_dias_vividos(fecha_nac)
fecha_8000 = calcular_fecha_8000_dias(fecha_nac)

# 3. Mostrar resultados
print(f"Has vivido {total_dias} días.")
print(f"Cumplirás 8.000 días el: {fecha_8000}")