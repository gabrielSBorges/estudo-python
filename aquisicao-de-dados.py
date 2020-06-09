import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Funções
def montaPlanilhaDiretores(planilha) :
    indicacoes_por_direcao = planilha[planilha.category.str.contains('DIRECTING')]

    vencedores = indicacoes_por_direcao[indicacoes_por_direcao.winner]

    planilha_diretores = vencedores.groupby(['name']).size().reset_index(name = 'oscares')
    planilha_diretores = planilha_diretores.sort_values(by = ['oscares'], ascending = False).head(5)

    return planilha_diretores

# 1- Pega os dados da planilha:
planilha = pd.read_csv('./dados/the_oscar_award.csv')
planilha = montaPlanilhaDiretores(planilha)

# 2 - Filtra os dados que serão utilizados:
diretores = []
oscares_qtd = []

for diretor in planilha['name'] :
    diretores.append(diretor)

for oscar_qtd in planilha['oscares'] :
    oscares_qtd.append(oscar_qtd)

# 3 - Cria o gráfico:
fig, ax = plt.subplots()

plt.ylabel("Oscares")
plt.title("Diretores com o maior número de Oscares por direção (Desde 1928)")

ypos = np.arange(len(oscares_qtd))
plt.bar(ypos, oscares_qtd, align = 'center', alpha = 0.5)
plt.xticks(ypos, diretores)

max = int(len(oscares_qtd))
yint=range(0, max)
plt.yticks(yint)

# 3 - Mostra/salva o gráfico:
fig.set_size_inches(12, 6)
fig.savefig("./dados/diretor_mais_premiado.png", dpi=100)
plt.show()