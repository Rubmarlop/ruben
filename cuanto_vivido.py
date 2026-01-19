






from datetime import date, datetime

def calcular_dias_vividos(fecha_nacimiento):
    hoy = date.today()
    diferencia = hoy - fecha_nacimiento
    return diferencia.days

# resultado
nacimiento_str = input("Introduce fecha de nacimiento (AAAA-MM-DD): ")
nacimiento = datetime.strptime(nacimiento_str, "%Y-%m-%d").date()
print(f"Has vivido {calcular_dias_vividos(nacimiento)} días.")