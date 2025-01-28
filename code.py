import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs as go

# HTML content with inline CSS
html_code = """
<div class="h1" style="background-color: #FFFFFF; color: #470B63; padding: 20px; font-size: 45px; max-width: 3500px; margin: auto; margin-top: 50px; display: flex; align-items: center; text-align: center; text-shadow: 1px 1px 1px #13A7AC;">
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" alt="Image" width="300" style="float: left;">
    <span style="margin: auto; font-weight: bold;">Analysis of the Premier League season 2022-2023</span>
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" alt="Image" width="300" style="float: right;">
</div>
"""

# Read the dataset (you can use your local CSV or load it from a file)
# Make sure you replace this with the correct path to your CSV
d = pd.read_csv('data/premier_league_df.csv')


# Display the HTML content
st.markdown(html_code, unsafe_allow_html=True)

# Data processing
d = d[['home team', 'away team', 'FTHG', 'FTAG']]
df = d.copy()

# Renaming columns
df.rename(columns={'home team': 'team'}, inplace=True)
df.rename(columns={'FTHG': 'Goal_For'}, inplace=True)
df.rename(columns={'FTAG': 'Goal_Against'}, inplace=True)

# Grouping and summing by team
mean_values = df.groupby('team').sum()

# Sorting teams based on the goals scored (Goal_For)
home = mean_values.sort_values('Goal_For', ascending=False)

# Display the top teams with highest goals scored in the Streamlit app
st.write("Top teams based on total goals scored:")
st.write(home.head())

# You can also visualize this data using Plotly
fig = px.bar(home.head(), x=home.head().index, y='Goal_For', title='Top Teams by Goals Scored')
st.plotly_chart(fig)
