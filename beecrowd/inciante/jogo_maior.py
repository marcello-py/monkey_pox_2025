while True:
    caso_teste = int(input())
    if caso_teste == 0:
        break


    contador_a = 0
    contador_b = 0

    for _ in range(caso_teste):
        a, b = map(int, input().split())

        if a > b:
            contador_a += 1

        if b > a:
            contador_b += 1


    print(contador_a, contador_b)
