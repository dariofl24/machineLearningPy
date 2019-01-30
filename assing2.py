import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

tr_path = './train.csv'

data = pd.read_csv(tr_path)

print(data[['Street','Alley']])
