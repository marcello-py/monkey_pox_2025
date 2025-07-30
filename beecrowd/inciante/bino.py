contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0

caso_teste = int(input())
n = list(map(int, input().split()))

for i in n:
    if i % 2 == 0:
        contador_2 += 1

    if i % 3 == 0:
        contador_3 += 1

    if i % 4 == 0:
        contador_4 += 1

    if i % 5 == 0:
        contador_5 += 1

print(f'{contador_2} Multiplo(s) de 2')
print(f'{contador_3} Multiplo(s) de 3')
print(f'{contador_4} Multiplo(s) de 4')
print(f'{contador_5} Multiplo(s) de 5')
