'''
chas = {
1: 'cha_branco',
2: 'cha_verde',
3: 'cha_preto',
4: 'cha_ervas',
}'''


#cha = []

t = int(input())

respostas = list(map(int, input().split()))

contador = 0

for i in respostas:
    if i == t:
        contador += 1
print(contador)