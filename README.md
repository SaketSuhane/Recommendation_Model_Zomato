![image](https://user-images.githubusercontent.com/123991455/235980695-c5be9af5-2b50-4cc7-8577-b54ca7fd61b8.png)

## Context
I was always fascinated by the food culture of Bengaluru. Restaurants from all over the world can be found here in Bengaluru. From United States to Japan, Russia to Antarctica, you get all type of cuisines here. Delivery, Dine-out, Pubs, Bars, Drinks,Buffet, Desserts you name it and Bengaluru has it. Bengaluru is best place for foodies. The number of restaurant are increasing day by day. Currently which stands at approximately 12,000 restaurants. With such an high number of restaurants. This industry hasn't been saturated yet. And new restaurants are opening every day. However it has become difficult for them to compete with already established restaurants. The key issues that continue to pose a challenge to them include high real estate costs, rising food costs, shortage of quality manpower, fragmented supply chain and over-licensing. This Zomato data aims at analysing demography of the location. Most importantly it will help new restaurants in deciding their theme, menus, cuisine, cost etc for a particular location. It also aims at finding similarity between neighborhoods of Bengaluru on the basis of food. The dataset also contains reviews for each of the restaurant which will help in finding overall rating for the place.

## Content 📋
The basic idea of analyzing the Zomato dataset is to get a fair idea about the factors affecting the establishment of different types of restaurant at different places in Bengaluru, aggregate rating of each restaurant, Bengaluru being one such city has more than 12,000 restaurants with restaurants serving dishes from all over the world. With each day new restaurants opening the industry has’nt been saturated yet and the demand is increasing day by day. Inspite of increasing demand it however has become difficult for new restaurants to compete with established restaurants. Most of them serving the same food. Bengaluru being an IT capital of India. Most of the people here are dependent mainly on the restaurant food as they don’t have time to cook for themselves. With such an overwhelming demand of restaurants it has therefore become important to study the demography of a location. What kind of a food is more popular in a locality. Do the entire locality loves vegetarian food. If yes then is that locality populated by a particular sect of people for eg. Jain, Marwaris, Gujaratis who are mostly vegetarian. These kind of analysis can be done using the data, by studying the factors such as • Location of the restaurant • Approx Price of food • Theme based restaurant or not • Which locality of that city serves that cuisines with maximum number of restaurants • The needs of people who are striving to get the best cuisine of the neighborhood • Is a particular neighborhood famous for its own kind of food.

“Just so that you have a good meal the next time you step out”

We were able scrape the Zomato website successful and were able to extract around 3000 records.



## Methodology 🛠️
### Phase I,
Web Scrapping 
Scrapped the data using Beautiful soup and Selenium for scrolling

### Phase II,
Data Preprocessing
Cleaning the Raw data using Numpy, Panadas  and Excel 

### Phase III,
Model Building 
Worked on different models and Random Forest was the best suitable

### Phase IV,
Model Deployment
Deployed the model on HTML webpage

## Inspiration
I was always astonished by how each of the restaurants are able to keep up the pace inspite of that cutting edge competition. And what factors should be kept in mind if someone wants to open new restaurant. Does the demography of an area matters? Does location of a particular type of restaurant also depends on the people living in that area? Does the theme of the restaurant matters? Is a food chain category restaurant likely to have more customers than its counter part? Are any neighborhood similar ? If two neighborhood are similar does that mean these are related or particular group of people live in the neighborhood or these are the places to it? What kind of a food is more popular in a locality. Do the entire locality loves vegetarian food. If yes then is that locality populated by a particular sect of people for eg. Jain, Marwaris, Gujaratis who are mostly vegetarian. There are infacts dozens of question in my mind. lets try to find out the answer with this dataset.

## Sections 📚
✔️ Exploratory Data Analysis\
✔️ Visualization \
✔️ Rate Prediction\
✔️ Restraurant Prediction\
✔️ Recommendation System\

## Quick Summary

    1. Using Selenium And BeautifulSoup libraries of Python we Extracted data present on page and stored it in series and merging them to get DatFrame
    	a)MainPage Scrapper
![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/bcf3804c-4734-40e8-b303-fd905eadb7c3)

![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/539d66e8-cf48-4874-a548-eddbb9e4b365)

    
    	b)Restaurants info Scrapper
    
![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/577b3980-c832-4306-8b92-a1974549808b)

![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/ce8083e6-d33f-4974-88f4-961433711cb1)

![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/05620b7e-e18c-4fff-8fd4-29dfb7d3afa8)

 
    2. After obtaining the DataFrame we performed some data cleansing operation using Power Querry Editor , Excel and obtained a single table.
    	a) Raw Data 
      ![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/8a3b450c-cc24-4d73-a731-450b2a95c910)
      
      ![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/e6ed4bf2-f460-472e-b808-6d78a3a5b9d6)

      a) Cleaned Table and Joined Table 
      
	![image](https://github.com/SaketSuhane/Recommendation_Model_Zomato/assets/123991455/d79eb1bf-3fa4-4f29-83d5-5dc821c799e9)

       
    3. After joining the tables, we imported the dataset into Power BI in order to visualize the data.
    
    4. In Power Bi, we made some useful KPI's and some user friendly charts.
    
    5. Created a interactive and dynamic dashboard at the end using Power Bi and generated some useful insights.

## Conclusion
As per our analysis, if the person wants to open a remote kitchen in Bangalore he/she should prefer opening it in Shanti Nagar or Basavanagudi, since the place is having less no of restaurant which reduces the competition and it has some of the expensive restaurants in the Banglore, hence the person can deliver food at lower price which reduces the competition even further.

The second suggestion would be sell North Indian, South Indian cuisine as they are demanded the most by the customers and they can keep the price ranging from 300 - 400 Rs for Non vegetarian category and 200 - 300 Rs for vegetarian category.

## Images 

![image](https://user-images.githubusercontent.com/123991455/235981550-08cef644-e16d-4742-bf34-fd3622e8670d.png)



![image](https://user-images.githubusercontent.com/123991455/235981643-18f4980e-4027-49bf-ac16-95cd88426a3c.png)



![image](https://user-images.githubusercontent.com/123991455/235982036-567be9f4-0b1b-43bd-b346-34d6ee9c31c9.png)



![image](https://user-images.githubusercontent.com/123991455/235982186-69a4c94e-d935-4a3e-9666-e875d0361417.png)


