n = int(input())
vetor = [n]
if n <= 50:
    for i in range(1, 10):
       vetor.append(vetor[i - 1] * 2)

for i in range(10):
    print(f'N[{i}] = {vetor[i]}')
