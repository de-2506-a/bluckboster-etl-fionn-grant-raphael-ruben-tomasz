import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from io import BytesIO
import plotly.graph_objects as go

st.sidebar.image("https://sdmntprpolandcentral.oaiusercontent.com/files/00000000-5c8c-620a-a2a0-12bb77c26765/raw?se=2025-08-13T14%3A37%3A44Z&sp=r&sv=2024-08-04&sr=b&scid=0022f377-9ad9-5a62-95dd-081dd166e4ba&skoid=71e8fa5c-90a9-4c17-827b-14c3005164d6&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-08-13T13%3A37%3A01Z&ske=2025-08-14T13%3A37%3A01Z&sks=b&skv=2024-08-04&sig=27FDBqipU0WfIBHM/pYRyE3Fd%2BN6MkZTSUQxCA%2BeBRw%3D", width=300)

st.header('BluckBoster')
st.markdown("""
    <hr style="border: 1px solid #ccc; margin: 20px 0;">
    """, unsafe_allow_html=True)

# # Load data
path = "../data/raw/"
df_film = pd.read_csv(path + "uncleaned_film.csv")
df_category = pd.read_csv(path + "uncleaned_category.csv")
df_film_category = pd.read_csv(path + "uncleaned_film_category.csv")
df_inventory = pd.read_csv(path + "uncleaned_inventory.csv")
df_rental = pd.read_csv(path + "uncleaned_rental.csv")
df_payment = pd.read_csv(path + "uncleaned_payment.csv")
df_customer = pd.read_csv(path + "uncleaned_customer.csv")
df_address = pd.read_csv(path + "uncleaned_address.csv")
df_city = pd.read_csv(path + "uncleaned_city.csv")
df_country = pd.read_csv(path + "uncleaned_country.csv")
df_actor = pd.read_csv(path + "uncleaned_actor.csv")
df_film_actor = pd.read_csv(path + "uncleaned_film_actor.csv")

df_film = df_film.drop(columns=['last_update'])
df_category = df_category.drop(columns=['last_update'])
df_film_category = df_film_category.drop(columns=['last_update'])
df_inventory = df_inventory.drop(columns=['last_update'])
df_rental = df_rental.drop(columns=['last_update'])
df_customer = df_customer.drop(columns=['last_update'])
df_address = df_address.drop(columns=['last_update'])
df_city = df_city.drop(columns=['last_update'])
df_country = df_country.drop(columns=['last_update'])
df_actor = df_actor.drop(columns=['last_update'])
df_film_actor = df_film_actor.drop(columns=['last_update'])


# Most popular film category by country
def get_most_popular_category_by_country():
    # Merge dataframes to get the necessary information
    merged_df = df_film.merge(df_film_category, on='film_id') \
                        .merge(df_category, on='category_id') \
                        .merge(df_inventory, on='film_id') \
                        .merge(df_rental, on='inventory_id') \
                        .merge(df_customer, on='customer_id') \
                        .merge(df_address, on='address_id') \
                        .merge(df_city, on='city_id') \
                        .merge(df_country, on='country_id')

    # Group by country and category to find the most popular category
    most_popular = merged_df.groupby(['country', 'name'])['rental_id'].count().reset_index()
    most_popular = most_popular.loc[most_popular.groupby('country')['rental_id'].idxmax()]

    return most_popular


# Most popular films rented
def get_most_popular_films():
    # Merge dataframes to get the necessary information
    merged_df = df_film.merge(df_film_category, on='film_id') \
                        .merge(df_category, on='category_id') \
                        .merge(df_inventory, on='film_id') \
                        .merge(df_rental, on='inventory_id') \
                        .merge(df_customer, on='customer_id')

    # Group by film to find the most popular films
    most_popular = merged_df.groupby('title')['rental_id'].count().reset_index()
    most_popular = most_popular.sort_values(by='rental_id', ascending=False).head(10)

    return most_popular


# Most popular actors by rental count
def get_most_popular_actors():
    # Merge dataframes to get the necessary information
    merged_df = df_film.merge(df_film_actor, on='film_id') \
                        .merge(df_actor, on='actor_id') \
                        .merge(df_inventory, on='film_id') \
                        .merge(df_rental, on='inventory_id') \

    # Group by actor to find the most popular actors and display their names
    most_popular = merged_df.groupby('actor_id')['rental_id'].count().reset_index()
    most_popular = most_popular.sort_values(by='rental_id', ascending=False).head(10)

    return most_popular


# Most popular films rented by month
def get_most_popular_films_by_month():
    # Merge dataframes to get the necessary information
    merged_df = df_film.merge(df_film_category, on='film_id') \
                        .merge(df_category, on='category_id') \
                        .merge(df_inventory, on='film_id') \
                        .merge(df_rental, on='inventory_id') \
                        .merge(df_customer, on='customer_id')

    # Convert rental date to datetime
    merged_df['rental_date'] = pd.to_datetime(merged_df['rental_date'])

    # Extract month and year from rental date
    merged_df['month_year'] = merged_df['rental_date'].dt.strftime('%Y-%m')

    # Group by month and film to find the most popular films by month
    most_popular = merged_df.groupby(['month_year', 'title'])['rental_id'].count().reset_index()
    most_popular = most_popular.loc[most_popular.groupby('month_year')['rental_id'].idxmax()]

    return most_popular

# Visualisations


# Visualisation 1: Most popular film category by country
most_popular_category = get_most_popular_category_by_country()
fig1 = px.bar(most_popular_category, 
                x='country', 
                y='rental_id', 
                color='name', 
                title='Most Popular Film Category by Country',
                labels={'rental_id': 'Number of Rentals', 'name': 'Film Category'})

fig1.update_layout(xaxis_title='Country', yaxis_title='Number of Rentals')
st.plotly_chart(fig1)

# Visualisation 5: chloropleth map of most popular film category in each country
most_popular_category = get_most_popular_category_by_country()
fig5 = px.choropleth(most_popular_category, 
                        locations='country', 
                        locationmode='country names',
                        color='name', 
                        title='Most Popular Film Category by Country',
                        color_continuous_scale=px.colors.sequential.Plasma)

fig5.update_layout(xaxis_title='Country', yaxis_title='Film Category')
st.plotly_chart(fig5)

# Visualisation 2: Most popular films rented
most_popular_films = get_most_popular_films()
fig2 = px.bar(most_popular_films, 
                x='title', 
                y='rental_id', 
                title='Most Popular Films Rented',
                labels={'rental_id': 'Number of Rentals', 'title': 'Film Title'})

fig2.update_layout(xaxis_title='Film Title', yaxis_title='Number of Rentals')
st.plotly_chart(fig2)

# Visualisation 3: Most popular actors by rental count and display their first name and last name combined
# st.subheader("Most Popular Actors by Rental Count")
# most_popular_actors = get_most_popular_actors()
# most_popular_actors['actor_name'] = most_popular_actors['first_name'] + ' ' + most_popular_actors['last_name']
# fig3 = px.bar(most_popular_actors, 
#                 x='actor_name', 
#                 y='rental_id', 
#                 title='Most Popular Actors by Rental Count',
#                 labels={'rental_id': 'Number of Rentals', 'actor_name': 'Actor Name'})
# fig3.update_layout(xaxis_title='Actor Name', yaxis_title='Number of Rentals')
# st.plotly_chart(fig3)

# Visualisation 4: Most popular films rented by month
most_popular_films_by_month = get_most_popular_films_by_month()
fig4 = px.bar(most_popular_films_by_month, 
            x='month_year', 
            y='rental_id', 
            color='title', 
            title='Most Popular Films Rented by Month',
            labels={'rental_id': 'Number of Rentals', 'title': 'Film Title'})  
fig4.update_layout(xaxis_title='Month-Year', yaxis_title='Number of Rentals')
st.plotly_chart(fig4)
