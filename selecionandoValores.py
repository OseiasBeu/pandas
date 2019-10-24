import pandas as pd

df = pd.read_excel('depara_categoria.xlsx', encoding='UTF-8')

#Selecionando a primeira linha da coluna
print(df.loc[0,'sku'])

print(df.index(df.loc[0,'sku'].index()))