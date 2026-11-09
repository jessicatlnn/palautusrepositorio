import requests
from player import Player
from rich.console import Console
from rich.table import Table

def main():
    season = input("Season: ")
    nationality = input("Nationality: ")

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"

    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)

    console = Console()

    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Released", style="cyan")
    table.add_column("teams", style="magenta")
    table.add_column("goals", style="green")
    table.add_column("assists", style="green")
    table.add_column("points", style="green")

    for player in players:
        points = player.goals + player.assists

        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(points)
        )
    
    console.print(table)


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        players = []
    
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        
        return players


class PlayerStats():
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        nationality_players = []

        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)
        
        sorted_players = sorted(nationality_players, key=lambda player: player.goals + player.assists, reverse=True)

        return sorted_players


if __name__ == "__main__":
    main()
