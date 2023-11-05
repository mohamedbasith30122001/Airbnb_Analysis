# Airbnb_Analysis
## Airbnb Analysis Travel Industry, Property Management and Tourism (using streamlit,pandas,pymongo,Plotly and Tableau Data visulization)
# Introduction:
- Airbnb Analysis: Extracting data in MongoDB using  with Tableau Overview.Airbnb Analysis is a  web application which anlaysis data using tableau to improve customer interaction .
- Users can easly  analysis the information of a tourism,room booking,price prediction,country and locations difference between price and country and prototype and room type, and related columns to get the Tourism and Traveling  information.
- then displayed in a user-friendly format and can be seen in a Tableau or Streamlit  for future reference.
# Domain:
- Travel Industry, Property Management and Tourism
# Problem statement:
- This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.
- retrieve the Airbnb dataset using MongoDB Altlas connection, and ensure efficient data retrieval for analysis.Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.
- Develop a streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.
- Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.
- Analyze availability patterns across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.
- Create interactive visualizations that enable users to filter and drill down into the data.
- Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.
## Libraries
### Libraries/Modules needed for the project!
- Plotly, Seaborn - (To plot and visualize the data)
- Pandas - (To Clean and maipulate the data)
- Pymongo - (To store and retrieve the data by connecting with MongoDB Atlas)
- Streamlit - (To Create Graphical user Interface)
# Problem solution:
## what i did for project solution:
## workflow:
#### Step 1 :
- Establish a connection to the MongoDB Atlas database and retrieve the Airbnb dataset. 
#### Step 2 : 
- Clean the Airbnb dataset by handling missing values, removing duplicates, and transforming data types as necessary. Prepare the dataset for EDA and visualization tasks, ensuring data integrity and consistency.
#### Step 3 :
- Develop a streamlit web application that utilizes the geospatial data from the Airbnb dataset to create interactive maps.using technologies Pandas, PIL,plotly.express (px) libraries in imported  setup and running Features.
#### Step 4 :
  Use the cleaned data to analyze and visualize how prices vary across different locations, property types, and seasons. Create dynamic plots and charts that enable users to explore price trends, outliers, and correlations with other variables.
#### Step 5 :
- Utilize Tableau  to create a comprehensive dashboard that presents key insights from your analysis. Combine different visualizations, such as maps, charts, and tables, to provide a holistic view of the Airbnb dataset and its patterns.
#### Streamlit Dashboard workflow:
- **Home** : Displays an overview of the app including technologies used and a brief description of the app.
- **Tableau** : This section allows the user to interact the data  with tableau user can understand the airbnb offers and travel and tourism data. Example : price prediction,locaton based insights and bedtype, roomtype, property type and rating(review score) then host name,host id and country to select and choose easly using this tableau visualization.
- **Basic Overveiw** : its also like as tableau visulization but manly shows data top 10 and average informations.
- **Data Visualization** and **Exploration** to visualize information also like as tableau viualization information  using  streamlit plots.
# Tableau Visualization:
## Tableau Dashboard Image:
![Outlook](https://github.com/mohamedbasith30122001/Airbnb_Analysis/blob/main/Airbnb_project_github/Dashboard%201.png)
## Tableau Dashboard Link:
# Conclusion:
- I Created the project to used to detecting the  information to visualize the Tableau.
- It mostly  helped as customer knows about **Airbnb** price,locations,room,bed,prototype,country and host name,host id.. to easly interact with travel,tourism and other works.
- Customer can easly choose our affortable country to select affortable price and  their rating(review_scores). to visualizing the tableau and seeing informations.
- Through this exploratory data analysis and visualization project, we gained several interesting insights into the Airbnb rental market. Below we will summarise the answers to the questions that we wished to answer at the beginning of the project:
- How do prices of listings vary by location? What localities in Countries are rated highly by guests? Spain has the low rentals and high rating and all property type by varying prices to  compared to the other boroughs. Prices are higher for rentals closer to city hotspots. Rentals that are rated highly on the location by the host also have higher prices.
