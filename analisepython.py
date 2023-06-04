import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
comprimento = float(input())
dados = pd.read_csv('C:/Users/sonic/OneDrive/Documentos/matlabs/Teste1/log/Amostra1.csv')
colunas = ['Duracao alto', 'Duracao baixo']
dados[colunas] = dados[colunas].replace(',', '.', regex = True)
dados[colunas] = dados[colunas].astype(float)
tempo_de_volta = dados['Duracao baixo']
Diferença_tempo_de_volta = tempo_de_volta.diff()
dados['Diferença do tempo de volta(ms)'] = Diferença_tempo_de_volta
dados.loc[0, 'Diferença do tempo de volta(ms)'] = '-'
dados.rename(columns={'Duracao baixo': 'Tempo de volta (ms)'}, inplace=True)
velocidade_instantânea = 3600*comprimento/dados['Duracao alto'] 
dados['Velocidade instantânea (Km/h)'] = velocidade_instantânea
dados = dados.drop('Duracao alto', axis=1)
tempo_volta = dados['Tempo de volta (ms)'].values 
print(dados)
plt.hist(tempo_volta, bins ='auto')
plt.xlabel('Tempo de volta (ms)')
plt.ylabel('Frequência')
plt.savefig('C:/Users/sonic/OneDrive/Documentos/Onboarding/Python/Histograma.jpg', dpi = 300)
plt.show()
dados.to_excel('C:/Users/sonic/OneDrive/Documentos/Onboarding/Python/Resultados.xlsx', index=False)
