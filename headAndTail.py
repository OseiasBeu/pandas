import pandas as pd
# s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
# print(s)


# # Criando um dicionário onde cada chave será uma coluna do DataFrame >>>
# data = {
#     'Pais': ['Bélgica', 'Índia', 'Brasil'],
#     'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
#     'População': [123465, 456789, 987654]
# }

# df = pd.DataFrame(data,columns=['Pais', 'Capital','População'])

# print(df)

xlsx = pd.ExcelFile('depara_categoria.xlsx')
df = pd.read_excel(xlsx, 'Sheet1', encoding='utf-8')
print('HEAD')
print(df.head())
print(df.tail())


#

