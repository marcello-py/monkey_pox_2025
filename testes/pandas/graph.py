# %%
import matplotlib.pyplot as plt


# %%
x = [
    "Maçã", "Banana", "Laranja", "Uva", "Manga",
    "Abacaxi", "Melancia", "Morango", "Pera", "Pêssego",
    "Cereja", "Kiwi", "Goiaba", "Ameixa", "Maracujá",
    "Framboesa", "Amora", "Caju", "Tangerina", "Mamão"
]
y = [
    12, 12, 41, 22, 45, 
    5, 7, 24, 8, 14, 
    87,2, 72, 12, 76, 
    14, 51, 21, 52, 22
]
cores = ['red', 'blue', 'green', 'orange', 'purple']
plt.figure(figsize=(10, 4))
plt.scatter(x, y, c='red')
plt.legend()
plt.xlabel('Frutas')
plt.ylabel('Quantidade')
plt.title('Quadro de frutas')
plt.grid()
plt.xticks(rotation=45)