import pandas as pd

df  = pd.read_excel('depara_categoria.xlsx', encoding='UTF-8')
#Função de substituição ('a' por 'b')
result = df.apply(lambda x: x.replace('a','b'))
print(result)
print(df.head())