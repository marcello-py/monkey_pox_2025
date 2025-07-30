'''
A entrada contém somente valores inteiros, um por linha, podendo ser positivos ou negativos. 
O primeiro valor da entrada será o valor de X. 
A próxima linha da entrada irá conter Z. 
Se Z não atender a especificação do problema, ele deverá ser lido novamente, tantas vezes quantas forem necessárias.
'''

x = int(input('x: '))

contador = 1
soma = x

while True:
    z = int(input('z: '))
    if z > x:
        while soma <= z:
            contador += 1
            soma += (x + contador - 1)
        break
print(contador)
  
    
