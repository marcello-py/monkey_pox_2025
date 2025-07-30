caso_teste = int(input())

def fatiamento(palavra):
    fatiar = palavra[::-1]
    return fatiar

def deslocar(palavra):
    nova_palavra = ''
    for letra in palavra:
        if letra.isalpha():
            nova_letra = chr(ord(letra) + 3)
            nova_palavra += nova_letra
        else:
            nova_palavra += letra
    return nova_palavra

def deslocar_menor(palavra):
    nova_palavra = ''
    meio = len(palavra) // 2
    for i, letra in enumerate(palavra):
        if i >= meio:        
            nova_letra = chr(ord(letra) - 1)
        else:
            nova_letra = letra
        nova_palavra += nova_letra                  
    return nova_palavra

for _ in range(caso_teste):
    m = input()
    etapa1 = deslocar(m)
    etapa2 = fatiamento(etapa1)
    etapa3 = deslocar_menor(etapa2)
    print(etapa3)