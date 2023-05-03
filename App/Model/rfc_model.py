import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

df=pd.read_csv(r"C:/Users/kamle/Desktop/ML Project/Final/App/CSV Data/processed_data.csv")
df.drop(columns=['Unnamed: 0','Rating'],inplace=True)

cuisines=df['cusine'].unique()
cuisine_dic={}
for i in range(len(cuisines)):
    cuisine_dic[cuisines[i]]=i
df=df.replace({'cusine': cuisine_dic})

location=df['Location'].unique()
location_dic={}
for i in range(len(location)):
    location_dic[location[i]]=i
df=df.replace({'Location': location_dic})

X=df[['cusine','price_for_one']].values
Y=df['Location'].values

X_train1,X_test1,Y_train1,Y_test1 = train_test_split(X,Y,test_size=0.1,random_state=42)

rfc=RandomForestClassifier(n_estimators=20,min_samples_split=10,max_features='log2',max_depth=10,criterion='gini')
rfc.fit(X_train1,Y_train1)

pickle.dump(rfc, open("rfc_model.pkl", "wb"))