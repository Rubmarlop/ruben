






from datetime import datetime, timedelta

def calcular_fecha_8000_dias(fecha_nacimiento):
    intervalo = timedelta(days=8000)
    fecha_objetivo = fecha_nacimiento + intervalo
    return fecha_objetivo

# resultado
nacimiento_str = input("Introduce fecha de nacimiento (AAAA-MM-DD): ")
nacimiento = datetime.strptime(nacimiento_str, "%Y-%m-%d").date()
print(f"Cumplirás 8.000 días el: {calcular_fecha_8000_dias(nacimiento)}")