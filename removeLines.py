import pandas as pd

df = pd.read_excel('depara_categoria.xlsx','Sheet1',encoding='UTF-8')



#Remover Linhas
print('RM LIN')
print(df.drop([0,1]))
