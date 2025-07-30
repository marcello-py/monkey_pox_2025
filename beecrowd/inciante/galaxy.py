while True:
    n = int(input())
    if n == 0:
        break
    
    mais_antigo = float('inf')
    planeta_mais_antigo = ""
    for _ in range(n):
        planeta, a, t = input('').split()
        a, t = map(int(a, t))
        envio = a - t
        if envio < mais_antigo:
            mais_antigo = envio
            planeta_mais_antigo = planeta

    print(planeta_mais_antigo)