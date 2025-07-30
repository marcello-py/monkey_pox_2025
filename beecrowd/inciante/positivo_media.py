positivos = 0
soma = 0

for _ in range(6):
    a = float(input())
    if a > 0:
        positivos += 1
        soma += a
        media = soma / positivos

print(f"{positivos} valores positivos")
print(f"{media:.1f}")