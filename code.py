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

# Load the data
d = pd.read_csv('premier_league_df.csv')

# Renaming columns for consistency with the expected column names
d.rename(columns={'HomeTeam': 'home team', 'AwayTeam': 'away team'}, inplace=True)

# Proceed with the existing code to process the data
d = d[['home team', 'away team', 'FTHG', 'FTAG']]
df = d.copy()

df.rename(columns={'home team': 'team'}, inplace=True)
df.rename(columns={'FTHG': 'Goal_For'}, inplace=True)
df.rename(columns={'FTAG': 'Goal_Against'}, inplace=True)

# Standardizing team names to match the team_colors dictionary
team_name_mapping = {
    'Man City': 'Manchester City',
    'Tottenham': 'Tottenham Hotspur',
    'West Ham': 'West Ham United',
    'Leicester': 'Leicester City',
    'Crystal Palace': 'Crystal Palace',
    'Aston Villa': 'Aston Villa',
    'Nottingham Forest': 'Nottingham Forest',
    'Brighton': 'Brighton & Hove Albion',
    'Fulham': 'Fulham',
    'Chelsea': 'Chelsea',
    'Liverpool': 'Liverpool',
    'Southampton': 'Southampton',
    'Everton': 'Everton',
    'Leeds': 'Leeds United',
    'Brentford': 'Brentford',
    'Bournemouth': 'AFC Bournemouth',
    'Arsenal': 'Arsenal',
    'Manchester United': 'Manchester United',
    'Newcastle': 'Newcastle United',
    'Wolverhampton': 'Wolverhampton Wanderers'
}

# Apply the name mapping
df['team'] = df['team'].replace(team_name_mapping)

# Grouping and sorting the data
mean_values = df.groupby('team').sum('Goal_For')
home = mean_values.sort_values('Goal_For', ascending=False)

# Display the top teams based on goals scored
st.write("Top teams based on total goals scored:")
st.write(home.head())

# Define team colors (these are your team-color pairs)
team_colors = {
    'Manchester City': '#01D4D1',    
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

# Extract the teams that appear in your dataset, both home and away
teams_in_data = pd.concat([df['team'], d['away team']]).unique()

# Match the dataset team names with the team_colors dictionary
team_colors_map = {team: team_colors.get(team, '#000000') for team in teams_in_data}

# Plotting the data using Plotly with each team having a different color
fig = px.bar(home.head(), 
             x=home.head().index, 
             y='Goal_For', 
             title='Top Teams by Goals Scored', 
             color=home.head().index,  # Color by team name (index)
             color_discrete_map=team_colors_map)  # Use custom colors for each team

# Show the plot in Streamlit
st.plotly_chart(fig)

# Plotting the 'Total_Goal_For' and 'Total_Goal_Against' for additional insights
# Group by 'team' and sum 'Goal_For' and 'Goal_Against' for total goals
total_goals = df.groupby('team').sum()

# Total Goals Scored (Total_Goal_For) in descending order
fig_total_for = px.bar(total_goals.sort_values('Goal_For', ascending=False), 
                       x=total_goals.sort_values('Goal_For', ascending=False).index, 
                       y='Goal_For', 
                       title='Total Goals Scored by Each Team (Descending)', 
                       color=total_goals.sort_values('Goal_For', ascending=False).index,  # Color by team name (index)
                       color_discrete_map=team_colors_map)  # Use custom colors
st.plotly_chart(fig_total_for)

# Total Goals Conceded (Total_Goal_Against) in descending order
fig_total_against = px.bar(total_goals.sort_values('Goal_Against', ascending=False), 
                           x=total_goals.sort_values('Goal_Against', ascending=False).index, 
                           y='Goal_Against', 
                           title='Total Goals Conceded by Each Team (Descending)', 
                           color=total_goals.sort_values('Goal_Against', ascending=False).index,  # Color by team name (index)
                           color_discrete_map=team_colors_map)  # Use custom colors
st.plotly_chart(fig_total_against)

# Add the 'Goal Difference' plot
# Calculate goal difference (Goals For - Goals Against)
total_goals['Goal_Difference'] = total_goals['Goal_For'] - total_goals['Goal_Against']

# Goal Difference plot
fig_goal_diff = px.bar(total_goals.sort_values('Goal_Difference', ascending=False), 
                       x=total_goals.sort_values('Goal_Difference', ascending=False).index, 
                       y='Goal_Difference', 
                       title='Goal Difference by Each Team', 
                       color=total_goals.sort_values('Goal_Difference', ascending=False).index,  # Color by team name (index)
                       color_discrete_map=team_colors_map)  # Use custom colors
st.plotly_chart(fig_goal_diff)

# Add the 'Goal_For_Home' plot
# Calculate total goals scored at home
home_goals = df.groupby('team').sum()['Goal_For']  # Home goals are 'Goal_For' in the home team data

# Home Goals plot
fig_home_goals = px.bar(home_goals.sort_values(ascending=False), 
                        x=home_goals.sort_values(ascending=False).index, 
                        y=home_goals.sort_values(ascending=False), 
                        title='Goals Scored by Each Team at Home', 
                        color=home_goals.sort_values(ascending=False).index,  # Color by team name (index)
                        color_discrete_map=team_colors_map)  # Use custom colors
st.plotly_chart(fig_home_goals)

# Add the 'Goal_For_Away' plot
# Calculate total goals scored away
away_goals = df.groupby('team').sum()['Goal_Against']  # Away goals are 'Goal_Against' for away teams

# Away Goals plot
fig_away_goals = px.bar(away_goals.sort_values(ascending=False), 
                        x=away_goals.sort_values(ascending=False).index, 
                        y=away_goals.sort_values(ascending=False), 
                        title='Goals Scored by Each Team Away from Home', 
                        color=away_goals.sort_values(ascending=False).index,  # Color by team name (index)
                        color_discrete_map=team_colors_map)  # Use custom colors
st.plotly_chart(fig_away_goals)
