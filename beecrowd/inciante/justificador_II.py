lista  = []
lista_formatada = []

while True:
    casos_testes = int(input())
    
    if casos_testes == 0:
        break

    lista_temporaria = []
    for _ in range(casos_testes):
        palavras = input().strip()
        lista_temporaria.append(palavras)
    lista.append(lista_temporaria)

# Limpeza de espaços
for bloco in lista:
    bloco_formatado = []

    for linha in bloco:
        palavras_limpa = ' '.join(linha.strip().split())
        bloco_formatado.append(palavras_limpa) 
    lista_formatada.append(bloco_formatado)

# Justificação à direita e exibição
for i, bloco in enumerate(lista_formatada):
    max_len = max(len(linha) for linha in bloco)
    
    for linha in bloco:
        print(linha.rjust(max_len))
    
    if i < len(lista_formatada) - 1:
        print()
