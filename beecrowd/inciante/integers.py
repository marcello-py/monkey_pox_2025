valores = list(map(int, input().split()))

A = valores[0]

for num in valores[1:]:
    if num > 0:
        N = num
        break

soma = sum(A + i for i in range(N))
print(soma)