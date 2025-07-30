indice = 0
total_moradores = 0
total_consumo = 0
pares = []

while True:
    caso_teste = int(input())
    indice += 1
    if caso_teste == 0:
        break

    for _ in range(caso_teste):
        x, y = map(int, input().split())
        total_moradores += x
        total_consumo += y
        par = f"{x}-{y // x}"
        pares.append(par)

    consumo_medio = total_consumo / total_moradores
    
    print(f'Cidade# {indice}:')
    print(" ".join(pares))
    print(f'Consumo medio: {consumo_medio:.2f} m3.')