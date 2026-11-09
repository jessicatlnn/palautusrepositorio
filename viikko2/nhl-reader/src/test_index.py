import unittest

# pylint: disable=too-few-public-methods

from index import PlayerStats
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Player One",
                "nationality": "FIN",
                "assists": 10,
                "goals": 20,
                "team": "DAL",
                "games": 80,
                "id": 1
            }),
            Player({
                "name": "Player Two",
                "nationality": "FIN",
                "assists": 30,
                "goals": 5,
                "team": "DAL",
                "games": 80,
                "id": 2
            }),
            Player({
                "name": "Player Three",
                "nationality": "SWE",
                "assists": 15,
                "goals": 15,
                "team": "NYR",
                "games": 80,
                "id": 3
            })
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Player Two", "Player One"]
        )

    def test_top_scorers_by_nationality_returns_empty_list_if_not_found(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(players, [])

    def test_top_scorers_by_team_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_team("DAL")

        self.assertEqual(
            [player.name for player in players],
            ["Player Two", "Player One"]
        )

    def test_top_scorers_by_team_returns_empty_list_if_not_found(self):
        players = self.stats.top_scorers_by_team("BOS")

        self.assertEqual(players, [])

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(
            [player.name for player in players],
            ["Player One", "Player Three"]
        )
