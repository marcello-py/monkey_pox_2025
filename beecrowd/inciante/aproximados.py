import math

n = int(input())

ln_n = math.log(n)

p = n / ln_n
m = n / (ln_n - 1)

print(f"{p:.1f} {m:.1f}")
