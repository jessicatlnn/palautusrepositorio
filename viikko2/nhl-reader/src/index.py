import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN:")

    finnish_players = []
    for player in players:
        if player.nationality == "FIN":
            finnish_players.append(player)
    
    sorted_players = sorted(finnish_players, key=lambda player: player.goals + player.assists, reverse=True)

    for player in sorted_players[:5]:
        print(player)


if __name__ == "__main__":
    main()
