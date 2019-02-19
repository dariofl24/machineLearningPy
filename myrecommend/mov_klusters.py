import numpy as np
import pandas as pd


def distEclud(vecA, vecB):
    #print(vecA)
    #print(vecB)
    return (np.sum((vecA - vecB)**2.0))**0.5

def findSimilar_single(dff,baseIdx,limit=5):

    base_mov = dff.loc[baseIdx]

    nn_index = []
    nn_dist = []

    for idx in dff.index.values:

        if(idx != baseIdx):
            nn_index.append(idx)
            dist = distEclud(dff.loc[idx],base_mov)
            nn_dist.append( 1./(1.+dist) )

    return pd.Series(data=nn_dist,index= nn_index).sort_values(ascending = False)




# MAIN
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid')

#print(df.head())

rate_pos_map =	{
  0.5: 0,
  1.0: 1,
  1.5: 2,
  2.0: 3,
  2.5: 4,
  3.0: 5,
  3.5: 6,
  4.0: 7,
  4.5: 8,
  5.0: 9
}

dim_vec_list = []

for col in df.columns:
    dim_vec = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

    val_counts = df[col].value_counts().sort_index()
    summ = np.sum (val_counts.values)
    mov_vec = (val_counts/float(summ))*100.

    for idx in mov_vec.index.values:
        dim_vec[rate_pos_map[idx]] = mov_vec[idx]

    dim_vec_list.append(dim_vec)

df2 = pd.DataFrame(data=dim_vec_list,columns=[0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0],
index=df.columns.values)

#print(df2)

#print(df2.iloc[1])
#print(distEclud( df2.iloc[30],df2.iloc[101] ))

movie_usr ='Toy Story 3 (2010)'

similar = findSimilar_single(df2,movie_usr)
print(df2.loc[movie_usr])
print(similar)












#
