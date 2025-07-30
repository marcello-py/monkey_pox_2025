tabela = {
    1001 :  1.50,

    1002 : 2.50,

    1003 : 3.50,

    1004 : 4.50,

    1005 : 5.50
}
soma_total = 0
casos = int(input())

for _ in range(casos):
    produto , quantidade_protudo = map(int, input().split())
    total = tabela[produto] * quantidade_protudo
 
    soma_total += total

print(f'{soma_total:.2f}')
