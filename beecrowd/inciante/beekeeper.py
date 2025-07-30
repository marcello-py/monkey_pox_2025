while True:
    try:
        V = float(input())
        D = float(input())
        raio = D / 2
        area = (3.14 * raio**2)
        altura = V / area

        print(f'ALTURA = {altura:.2f}')
        print(f'AREA = {area:.2f}')
    except EOFError:
        break

