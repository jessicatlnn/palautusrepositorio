from index import PlayerReader, PlayerStats

URL = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
stats = PlayerStats(PlayerReader(URL))

for p in stats.top_scorers_by_team("DAL"):
    print(p)
