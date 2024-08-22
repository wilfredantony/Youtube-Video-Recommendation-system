import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import pickle
import boto3
import os

st.set_page_config(layout="wide")



# Setup the database connection
db_user = 'postgres'
db_password = 'your db password'
db_host = 'Your hostname'
db_port = '5432'
db_name = 'youtube'
connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_string)

# Load pre-trained models and vectorizers
with open('model.pkl', 'rb') as f: 
    model = pickle.load(f)
    
with open('vector.pkl', 'rb') as f: 
    vector = pickle.load(f)
    
with open('pca.pkl', 'rb') as f: 
    pca = pickle.load(f)

# Fetch data from AWS RDS
@st.cache_data
def fetch_data():
    query = "SELECT * FROM videos"
    df = pd.read_sql(query, engine)
    return df

df = fetch_data()


st.title("Wilfred's Youtube Replica")

# Sidebar for search
st.sidebar.header('Search Videos')
search_term = st.sidebar.text_input('Enter search term')

# Filter based on search term
if search_term:
    # Vectorize the search term
    search_vector = vector.transform([search_term])
    
    # Apply PCA transformation
    search_vector_pca = pca.transform(search_vector)
    
    # Predict the cluster using the PCA-transformed search vector
    cluster = model.predict(search_vector_pca)[0]
    
    # Filter the DataFrame based on the predicted cluster
    filtered_df = df[df['cluster'] == cluster]
else:
    filtered_df = df

# Grid layout for displaying videos
st.subheader('Video Results')

if not filtered_df.empty:
    num_columns = 4  # Number of columns in the grid
    rows = [filtered_df.iloc[i:i + num_columns] for i in range(0, len(filtered_df), num_columns)]
    
    for row in rows:
        cols = st.columns(num_columns)
        for i, video in enumerate(row.itertuples()):
            with cols[i]:
                st.image(video.thumbnail_url, use_column_width=True)
                st.markdown(f"**[{video.title}]({video.url})**")  # Clickable title
                st.write(video.description)
                st.write(f"**Tags:** {video.tags_joined}")
else:
    st.write("No videos found for the entered search term.")

