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
# Display the HTML header using Streamlit
st.markdown(html_code, unsafe_allow_html=True)

# Load the data
d = pd.read_csv('premier_league_df.csv')

# Display the columns to check for mismatches
st.write("Columns in the dataset:")
st.write(d.columns)

# Strip any extra spaces from the column names
d.columns = d.columns.str.strip()

# Check if all expected columns are present
expected_columns = ['home team', 'away team', 'FTHG', 'FTAG']
missing_columns = [col for col in expected_columns if col not in d.columns]

# If any columns are missing, show an error
if missing_columns:
    st.error(f"Missing columns: {', '.join(missing_columns)}")
else:
    # Proceed with data processing
    d = d[expected_columns]
    df = d.copy()

    # Renaming columns for clarity
    df.rename(columns={'home team': 'team'}, inplace=True)
    df.rename(columns={'FTHG': 'Goal_For'}, inplace=True)
    df.rename(columns={'FTAG': 'Goal_Against'}, inplace=True)

    # Grouping and sorting the data
    mean_values = df.groupby('team').sum('Goal_For')
    home = mean_values.sort_values('Goal_For', ascending=False)

    # Display the top teams based on goals scored
    st.write("Top teams based on total goals scored:")
    st.write(home.head())

    # Plotting the data using Plotly
    fig = px.bar(home.head(), x=home.head().index, y='Goal_For', title='Top Teams by Goals Scored')
    st.plotly_chart(fig)
