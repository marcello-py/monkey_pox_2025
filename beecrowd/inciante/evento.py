from datetime import datetime

dia_inicio = int(input().split()[1])
hora_inicio = list(map(int, input().split(" : ")))

dia_fim = int(input().split()[1])
hora_fim = list(map(int, input().split(" : ")))

inicio = datetime(2020, 1, dia_inicio, *hora_inicio)
fim = datetime(2020, 1, dia_fim, *hora_fim)

diferenca = fim - inicio
diferenca_segundos = int(diferenca.total_seconds())

dias = diferenca_segundos // 86400
diferenca_segundos %= 86400

horas = diferenca_segundos // 3600
diferenca_segundos %= 3600

minutos = diferenca_segundos // 60
segundos = diferenca_segundos % 60


print(f'{dias} dias(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')