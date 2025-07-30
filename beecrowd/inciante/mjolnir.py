c = int(input()).strip()

for _ in range(c):
    nome, forca = input().split()
    forca = int(forca)
    resultado = 'Y ' if nome == 'Thor' else 'N'
    print(resultado)
        