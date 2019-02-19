import numpy as np
import pandas as pd

def series_avg(series):

    index = series.index.values
    values = series.values

    nn = float(np.sum(values))
    ss = float(np.sum(values * index))

    avg = ss / nn

    return avg

def df_ratings_avg(dff):

    avg_index = []
    avg_data = []

    for col in dff.columns:
        val_counts = dff[col].value_counts().sort_index()
        avgg=series_avg(val_counts)

        avg_index.append(col)
        avg_data.append(avgg)

    avg_series = pd.Series(data = avg_data,index=avg_index).sort_values(ascending = False)

    return avg_series

# MAIN
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid')

print(df.head())

ratings = df_ratings_avg(df)

for mov in ratings.index.values:
    print(mov)
    print(ratings[mov])
    print('-')

#print(df_ratings_avg(df))

















#
