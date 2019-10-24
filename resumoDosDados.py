import pandas as pd

df = pd.read_excel('depara_categoria.xlsx','Sheet1',encoding='UTF-8')

#Soma dos valores de um dataFrame
print('Soma dos valores de um dataFrame')
print(df.sum())

#Menor valor de um dataframe
print('Menor valor de um dataframe')
print(df.min())

#Maior Valor:
print(df.max())

#Index do menor valor:
# mi = df.idmin()
# print(mi)
# ma = df.idmax()
# print(ma)


#Resumo estatístico do Data Frame
print('-----Resumo-------------')
print(df.describe)


#Média dos valores:
print(df.mean())


#Mediana dps valores:
print(df.median())