import pandas as pd

df = pd.read_excel('depara_categoria.xlsx','Sheet1',encoding='UTF-8')

#quantidade de linhas e colunas do DataFrame
print(df.shape)


#Descrição do Index
print(df.index)


#Colunas presentes no DataFrame
print(df.columns)

#Contagem de dados não-nulos
print(df.count())