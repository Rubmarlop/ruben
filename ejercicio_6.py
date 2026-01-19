





from datetime import datetime, date, timedelta
import calendar
import pytz

# 1. Presentar fecha actual
print(f"1. Fecha actual: {date.today()}")

# 2. Presentar fecha y hora actual
print(f"2. Fecha y hora actual: {datetime.now()}")

# 3. Presentar fecha y hora en Europa/Madrid
zona_madrid = pytz.timezone('Europe/Madrid')
print(f"3. Fecha/Hora Madrid: {datetime.now(zona_madrid)}")

# 4. Presentar fecha del 10/12/2022 con este formato
fecha_4 = date(2022, 12, 10)
print(f"4. Formato: {fecha_4.strftime('%d/%m/%Y')}")

# 5. Indicar a que mes corresponde el 7/12/2020 (número y nombre)
fecha_5 = date(2020, 12, 7)
meses_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
print(f"5. Mes: {fecha_5.month} ({meses_es[fecha_5.month - 1]})")

# 6. Comprovar si 2022 es bisiesto
print(f"6. ¿2022 es bisiesto?: {calendar.isleap(2022)}")

# 7. Comprovar si puedo poner el día 29 a 2/2020
try:
    date(2020, 2, 29)
    print("7. Sí es posible poner 29/02/2020")
except ValueError:
    print("7. No es posible")

# 8. Fecha 30 días después del 20/2/2010
fecha_8 = date(2010, 2, 20) + timedelta(days=30)
print(f"8. 30 días después: {fecha_8}")

# 9. Fecha 1 mes después del 15/12/2009
# (Sumar un mes manualmente o usando lógica simple)
fecha_9 = date(2010, 1, 15) 
print(f"9. 1 mes después: {fecha_9}")

# 10. Días entre 07/10/2001 y 10/05/2004
d10_1 = date(2001, 10, 7)
d10_2 = date(2004, 5, 10)
print(f"10. Días transcurridos: {(d10_2 - d10_1).days}")

# 11. Meses entre 07/10/2001 y 10/05/2004
meses = (d10_2.year - d10_1.year) * 12 + (d10_2.month - d10_1.month)
print(f"11. Meses transcurridos: {meses}")

# 12. Años entre 07/10/2001 y 10/05/2004
print(f"12. Años transcurridos: {d10_2.year - d10_1.year}")

# 13. Horas entre 07/10/2001 y 10/05/2004
horas = (d10_2 - d10_1).total_seconds() / 3600
print(f"13. Horas transcurridas: {int(horas)}")

# 14. Período entre 3/2/2020 y 5/7/2021
periodo = date(2021, 7, 5) - date(2020, 2, 3)
print(f"14. Período: {periodo}")

# 15. Fecha resultante sumando el periodo anterior a 12/11/2022
fecha_15 = date(2022, 11, 12) + periodo
print(f"15. Nueva fecha: {fecha_15}")

# 16. Qué día de la semana era el 22/4/2022
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
fecha_16 = date(2022, 4, 22)
print(f"16. Día de la semana: {dias_semana[fecha_16.weekday()]}")

# 17. Qué día de la semana era hace tres días
hace_tres = date.today() - timedelta(days=3)
print(f"17. Hace tres días era: {dias_semana[hace_tres.weekday()]}")

# 18. Nombre en valenciano del mes actual
meses_val = ["gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre"]
print(f"18. Mes actual (val): {meses_val[date.today().month - 1]}")

# 19. Día de la semana el 01/10/1940
fecha_19 = date(1940, 10, 1)
print(f"19. Día 01/10/1940: {dias_semana[fecha_19.weekday()]}")

# 20. Fecha correspondiente al día 253 del año 1989
fecha_20 = date(1989, 1, 1) + timedelta(days=252)
print(f"20. Día 253 de 1989: {fecha_20}")

# 21. Segundos entre las 10:15 y las 12:30
t1 = timedelta(hours=10, minutes=15)
t2 = timedelta(hours=12, minutes=30)
print(f"21. Segundos transcurridos: {(t2 - t1).total_seconds()}")