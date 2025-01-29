import pandas as pd
import plotly.express as px
import streamlit as st

# HTML header with inline CSS for Streamlit
header_html = """
<div style="background-color: #FFFFFF; color: #470B63; padding: 20px; font-size: 45px; display: flex; align-items: center; text-align: center;">
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" width="300" style="float: left;">
    <span style="margin: auto; font-weight: bold;">Analysis of the Premier League season 2022-2023</span>
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" width="300" style="float: right;">
</div>
"""
# Display the header using Streamlit
st.markdown(header_html, unsafe_allow_html=True)

# Load the data
df = pd.read_csv('premier_league_df.csv')[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]

# Rename columns for consistency
df.rename(columns={'HomeTeam': 'home team', 'AwayTeam': 'away team', 'FTHG': 'Goal_For', 'FTAG': 'Goal_Against'}, inplace=True)

# Standardize team names
team_name_mapping = {
    'Man City': 'Manchester City', 'Tottenham': 'Tottenham Hotspur', 'West Ham': 'West Ham United', 
    'Leicester': 'Leicester City', 'Crystal Palace': 'Crystal Palace', 'Aston Villa': 'Aston Villa',
    'Nottingham Forest': 'Nottingham Forest', 'Brighton': 'Brighton & Hove Albion', 'Fulham': 'Fulham', 
    'Chelsea': 'Chelsea', 'Liverpool': 'Liverpool', 'Southampton': 'Southampton', 'Everton': 'Everton',
    'Leeds': 'Leeds United', 'Brentford': 'Brentford', 'Bournemouth': 'AFC Bournemouth', 'Arsenal': 'Arsenal', 
    'Manchester United': 'Manchester United', 'Newcastle': 'Newcastle United', 'Wolverhampton': 'Wolverhampton Wanderers'
}
df['team'] = df['home team'].replace(team_name_mapping)

# Group data by team and calculate statistics
team_stats = df.groupby('team').sum()
team_stats['Goal_Difference'] = team_stats['Goal_For'] - team_stats['Goal_Against']
home_stats = team_stats.sort_values('Goal_For', ascending=False)

# Define team colors
team_colors = {
    'Manchester City': '#01D4D1', 'Arsenal': '#FA3737', 'Liverpool': '#D40108', 'Brighton & Hove Albion': '#0057B8',
    'Tottenham Hotspur': '#132257', 'Manchester United': '#FF5533', 'Newcastle United': '#241F20', 'Brentford': '#E20E0E',
    'Aston Villa': '#92024A', 'Fulham': '#37010F', 'Nottingham Forest': '#03F71D', 'West Ham United': '#7A263A',
    'Leeds United': '#FFCD00', 'Leicester City': '#003090', 'Crystal Palace': '#1B458F', 'AFC Bournemouth': '#660610',
    'Chelsea': '#0408EE', 'Southampton': '#D71920', 'Wolverhampton Wanderers': '#EEDC04', 'Everton': '#003399'
}

# Prepare color mapping for plot
team_colors_map = {team: team_colors.get(team, '#000000') for team in team_stats.index}

# Plot Top Teams by Goals Scored
fig = px.bar(home_stats.head(), x=home_stats.head().index, y='Goal_For', title='Top Teams by Goals Scored',
             color=home_stats.head().index, color_discrete_map=team_colors_map)
st.plotly_chart(fig)

# Plot Total Goals Scored
fig_total_for = px.bar(team_stats.sort_values('Goal_For', ascending=False), x=team_stats.index, y='Goal_For',
                       title='Total Goals Scored by Each Team', color=team_stats.index, color_discrete_map=team_colors_map)
st.plotly_chart(fig_total_for)

# Plot Total Goals Conceded
fig_total_against = px.bar(team_stats.sort_values('Goal_Against', ascending=False), x=team_stats.index, y='Goal_Against',
                           title='Total Goals Conceded by Each Team', color=team_stats.index, color_discrete_map=team_colors_map)
st.plotly_chart(fig_total_against)

# Plot Goal Difference
fig_goal_diff = px.bar(team_stats.sort_values('Goal_Difference', ascending=False), x=team_stats.index, y='Goal_Difference',
                       title='Goal Difference by Each Team', color=team_stats.index, color_discrete_map=team_colors_map)
st.plotly_chart(fig_goal_diff)

# Plot Home Goals Scored
fig_home_goals = px.bar(df.groupby('team').sum()['Goal_For'].sort_values(ascending=False), x=df.groupby('team').sum().index, y='Goal_For',
                        title='Goals Scored by Each Team at Home', color=df.groupby('team').sum().index, color_discrete_map=team_colors_map)
st.plotly_chart(fig_home_goals)

# Plot Away Goals Scored
fig_away_goals = px.bar(df.groupby('team').sum()['Goal_Against'].sort_values(ascending=False), x=df.groupby('team').sum().index, y='Goal_Against',
                        title='Goals Scored by Each Team Away from Home', color=df.groupby('team').sum().index, color_discrete_map=team_colors_map)
st.plotly_chart(fig_away_goals)
