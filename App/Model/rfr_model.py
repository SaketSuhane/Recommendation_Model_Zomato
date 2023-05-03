import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
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

X=df[['cusine','Location']].values
Y=df['price_for_one'].values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.1,random_state=42)

rfg=RandomForestRegressor(n_estimators=20,min_samples_split=8,max_features='sqrt',max_depth=10,criterion='squared_error')
rfg.fit(X_train,Y_train)

pickle.dump(rfg, open("rfr_model.pkl", "wb"))

