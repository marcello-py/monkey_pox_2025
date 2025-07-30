salario = float(input())

if  0 <= salario <= 400:
    percentual = 15

elif 400.01 <= salario <= 800:
    percentual = 12

elif 800 <= salario <= 1200:
    percentual = 10

elif 1200 <= salario <= 2000:
    percentual = 7

else:
    percentual = 4

reajuste = percentual / 100 * salario

print(f'Novo salario: {reajuste + salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percentual} %')