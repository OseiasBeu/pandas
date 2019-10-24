import pandas as pd

xlsx = pd.ExcelFile('depara_categoria.xlsx')
df = pd.read_excel(xlsx, 'Sheet1', encoding='utf-8')

#Remover Colunas
print('RM COL')
print(df.drop('categoria',axis=1))