import pandas as pd

df = pd.read_excel('depara_categoria.xlsx', encoding='UTF-8')

#Filtrando o DataFrame para mostrar apenas valores pares

print(df[df['id'] % 2 == 0])