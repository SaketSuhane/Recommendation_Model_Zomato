import numpy as np
import pandas as pd
import json
from flask import Flask, redirect, url_for, render_template, request
import pickle

#Datasets
df = pd.read_csv(r".\CSV Data\processed_data.csv")
normal_form = pd.read_csv(r".\CSV Data\normal_form.csv")
restaurant_data = pd.read_csv(r".\CSV Data\restaurant_data.csv")
df_json = json.loads(df.to_json(orient='records'))

#Encoding Data
cuisines = df['cusine'].unique()
print(cuisines)
cuisine_dic = {}
for i in range(len(cuisines)):
    cuisine_dic[cuisines[i].lower().strip()] = i

location=df['Location'].unique()
print(location)
location_dic={}
for i in range(len(location)):
    location_dic[location[i].lower().strip()] = i

# Create flask app
app = Flask(__name__)

#Loading Models
random_forest_regression = pickle.load(open("./Model/rfr_model.pkl", "rb"))
random_forest_classifier = pickle.load(open("./Model/rfc_model.pkl", "rb"))

#Defining Routes
#Base Route
@app.route('/')
def inputs():
    return render_template('inputs-Final.html',cuisines=cuisines,locations=location)

#Recommendation Route
@app.route("/predict", methods = ["POST","GET"])
def predict():
    #Pulling Data From "Form"
    if request.method == "POST":
        a = request.form.get("cusine")
        b = request.form.get("price")
        c = request.form.get("Location")
        
    #Processing Input Data
    cuisine = str(a).lower().strip()
    price = int(b)
    location = str(c).lower().strip()
    

    #getting encoded values from dictionary
    encoded_cuisine = cuisine_dic[cuisine]
    encoded_location = location_dic[location]

    #Regression Model
    rf_reg_inputs = [[int(encoded_cuisine), int(encoded_location)]]
    price_prediction = random_forest_regression.predict(rf_reg_inputs)
    print(price_prediction)
    predicted_price = round(price_prediction[0], 2)
    print(predicted_price)

    #Classification Model
    rf_classifier_input = [[int(encoded_cuisine), price]]
    location_prediction = random_forest_classifier.predict(rf_classifier_input)
    print(location_prediction)
    predicted_location = list(location_dic.keys())[list(location_dic.values()).index(location_prediction)]
    print(predicted_location)


    #getting aggregation result
    def search_engine(cusine, location):
        popular_cus = ''
        popular_cusine = normal_form[normal_form['Location'] == location].groupby('cusine')[
            'cusine'].count().sort_values(ascending=False)
        popular_cusine = popular_cusine[popular_cusine == popular_cusine.max()].index.tolist()
        if len(popular_cusine) == 1:
            popular_cus = popular_cusine[0]
        else:
            for i in popular_cusine:
                if i not in popular_cusine[-1]:
                    popular_cus += i
                    popular_cus += ','
                else:
                    popular_cus += i

        popular_restaurant_cusine = restaurant_data[
            (restaurant_data['cusine'].str.contains(cusine)) & (restaurant_data['Location'] == location)].sort_values(
            ['review', 'rating'], ascending=False).iloc[0][0]

        avg_price = restaurant_data['price'][restaurant_data['Location'] == location]

        most_popular_restaurant = restaurant_data[restaurant_data['Location'] == location].sort_values(
            ['review', 'rating'], ascending=False)

        return [round(avg_price.mean(), 0), popular_cus, most_popular_restaurant.iloc[0][0],
                most_popular_restaurant.iloc[0][4], popular_restaurant_cusine]

    avg_price,pop_cuisine,mpop_rest,serve,rest_popcui=search_engine(cuisine,location)

    return render_template("Recommendation-Final.html", predict1="{}".format(int(predicted_price)), predict2="{}".format(predicted_location.title()),
                           average_text="{}".format(int(avg_price)),
                           popular_text="{}".format(pop_cuisine.title()), rest_text="{}".format(mpop_rest.title()),
                           serves_text="{}".format(serve.title()), poprest_text="{}".format(rest_popcui.title()))


if __name__ == "__main__":
    app.run(debug=True)
