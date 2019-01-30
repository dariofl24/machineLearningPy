import pandas as pd
import numpy as np

df = pd.read_excel("/Users/darioflores/Documents/machineLearn/uci/default_credit_card_clients.xls", header = 1)

df.rename(columns = {"PAY_0":"PAY_1"}, inplace = True) #renaming mis-named column

print(df.head())

print(df['default payment next month'].value_counts())

print(df['EDUCATION'].value_counts())

print(df['MARRIAGE'].value_counts())

print(df['SEX'].value_counts())
