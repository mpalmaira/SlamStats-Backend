from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

# Retrieve player stats for the current season
player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season='2023-24').get_data_frames()[0]

print(player_stats)

# Group the player stats by team
team_stats = player_stats.groupby('TEAM_ABBREVIATION')

# Get the season leader for each team
season_leaders = {}
for team, stats in team_stats:
    leader = stats.loc[stats['PTS'].idxmax()]  # Change 'PTS' to the desired statistic (e.g., points, assists, rebounds, etc.)
    season_leaders[team] = leader

# Convert the dictionary to a DataFrame for better readability
season_leaders_df = pd.DataFrame(season_leaders).T
print(season_leaders_df)
