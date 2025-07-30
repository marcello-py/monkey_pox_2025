n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    rafael = (x * 3) ** 2 + y ** 2
    beto = 2 * (x ** 2) + (5 *y) ** 2
    carlos = -100 * x + y ** 3

    if rafael > beto and rafael > carlos:
        print('Rafael ganhou')
        
    elif beto > rafael and beto > carlos:
        print('Beto ganhou')
        
    else:
#    elif beto and rafael < carlos:
        print('Carlos ganhou')