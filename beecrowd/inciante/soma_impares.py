num_casos = int(input())

for _ in range(num_casos):
    x, y = map(int, input().split())
    if x % 2 == 0:
        x += 1 #incrementador 
    soma_impares = 0

    for _ in range(y):
        soma_impares += x
        x += 2
    print(soma_impares)