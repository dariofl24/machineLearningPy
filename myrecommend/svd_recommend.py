import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

me_rate = [3.5, 0.0, 3.0, 3.0, 5.0, 2.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 4.5, 0.0, 3.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 4.5, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 3.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 4.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 2.0, 2.0, 4.5, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 4.5, 0.0, 0.0, 5.0, 0.0, 0.0, 2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 3.0, 3.5, 2.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 3.5, 0.0, 4.0, 0.0, 5.0, 0.0, 4.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 5.0, 5.0, 0.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 4.0, 0.0, 4.5, 0.0, 0.0, 4.5, 4.5, 5.0, 0.0, 0.0, 0.0, 4.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 4.5, 3.5, 0.0, 0.0, 0.0, 5.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 2.0, 3.5, 2.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 0.0, 2.0, 4.5, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 3.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 5.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 3.0, 4.5, 0.0, 0.0, 0.0, 2.0, 0.0, 3.5, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 3.5, 0.0, 5.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 2.0, 3.5, 0.0, 5.0, 3.5, 0.0, 4.5, 0.0, 0.0, 2.0, 0.0, 4.0, 4.5, 0.0, 0.0, 0.0, 3.0, 3.5, 3.0, 0.0, 0.0, 0.0, 2.0, 3.0, 3.0, 3.5, 4.0, 0.0, 2.0, 0.0, 3.0, 0.0, 2.0, 3.5, 2.0, 5.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 3.5, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 5.0, 3.0, 4.0, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 3.5, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.0, 5.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 4.5, 4.0, 4.0, 4.0, 0.0, 0.0, 3.0, 0.0, 4.5, 4.0, 0.0, 0.0, 0.0, 2.0, 0.0, 3.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 4.0, 2.0, 0.0, 3.5, 4.0, 0.0, 5.0, 3.5, 0.0, 0.0, 0.0, 0.0, 3.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 2.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 0.0, 3.5, 2.0, 2.0, 4.5, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.5, 2.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.5, 4.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 4.0, 0.0, 0.0, 4.5, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 2.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 4.0, 0.0, 4.0, 0.0, 4.5, 4.5, 0.0, 4.0, 0.0, 0.0, 0.0, 3.5, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.5, 2.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 4.5, 0.0, 0.0, 4.5, 0.0, 0.0, 0.0, 4.0, 3.5, 4.5, 0.0, 5.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0]

def drop_val (df, to_drop):

    for col in df.columns:
        df = df[ df[col] !=  to_drop]

    return df

#

def e_sim(ser1, ser2):

    sqrtt= (ser1 - ser2) ** 2.

    distt = sqrtt.sum() ** .5

    return 1. / (1. + distt)

def get_cos(vec1,vec2):

    return np.dot(vec1, vec2) / (np.sqrt(np.dot(vec1,vec1)) * np.sqrt(np.dot(vec2,vec2)))
#

def get_proyection_cos(test_v,main_v):

    product_ = np.multiply(test_v , main_v)

    rate = (float(main_v[product_ != 0.].shape[0]) / float(main_v.shape[0]))


    if(rate > 0):
        coss = get_cos(test_v[product_ != 0.],main_v[product_ != 0.])

        return coss * rate
    else:
        return 0.
#get_proyection_cos

def get_similar_users_proy(df,main):

    values_list = []

    for idx in df.index.values:

        t_usr = np.array( df.loc[idx].values )
        sim_val = get_proyection_cos(np.array(t_usr),np.array(main))
        values_list.append(sim_val)

    values= np.array(values_list)

    average = np.average(values)

    maxx=np.ndarray.max(values)

    std=np.std(values)

    return df[values >= (maxx - ( (maxx - average)/1.85 ))]
#get_similar_users_proy

def get_similar_users(df,usr):

    sim_usr_idx = []

    COS_85=0.087
    COS_80=0.174
    COS_75=0.259
    COS_70=0.342
    COS_60=0.5


    for idx in df.index.values:
        t_usr = np.array( df.loc[idx].values )

        coss = get_cos(t_usr,usr)
        norm_proy = np.dot(usr, t_usr)/np.dot(usr,usr)

        #print( str(coss) +" :: "+ str(norm_proy) )

        if coss >= COS_75 and norm_proy >= 0.45 and norm_proy <= 1.1:
            #print( str(coss)+' :: '+ str(np.dot(usr, t_usr)/np.dot(usr,usr)))
            sim_usr_idx.append(idx)
            #print('OK')

    return df.loc[sim_usr_idx]


#get_similar_users

#Main
df = pd.read_csv("../java/testproj/reviewsTable_0_30.csv").set_index('custid').fillna(0.)
df2 = pd.DataFrame([me_rate], columns=df.columns.values,index=[0])

#print(df.head())
not_rated = df2.columns[df2.loc[0] == 0.].values #[40:41]
do_rated = df2.columns[df2.loc[0] != 0.]

df_sim = get_similar_users(df, np.array(me_rate))

#print(not_rated)
print("df_sim")
print(df_sim)

predictions = []

for mov in not_rated:
    #print('get score for :: '+mov)

    sum_sim = 0.
    sum_prod = 0.

    for df_mov in do_rated:

        if mov != df_mov:

            df_x = drop_val(df_sim.loc[:,[df_mov,mov]],0.)
            #print(df_x)

            if float(len(df_x.index.values)) >= float(len(df_sim.index.values))/2.5:

                vec_a = df_x.iloc[:,0].values
                vec_b = df_x.iloc[:,1].values

                #print(vec_a)
                #print(vec_b)

                sim_cos = get_cos(vec_a,vec_b)
                sim_e = e_sim(vec_a,vec_b)
                joint_sim = sim_cos * sim_e

                usr_rate = df2.loc[:,df_mov].values[0]
                zim = sim_e

                #print(usr_rate)

                #print(sim_cos)
                #print(sim_e)
                #print(joint_sim)
                #print("*****")

                sum_prod = sum_prod + (usr_rate * zim)
                sum_sim = sum_sim + zim
                #print(sum_prod)
                #print(sum_sim)
                #if
        #
    #print(sum_prod)
    #print(sum_sim)

    if sum_sim > 0.:
        prediction = sum_prod / sum_sim
    else:
        prediction = 0.

    predictions.append(prediction)

    #print('Pred :: '+ str(prediction))
    #print('---------------')

print('++++++++++++++++++++++++++++++++')
predictions_series = pd.Series(data = predictions,index=not_rated).sort_values(ascending = False)

print(predictions_series[predictions_series > 0.])













#
