casos_testes = int(input())

for _ in range(casos_testes):
    x = int(input())  
    if x == 0:
        print("NULL")  
    elif x < 0:
        if x % 2 == 1:
            print("ODD NEGATIVE")
        else:
            print("EVEN NEGATIVE")
    else:
        if x % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
