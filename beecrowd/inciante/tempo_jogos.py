from datetime import datetime, timedelta

a, b, c, d = map(int, input().split())

hora_inicial = f"{a:02d}:{b:02d}"
hora_final = f"{c:02d}:{d:02d}"

obj_inicial = datetime.strptime(hora_inicial, "%H:%M") 
obj_final = datetime.strptime(hora_final, "%H:%M")

if obj_final == obj_inicial:
    obj_final += timedelta(days=1)

if obj_final < obj_inicial:
    obj_final += timedelta(days=1)

diferença = obj_final - obj_inicial
diferença_segundos = int(diferença.total_seconds())
horas = diferença_segundos // 3600
minutos = (diferença_segundos % 3600) // 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
