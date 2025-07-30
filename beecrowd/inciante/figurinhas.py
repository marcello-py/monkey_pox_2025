def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

casos = int(input())

for _ in range(casos):
    f, m = map(int, input().split())
    print(mdc(f, m))
