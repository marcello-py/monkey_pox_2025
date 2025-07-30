t = int(input()) 

vector = []
if 2 <= t <= 50:
    for n in range(1000):
        vector.append(n % t)
    for i in range(len(vector)):
        print(f'N[{i}] = {vector[i]}')
