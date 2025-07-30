# %%
def cargo(funcao):
    return {
    "Sobrenome": "Nunes",
    "Nome": "Marcelo",
    "Filhos": False,
    "Formacao": ["Sistema de Informação", "Atendente"],
}.get(funcao, 'não encontrado')

funcao = input('Quado cargo?')
cargo(funcao)

# %%

