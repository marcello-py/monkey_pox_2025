import math

while True:
    acm = input().strip()

    if acm == '0':
        break

    resultado = 0
    n = len(acm)

    for i in range(n):
        digito = int(acm[i])
        posicao = n - i
        resultado += digito * math.factorial(posicao)
        
    print(resultado)