from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import teamestimatedmetrics
from nba_api.stats.endpoints import teamdashlineups
from nba_api.live.nba.endpoints import boxscore

import json

def get_scoreboard():
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    games_dict = games.get_dict()
    
    return games_dict

def teamEstimatedMetrics():
    # Today's Score Board
    games = teamestimatedmetrics.TeamEstimatedMetrics()
    rowSet = games.get_dict()['resultSet']['rowSet']
    team_info = []
    for team in rowSet:
        team_info.append({'teamId': team[0], "win_percentage": team[5]})

    return team_info

def teamDashLineups():
    games = teamdashlineups.TeamDashLineups('1610612751')
    return games.get_normalized_json()

def boxScore():
    score = boxscore.BoxScore('0022300717')
    print(score.get_dict())
    return score




def lambda_handler(event, context):
    result = get_scoreboard()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

print(teamDashLineups())





