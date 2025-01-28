import pandas as pd
import plotly.express as px
import streamlit as st

# HTML content with inline CSS for Streamlit header
html_code = """
<div class="h1" style="background-color: #FFFFFF; color: #470B63; padding: 20px; font-size: 45px; max-width: 3500px; margin: auto; margin-top: 50px; display: flex; align-items: center; text-align: center; text-shadow: 1px 1px 1px #13A7AC;">
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" alt="Image" width="300" style="float: left;">
    <span style="margin: auto; font-weight: bold;">Analysis of the Premier League season 2022-2023</span>
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" alt="Image" width="300" style="float: right;">
</div>
"""
# Display the HTML header using Streamlit
st.markdown(html_code, unsafe_allow_html=True)

# Load the data (use your actual CSV file location here)
d = pd.read_csv('premier_league_df.csv')

# Renaming columns for consistency with the expected column names
d.rename(columns={'HomeTeam': 'home team', 'AwayTeam': 'away team'}, inplace=True)

# Proceed with the existing code to process the data
d = d[['home team', 'away team', 'FTHG', 'FTAG']]
df = d.copy()

df.rename(columns={'home team': 'team'}, inplace=True)
df.rename(columns={'FTHG': 'Goal_For'}, inplace=True)
df.rename(columns={'FTAG': 'Goal_Against'}, inplace=True)

# Grouping and sorting the data
mean_values = df.groupby('team').sum('Goal_For')
home = mean_values.sort_values('Goal_For', ascending=False)

# Display the top teams based on goals scored
st.write("Top teams based on total goals scored:")
st.write(home.head())

# Define custom colors for the teams
team_colors = {
    'Arsenal': 'red',  # RAL 3000 - Flame red
    'Manchester City': '#5CA9E1',  # Manchester City Sky Blue (Hex: #5CA9E1)
    'Manchester United': 'darkred',  # RAL 3003 - Ruby red
    'Chelsea': 'blue',  # RAL 5005 - Signal blue
    'Liverpool': 'crimson',  # RAL 3004 - Purple red
    'Tottenham Hotspur': 'navy',  # RAL 5003 - Sapphire blue
    'Newcastle United': 'black',  # RAL 9005 - Jet black
    'West Ham United': 'claret',  # RAL 3007 - Black red
    'Aston Villa': 'violet',  # RAL 4006 - Traffic violet
    'Leicester City': 'green',  # RAL 6000 - Patina green
    'Brighton & Hove Albion': 'lightgreen',  # RAL 6027 - Light green
    'Crystal Palace': 'blueviolet',  # RAL 4005 - Blue lilac
}

# Plotting the data using Plotly with each team having a different color
fig = px.bar(home.head(), 
             x=home.head().index, 
             y='Goal_For', 
             title='Top Teams by Goals Scored',
             color=home.head().index,  # Color by team name (index)
             color_discrete_map=team_colors)  # Use custom colors

# Display the chart in Streamlit
st.plotly_chart(fig)
