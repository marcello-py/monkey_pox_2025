def remover_zeros(numeros):
    return str(numeros).replace('0', '')

def soma(x, y):
    soma = x + y
    return int(remover_zeros(soma))


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    print(soma(m, n))