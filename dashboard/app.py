from nba_api.live.nba.endpoints import scoreboard
import json

def get_scoreboard():
    # Today's Score Board
    games = scoreboard.ScoreBoard()
    games_dict = games.get_dict()
    
    return games_dict


def lambda_handler(event, context):
    result = get_scoreboard()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }






