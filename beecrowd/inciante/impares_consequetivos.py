x, y = map(int, input().split())
maior = max(x, y)
menor = min(x, y)

soma = 0
for i in range(menor + 1, maior):
    if i % 2 == 1:
       soma += i

print(soma)
