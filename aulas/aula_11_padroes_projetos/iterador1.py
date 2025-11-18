# utilizando os pares chave-valor de um dicionário como iterador
capitais = {
    "França" : "Paris", 
    "Itália" : "Roma",
    "Espanha" : "Madri"
    }

for pais, cidade in capitais.items():
    # Lembrar de falar in dict / dict.keys() | dict.items() | dict.values()
    print(f"A capital de {pais} é {cidade}")


# utilizando uma array numpy como iterador
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
for elemento in arr:
    print(elemento)


# Utilizando um DataFrame como iterador
import pandas as pd
df = pd.DataFrame({
    'Nome' : ['Alice', 'David', 'Charlie'],
    'Idade' : [25, 30, 35]
})
for index, row in df.iterrows():
    print(f"Nome: {row['Nome']}, Idade: {row['Idade']}")