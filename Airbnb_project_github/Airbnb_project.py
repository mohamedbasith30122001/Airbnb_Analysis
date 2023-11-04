# Importing Libraries
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# Setting up page configuration
icon = Image.open("airbnb1.png")
st.set_page_config(page_title= "Airbnb Data Visualization | By Mohamedbasith A",
page_icon=icon,layout= "wide",initial_sidebar_state= "expanded",
menu_items={'About': """# This dashboard app is created by *Mohamedbasith A*!Data has been gathered from mongodb atlas"""})
st.markdown("<h1 style='text-align:center; color:crimson;'>Airbnb Analysis</h1>", unsafe_allow_html=True)

#Creating option menu in the menu bar
selected = option_menu(None,["Home", "Tableau", "Basic Overview", "Data Visualization", "Exploration","About"],
                        icons=["house", "list-task", "gear", "tools", "bar-chart","toggles"],
                        default_index=0,
                        orientation="horizontal",
                        styles={"nav-link": {"font": "sans serif", "font-size": "20px", "text-align": "centre","--hover-color": "#F27575","margin": "-2px","transition": "color 0.3s ease, background-color 0.3s ease"},
                                "nav-link-selected": {"font": "sans serif", "background-color": "#CF3030"},
                                "icon": {"font-size": "20px"}
                                }
                        )

# READING THE CLEANED DATAFRAME
df = pd.read_csv('Airbnb_data.csv')

# -----------------------------------------------Home Section--------------------------------------------------
if selected == "Home":
    col1,col2, = st.columns(2)
    with col1:
        st.markdown("<h2 style='color:red;'>Airbnb Analysis</h2>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:firebrick;'>Technologies:</h3>", unsafe_allow_html=True)
        st.markdown("#### Python, Pandas, Plotly, Streamlit, MongoDB, Python scripting,Data Preprocessing, Visualization, EDA")
        st.markdown("<h3 style='color:firebrick;'>Overview:</h3>", unsafe_allow_html=True)
        st.markdown("#### To conduct an analysis of Airbnb data using MongoDB Atlas, the process "
                    "involves cleaning and preparing the data, creating interactive visualizations, and generating "
                    "dynamic plots. The goal is to extract insights regarding price fluctuations, availability trends, "
                    "and location-based patterns within the dataset.")
    with col2:
        st.markdown("<h3 style='color:firebrick;'>Domain:</h3>", unsafe_allow_html=True)
        st.markdown("### Travel Industry, Property Management and Tourism")
        col3,col4, = st.columns(2)
        with col3:
            st.image("airbnb2.jfif")
        with col4:
            st.image("airbnb1.png")

# -----------------------------------------------Tableau Section--------------------------------------------------
if selected == "Tableau":
    st.markdown("<h2 style='color:firebrick; text-align: center;'>Tableau (Airbnb Data visualization)</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:crimson;'>Introduction:</h3>",unsafe_allow_html=True)
    st.write('##### Tableau is a software company that offers collaborative data visualization software for organizations working with business information analytics. ')
    st.markdown("<h3 style='color:crimson;'>Usages:</h3>",unsafe_allow_html=True)
    st.write('##### Organizations use Tableau to visualize data and reveal patterns for analysis in business intelligence, making the data more understandable.')
    st.markdown("<h3 style='color:crimson;'>Tableau public visulization Link:</h3>",unsafe_allow_html=True)
    st.info('##### https://public.tableau.com/app/profile/mohamedbasith.a/viz/sheet1_16990248307520/Dashboard1?publish=yes')

# -----------------------------------------------Basic Overview Section-------------------------------------------------
if selected == "Basic Overview":
    st.markdown("<h3 style='color:firebrick; text-align: center;'>Basic Overview of Airbnb Data</h3>", unsafe_allow_html=True)
    country = st.multiselect('Select a Country :',sorted(df.Country.unique()))
    property1 = st.multiselect('Select Property Type :',sorted(df.Property_type.unique()))
    room = st.multiselect('Select Room Type :',sorted(df.Room_type.unique()))
    price = st.slider('Select Price :', df.Price.min(), df.Price.max(),
                    (df.Price.min(), df.Price.max())
                    )
    
    # -----Taking the user inputs and merging then with MongoDB Query for Data Retrieval-----
    query = f'Country in {country} & Room_type in {room} & Property_type in {property1} & Price >= {price[0]} & Price <= {price[1]}'

    # -----Top 10 Property Types-----
    df1 = df.query(query)
    counts_df1 = df1.groupby(["Property_type"]).size().reset_index(name="count").sort_values(by='count',ascending=False).head(10)
    fig = px.bar(counts_df1,
                title='Top 10 Property Types',
                x='count',
                y='Property_type',
                color='Property_type',
                color_continuous_scale='sunset')
    fig.update_layout(width=800, height=600)
    fig.update_layout(title_font=dict(size=28),title_font_color='crimson')
    fig.update_yaxes(title='Property Type')
    fig.update_xaxes(title='Count')
    st.plotly_chart(fig, use_container_width=True)

    # -----Top 10 Hosts with Highest number of Listings-----
    df2 = df.query(query)
    counts_df2 = df2.groupby(["Host_name"]).size().reset_index(name="count").sort_values(by='count',ascending=False).head(10)
    fig = px.bar(counts_df2,
                title='Top 10 Hosts with Highest number of Listings',
                x='count',
                y='Host_name',
                color='Host_name',
                color_continuous_scale='sunset')
    fig.update_layout(width=800, height=600)
    fig.update_layout(title_font=dict(size=28),title_font_color='crimson')
    fig.update_yaxes(title='Host Name')
    fig.update_xaxes(title='Count')
    st.plotly_chart(fig, use_container_width=True)

    # -----Data of each Room Types-----
    df3 = df.query(query)
    counts_df3 = df3.groupby(["Room_type"]).size().reset_index(name="count")
    fig = px.pie(counts_df3,
                title='Data of each Room Types',
                names='Room_type',
                values='count')
    fig.update_layout(width=800, height=600)
    fig.update_layout(title_font=dict(size=28),title_font_color='crimson')
    fig.update_traces(textposition='outside', textinfo='value+label')
    st.plotly_chart(fig, use_container_width=True)

    # -----Total counts/listings based on Countries-----
    df4 = df.query(query)
    country_df = df4.groupby(['Country'], as_index=False)['Name'].count().rename(columns={'Name': 'count'})
    fig = px.choropleth(country_df,
                        title='Total Listings in each Country :',
                        locations='Country',
                        locationmode='country names',
                        color='count')
    fig.update_layout(width=800, height=600)
    fig.update_layout(title_font=dict(size=28),title_font_color='crimson')
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------Data Analysis and Visualization Section----------------------------------------
if selected == "Data Visualization":
    st.markdown("<h3 style='color:firebrick; text-align:center;'>Data Analysis and Visualization</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:firebrick; text-align:center;'>Visualization Options:</h4>", unsafe_allow_html=True)
    
    options = ["--select--","Display Difference Between review","Display Statistics",
               "Display Histogram of Selected Column","Display Box Plots","Display Outlier Counts"]
    select = st.selectbox("Select the option",options)

    #-----------Difference between countries and other requiered columns--------
    if select == "Display Difference Between review":
        st.markdown("<h3 style='color:crimson; text-align:center;'>Difference between other columns and average review data's:</h3>",unsafe_allow_html=True)
        columns = st.multiselect("Select a useful column:",df.columns)
        for column3 in columns:
            df1 = df.groupby(f'{column3}', as_index=False)['Review_scores'].mean()
            st.markdown(f'<h3 style="color:#5DBB63">Difference between {column3} and  Review_scores Bar Plot</h3>',unsafe_allow_html=True)
            fig = px.bar(df1, x=column3,y='Review_scores',color=column3,color_continuous_scale='sunset')
            fig.update_layout(width=800, height=480)
            st.plotly_chart(fig, use_container_width=True)

    # ----------Analysis of Numerical Data in the DataFrame----------
    if select == "Display Statistics":
        st.markdown("<h3 style='color:crimson; text-align:center;'>Analysis of Numerical Data in the DataFrame:</h3>", unsafe_allow_html=True)
        st.markdown('<h3 style="color:#5DBB63">Various Stats of the Numerical Data Columns of the DataFrame</h3>',unsafe_allow_html=True)
        st.write(df.describe())

    # ----------Display Histogram of Selected Column----------
    if select == "Display Histogram of Selected Column":
        st.markdown("<h3 style='color:crimson; text-align:center;'>Target Analysis:</h3>",unsafe_allow_html=True)
        all_columns = st.selectbox("Select a column :", df.columns)
        st.markdown(f'<h3 style="color:#5DBB63">Histogram of {all_columns}</h3>',unsafe_allow_html=True)
        fig = px.histogram(df, x=all_columns, color_discrete_sequence=(['#4772F7']))
        fig.update_layout(width=800, height=480)
        st.plotly_chart(fig)
    
    # ----------Display Box Plots----------
    if select == "Display Box Plots":
        st.markdown("<h3 style='color:crimson; text-align:center;'>Box Plots:</h3>",unsafe_allow_html=True)
        numerical_columns = df.select_dtypes(exclude='object').columns
        selected_numerical_columns = st.selectbox("Select numerical columns for box plots:",numerical_columns)
        st.markdown(f'<h3 style="color:#5DBB63">Box Plot of {selected_numerical_columns}</h3>',unsafe_allow_html=True)
        fig = px.box(df, y=selected_numerical_columns)
        fig.update_layout(width=800, height=480)
        st.plotly_chart(fig)

    # ----------Display Outlier Counts----------
    if select == "Display Outlier Counts":
        st.markdown("<h3 style='color:crimson; text-align:center;'>Outlier Analysis:</h3>",unsafe_allow_html=True)
        outlier_df = df.select_dtypes(exclude='object').apply(lambda x: sum((x - x.mean()) > 2 * x.std())).reset_index(name="outliers")
        st.write(outlier_df)

# -----------------------------------------------Exploration Section----------------------------------------------------
if selected == "Exploration":
    tab1, tab2 = st.tabs(['Data Exploration with Price','Data Exploration with Review/Rating'])
    with tab1:
        st.markdown("<h3 style='color:firebrick;'>Data Exploration with Price</h3>", unsafe_allow_html=True)
        # -----Creating Filter option for user inputs-----
        country = st.multiselect('Select a Country :',sorted(df.Country.unique()))
        property1 = st.multiselect('Select Property Type :',sorted(df.Property_type.unique()))
        room = st.multiselect('Select Room Type :',sorted(df.Room_type.unique()))
        price = st.slider('Select Price :', df.Price.min(), df.Price.max(),(df.Price.min(), df.Price.max()))

        # -----Taking the user inputs and merging then with MongoDB Query for Data Retrieval-----
        query = f'Country in {country} & Room_type in {room} & Property_type in {property1} & Price >= {price[0]} & Price <= {price[1]}'

        # -----Different Room Types based on their Average Booking Price-----
        st.markdown("<h3 style='color:crimson; text-align:center;'>Different Room Types based on their Average Booking Price:</h3>",unsafe_allow_html=True)
        df5 = df.query(query)
        price_df1 = df5.groupby('Room_type', as_index=False)['Price'].mean().sort_values(by='Price')
        fig = px.bar(price_df1, x='Room_type',y='Price',color='Price',color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)

        # -----Different Countries based on their Average Booking Price-----
        st.markdown("<h3 style='color:crimson; text-align:center;'>Different Countries based on their Average Booking Price:</h3>",unsafe_allow_html=True)
        df6 = df.query(query)
        price_df2 = df6.groupby('Country', as_index=False)['Price'].mean().sort_values(by='Price')
        fig = px.bar(price_df2,x='Country',y='Price',color='Price',color_continuous_scale='Viridis')
        st.plotly_chart(fig, use_container_width=True)

        # -----Availability by Room Type-----
        st.markdown("<h3 style='color:crimson; text-align:center;'>Availability by Room Type:</h3>",unsafe_allow_html=True)
        df7 = df.query(query)
        fig = px.box(df7, x='Room_type',y='Availability_365',color='Room_type')
        st.plotly_chart(fig, use_container_width=True)

        # -----Different Countries based on their Average Booking Price ==> SCATTERED PLOT-----
        st.markdown("<h3 style='color:crimson; text-align:center;'>Different Countries based on their Average Booking Price ==> SCATTERED PLOT:</h3>",unsafe_allow_html=True)
        df8 = df.query(query)
        country_df1 = df8.groupby('Country', as_index=False)['Price'].mean()
        fig = px.scatter_geo(data_frame=country_df1,locations='Country',color='Price',size='Price',locationmode='country names')
        st.plotly_chart(fig, use_container_width=True)

        # -----Different Countries based on their Average Availability ==> SCATTERED PLOT-----
        st.markdown("<h3 style='color:crimson; text-align:center;'>Different Countries based on their Average Availability ==> SCATTERED PLOT:</h3>",unsafe_allow_html=True)
        df9 = df.query(query)
        country_df2 = df9.groupby('Country', as_index=False)['Availability_365'].mean()
        country_df2.Availability_365 = country_df2.Availability_365.astype(int)
        fig = px.scatter_geo(data_frame=country_df2,locations='Country',color='Availability_365',size='Availability_365',locationmode='country names')
        st.plotly_chart(fig, use_container_width=True)

        # -----Different  Bed_type  based on Price ==> -----
        st.markdown("<h3 style='color:crimson; text-align:center;'>Different Bed_type based on Price:</h3>",unsafe_allow_html=True)
        df0 = df.query(query)
        country_df1 = df0.groupby('Bed_type', as_index=False)['Price'].mean()
        fig = px.pie(country_df1, names = 'Bed_type', values = 'Price',hole=0.4)
        st.plotly_chart(fig,use_container_width=True)

    
if selected == "About":
    st.markdown('## :red[About this project:]')
    st.markdown("<h3 style='color:crimson;'>Introduction:</h3>",unsafe_allow_html=True)
    st.write('##### Airbnb Analysis: Extracting data in MongoDB using  with Tableau Overview.Airbnb Analysis is a  web application which anlaysis data using tableau to improve customer interaction . Users can easly  analysis the information of a tourism,room booking,price prediction,country and locations difference between price and country and prototype and room type, and related columns to get the Tourism and Traveling  information. then displayed in a user-friendly format and can be seen in a Tableau or Streamlit  for future reference.')
    st.write("")
    st.markdown("<h3 style='color:crimson;'>Problem statement:</h3>",unsafe_allow_html=True)
    st.write("##### This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.")
    st.write('##### retrieve the Airbnb dataset using MongoDB Altlas connection, and ensure efficient data retrieval for analysis.Clean and prepare the dataset, addressing missing values, duplicates, and data type conversions for accurate analysis.')
    st.write('##### Develop a streamlit web application with interactive maps showcasing the distribution of Airbnb listings, allowing users to explore prices, ratings, and other relevant factors.')
    st.write('##### Conduct price analysis and visualization, exploring variations based on location, property type, and seasons using dynamic plots and charts.')
    st.write('##### Analyze availability patterns across seasons, visualizing occupancy rates and demand fluctuations using suitable visualizations.')
    st.write('##### Investigate location-based insights by extracting and visualizing data for specific regions or neighborhoods.')
    st.write('##### Create interactive visualizations that enable users to filter and drill down into the data.')
    st.write('##### Build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.')
    st.write("")
    st.markdown("<h3 style='color:crimson;'>Problem solution:</h3>",unsafe_allow_html=True)
    st.markdown("<h4 style='color:crimson;'>what i did for project solution:</h4>",unsafe_allow_html=True)
    st.write('#####  Create a Streamlit web app and using technologies Pandas, PIL,plotly.express (px) libraries in imported  setup and running Features .')
    st.write('##### **Home** : Displays an overview of the app including technologies used and a brief description of the app. ')
    st.write('##### **Tableau** : This section allows the user to interact the data  with tableau user can understand the airbnb offers and travel and tourism data. Example : price prediction,locaton based insights and bedtype, roomtype, property type and rating(review score) then host name,host id and country to select and choose easly using this tableau visualization.')
    st.write('##### **Basic Overveiw** : its also like as tableau visulization but manly shows data top 10 and average informations.')
    st.write('##### **Data Visualization** and **Exploration** to visualize information also using  streamlit plots.')                  
    st.markdown("<h3 style='color:crimson;'>Conclusion:</h3>",unsafe_allow_html=True)
    st.write("##### I Created the project to used to detecting the  information to visualize the Tableau. ")
    st.write("##### It mostly  helped as customer knows about **Airbnb** price,locations,room,bed,prototype,country and host name,host id.. to easly interact with travel,tourism and other works.")
    st.write("##### Customer can easly choose our affortable country to select affortable price and  their rating(review_scores). to visualizing the tableau and seeing informations.")


