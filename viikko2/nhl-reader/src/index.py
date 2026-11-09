import requests
from rich.console import Console
from rich.table import Table
from player import Player


def get_players_by_nationality(nationality):
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    return players


def get_players_by_team(team):
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_team(team)
    return players


def select_players(nationality):
    if nationality:
        return get_players_by_nationality(nationality), "nationality", nationality

    team = input("Team: ")
    return get_players_by_team(team), "team", team


def create_table(table):
    table.add_column("Released", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", style="green")
    table.add_column("assists", style="green")
    table.add_column("points", style="green")

def add_players_to_table(table, players):
    for player in players:
        points = player.goals + player.assists

        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points)
        )

def main():
    season = input("Season: ")
    nationality = input("Nationality (leave empty to search by team): ")
    players, filter_type, filter_name = select_players(nationality)

    console = Console()

    table = Table(title=f"Season {season} players from {filter_type} {filter_name}")
    create_table(table)
    add_players_to_table(table, players)

    console.print(table)


class PlayerReader:

    # pylint: disable=too-few-public-methods

    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players


class PlayerStats():

    # pylint: disable=too-few-public-methods

    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        nationality_players = []

        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)

        sorted_players = sorted(nationality_players, key=lambda player:
                                player.goals + player.assists, reverse=True)

        return sorted_players

    def top_scorers_by_team(self, team):
        players = self.reader.get_players()
        team_players = []

        for player in players:
            if player.team == team:
                team_players.append(player)

        sorted_players = sorted(team_players, key=lambda player:
                                player.goals + player.assists, reverse=True)

        return sorted_players

    def top_goal_scorers(self, how_many):
        players = self.reader.get_players()
        sorted_players = sorted(players, key=lambda player: player.goals, reverse=True)
        return sorted_players[:how_many]


if __name__ == "__main__":
    main()
