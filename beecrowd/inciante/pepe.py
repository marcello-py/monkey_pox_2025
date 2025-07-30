import datetime

caso_teste = int(input())

for _ in range(caso_teste):
    h, m, o = list(input().split())

    horario = datetime.time(int(h), int(m))

    horario_formatado = horario.strftime("%H:%M")

    if o == '1':
        print(f'{horario_formatado} - A porta abriu!')
    elif o == '0':
        print(f'{horario_formatado} - A porta fechou!')
