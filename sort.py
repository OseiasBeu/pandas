import pandas as pd

df = pd.read_excel('depara_categoria.xlsx', encoding='UTF-8')

#ordenando em ordem crescente
df.sort_values()

#ordenando em ordem decrescente
df.sort_values(ascending=False)

