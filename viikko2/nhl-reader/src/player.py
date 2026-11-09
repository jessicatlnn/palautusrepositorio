class Player:

    # pylint: disable=too-few-public-methods

    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']
        self.id = player_dict['id']

    def __str__(self):
        return f"{self.name}, team {self.nationality} points {self.goals + self.assists}"
