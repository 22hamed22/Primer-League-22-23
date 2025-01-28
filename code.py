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

# New color dictionary provided
team_colors = {
    'Man City': '#01D4D1',    
    'Arsenal': '#FA3737',    
    'Liverpool': '#D40108',    
    'Brighton & Hove Albion': '#0057B8',    
    'Tottenham Hotspur': '#132257',
    'Manchester United': '#FF5533',    
    'Newcastle United': '#241F20',    
    'Brentford': '#E20E0E',    
    'Aston Villa': '#92024A',    
    'Fulham': '#37010F',
    'Nottingham Forest': '#03F71D',    
    'West Ham United': '#7A263A',    
    'Leeds United': '#FFCD00',    
    'Leicester City': '#003090',    
    'Crystal Palace': '#1B458F',
    'AFC Bournemouth': '#660610',    
    'Chelsea': '#0408EE',    
    'Southampton': '#D71920',    
    'Wolverhampton Wanderers': '#EEDC04',    
    'Everton': '#003399'
}

# Create a color list based on the teams in the 'home' data
# Get unique team names from the dataset (combine home and away teams)
teams_in_data = pd.concat([df['team'], d['away team']]).unique()

# Assign colors to each team
team_colors_map = {team: team_colors.get(team, '#000000') for team in teams_in_data}

# Plotting the data using Plotly with each team having a different color
fig = px.bar(home.head(), 
             x=home.head().index, 
             y='Goal_For', 
             title='Top Teams by Goals Scored',
             color=home.head().index,  # Color by team name (index)
             color_discrete_map=team_colors_map)  # Use custom colors

# Display the chart in Streamlit
st.plotly_chart(fig)
