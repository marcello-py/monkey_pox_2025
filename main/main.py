# %%
# teste
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_mpox.csv")
df['date'] = pd.to_datetime(df['date'])
df_brazil = df[df['country'] == 'Brazil']
df_cases = df_brazil[['country', 'date', 'classification', 'new_cases', 'cases']]
df_grouped = (
    df.groupby(['date', 'classification'])['new_cases']
    .sum()
    .unstack()
    .fillna(0)
)

plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(15, 6))
plt.grid(True)
plt.xlabel('Data')
plt.ylabel('Novos Casos')
plt.title('Evolução de Novos Casos de Mpox no Brasil')

plt.plot(df_grouped["Suspected"], label="Suspected")
plt.plot(df_grouped["Deaths"], label="Deaths")
plt.plot(df_grouped["Confirmed"], label="Confirmed")
plt.xticks(df_grouped.index[::20], rotation=40)
plt.legend(title='Classificação')
plt.savefig('mpox_2025.jpg', format='jpg')

plt.show()
