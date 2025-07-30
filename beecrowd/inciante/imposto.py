valor = float(input())

if valor <= 2000.00:
    print('Isento')

elif valor <= 3000.00:
    imposto = (valor - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")


elif valor <= 4500.00:
    imposto = (1000.00 * 0.08) + ((valor - 3000.00) * 0.18)
    print(f"R$ {imposto:.2f}")

else:
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + ((valor - 4500.00) * 0.28)
    print(f"R$ {imposto:.2f}")
