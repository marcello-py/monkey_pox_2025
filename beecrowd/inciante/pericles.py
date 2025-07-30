x, y = map(int, input().split())

nova_aba = x

for _ in range(y):
    acao = input()

    if acao == 'fechou':
        nova_aba += 1
    elif acao == 'clicou':
        nova_aba -= 1

print(nova_aba)