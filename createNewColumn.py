import pandas as pd

df = pd.read_excel('depara_categoria.xlsx','Sheet1',encoding='UTF-8')

df['Nova Coluna'] = 0
print(df)