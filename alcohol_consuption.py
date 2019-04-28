from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans

import pandas as pd

# Carga da base de dados a ser utilizada
# [0] country    ; [1] beer_servings ; [2] spirit_servings ; [3] wine_servings      ; [4] total_litres_of_pure_alcohol ;
# [5] continente ; [6] região        ; [7] população       ; [8] população urbana(%);
data = pd.read_excel("drinks.xlsx")

# Comando para verificação das 5 primeiras linhas da base de dados
#print(data.head())

#Define os atributos utilizados
X = data.iloc[:, :5]

#Define o possível target
y = data['continente']

#Define nº clusters baseado no número de registros únicos do target
num_clusters = len(set(y))

#print(X.head())
print(num_clusters)

