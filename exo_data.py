import pandas as pd
import numpy as np
import seaborn as sns

#1
houses = pd.read_csv('../house_pricing.csv')
print(houses)
#2 liste des variables
print(houses.columns)
df = sns.load_dataset('df')
print(df)