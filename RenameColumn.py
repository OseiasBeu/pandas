import pandas as pd

df = pd.read_excel('depara_categoria.xlsx','Sheet1',encoding='UTF-8')

#Se seu DataFrame possui 3 coluna, passe 3 novos valores em uma lista:
df.columns = ['Coluna 1','Coluna 2', 'Coluna 3']

