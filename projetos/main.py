# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
df = pd.read_csv("data_mpox.csv")
# %%
df['date'] = pd.to_datetime(df['date'])

# %% Filtrando por Brasil
df_brazil = df[df['country'] == 'Brazil']

# %% Agrupando dados e tipo de classificação
df_cases = df_brazil[['country', 'date', 'classification', 'new_cases', 'cases']]
df_grouped = (df.groupby(['date', 'classification'])['new_cases']
                        .sum()
                        .unstack()
                        .fillna(0))
# %% Gráfico

plt.figure(figsize=(15, 6))
plt.grid(True)
plt.title("Evolução de Novos Casos de Mpox no Brasil")
plt.xlabel("Data")
plt.ylabel("Número de Casos")
plt.plot(df_grouped["Suspected"], label="Suspected")
plt.plot(df_grouped["Deaths"], label="Deaths")
plt.plot(df_grouped["Confirmed"], label="Confirmed")
plt.xticks(df_grouped.index[::10], rotation=40) #intervalo de dias apresentado
plt.style.use('seaborn-v0_8-whitegrid')
plt.legend(title = 'Classificação')
plt.savefig('mpox_2025.jpg', format='jpg')