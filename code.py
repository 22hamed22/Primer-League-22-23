import pandas as pd
import plotly.express as px
import streamlit as st

# Streamlit header HTML
st.markdown("""
<div style="background-color: #FFFFFF; color: #470B63; padding: 20px; font-size: 45px; display: flex; align-items: center; text-align: center;">
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" width="300" style="float: left;">
    <span style="margin: auto; font-weight: bold;">Premier League 2022-2023 Analysis</span>
    <img src="https://logowik.com/content/uploads/images/premier-league-lion8499.jpg" width="300" style="float: right;">
</div>
""", unsafe_allow_html=True)

# Load and preprocess data
df = pd.read_csv('premier_league_df.csv')[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
df.rename(columns={'HomeTeam': 'team', 'FTHG': 'Goal_For', 'FTAG': 'Goal_Against'}, inplace=True)
df['team'] = df['team'].replace({
    'Man City': 'Manchester City', 'Tottenham': 'Tottenham Hotspur', 'West Ham': 'West Ham United',
    'Leicester': 'Leicester City', 'Crystal Palace': 'Crystal Palace', 'Aston Villa': 'Aston Villa',
    'Nottingham Forest': 'Nottingham Forest', 'Brighton': 'Brighton & Hove Albion', 'Fulham': 'Fulham',
    'Chelsea': 'Chelsea', 'Liverpool': 'Liverpool', 'Southampton': 'Southampton', 'Everton': 'Everton',
    'Leeds': 'Leeds United', 'Brentford': 'Brentford', 'Bournemouth': 'AFC Bournemouth', 'Arsenal': 'Arsenal',
    'Manchester United': 'Manchester United', 'Newcastle': 'Newcastle United', 'Wolverhampton': 'Wolverhampton Wanderers'
})

# Team color dictionary
team_colors = {
    'Manchester City': '#01D4D1', 'Arsenal': '#FA3737', 'Liverpool': '#D40108', 'Brighton & Hove Albion': '#0057B8',
    'Tottenham Hotspur': '#132257', 'Manchester United': '#FF5533', 'Newcastle United': '#241F20', 'Brentford': '#E20E0E',
    'Aston Villa': '#92024A', 'Fulham': '#37010F', 'Nottingham Forest': '#03F71D', 'West Ham United': '#7A263A',
    'Leeds United': '#FFCD00', 'Leicester City': '#003090', 'Crystal Palace': '#1B458F', 'AFC Bournemouth': '#660610',
    'Chelsea': '#0408EE', 'Southampton': '#D71920', 'Wolverhampton Wanderers': '#EEDC04', 'Everton': '#003399'
}

# Plot team statistics
def plot_team_stats(data, title, color_column, y_column):
    fig = px.bar(data, x=data.index, y=y_column, title=title, color=color_column,
                 color_discrete_map=team_colors)
    st.plotly_chart(fig)

# Group by team and compute relevant stats
total_goals = df.groupby('team').sum()
home_goals = total_goals['Goal_For']

# Plot various statistics
plot_team_stats(home_goals.sort_values(ascending=False), 'Goals Scored by Each Team', home_goals.index, 'Goal_For')
plot_team_stats(total_goals['Goal_Against'].sort_values(ascending=False), 'Goals Conceded by Each Team', total_goals['Goal_Against'].index, 'Goal_Against')
plot_team_stats((total_goals['Goal_For'] - total_goals['Goal_Against']).sort_values(ascending=False), 'Goal Difference by Each Team', (total_goals['Goal_For'] - total_goals['Goal_Against']).index, 'Goal_Difference')

# Home and Away Goals
home_goals = df[df['team'] == df['team']]['Goal_For']
away_goals = df[df['team'] != df['team']]['Goal_For']

plot_team_stats(home_goals.sort_values(ascending=False), 'Home Goals Scored by Each Team', home_goals.index, 'Goal_For')
plot_team_stats(away_goals.sort_values(ascending=False), 'Away Goals Scored by Each Team', away_goals.index, 'Goal_For')
