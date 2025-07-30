def calcular_mediana(a, b, c):
    return sorted([a, b, c])[1]

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    candidatos = []

    
    c1 = 2 * a - b
    if calcular_mediana(a, b, c1) == (a + b + c1) // 3:
        candidatos.append(c1)

    
    if (a + b) % 2 == 0:
        c2 = (a + b) // 2
        if calcular_mediana(a, b, c2) == (a + b + c2) // 3:
            candidatos.append(c2)

    
    c3 = 2 * b - a
    if calcular_mediana(a, b, c3) == (a + b + c3) // 3:
        candidatos.append(c3)

    print(min(candidatos))
