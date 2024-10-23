import requests
import logging


class Extractor:
    def __init__(self, teams_url):
        self.teams_url = teams_url

    def extract(self) -> list:
        headers = {"X-Auth-Token": self.api_key}

        response = requests.get(self.teams_url, headers=headers)
        if response.status_code != 200:
            if response.status_code == 429:
                logging.error("Statuscode is 429. Check rate limits.")
                raise
            else:
                logging.error(
                    f"Failed to fetch teams, Status code: {response.status_code}"
                )
                raise

        teams_data = response.json()
        all_players = []

        for team in teams_data["teams"]:
            team_name = team["name"]
            players = team.get("squad", [])
            for player in players:
                player["team"] = team_name
                all_players.append(player)

        return all_players
