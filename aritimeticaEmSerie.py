import pandas as pd

df = pd.read_excel('depara_categoria.xlsx', encoding='UTF-8')

s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s)
#Somando tpdps ps vaçores presentes na Series por 2
print(s.add(2))

#subtraindo 2 de todos os valores
print(s.sub(2))

#multiplicando por 2
s.mul(2)

#dividindo valores por 2
s.div(2)

