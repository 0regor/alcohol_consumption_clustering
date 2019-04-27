from time import time
import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.cluster import KMeans

import pandas as pd

# Carga da base de dados a ser utilizada
data = pd.read_csv("drinks.csv")

print(data.head())
