import requests
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")


class PremierLeagueAPIExtractor:
    def __init__(self, teams_url: str, api_key: str):
        self.teams_url = teams_url
        self.api_key = api_key

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


class PremierLeagueTransformer:
    def __init__(self, data: list):
        self.data = data

    def transform(self) -> pd.DataFrame:
        df = pd.DataFrame(self.data)

        # Lets take only needed cols, exception in case API has changed
        try:
            df = df[["name", "position", "team", "dateOfBirth", "nationality"]]
        except KeyError as e:
            logging.error("KeyError, not found following: " + str(e))

        return df


class CSVLoader:
    def __init__(self, file_path: str, data: pd.DataFrame):
        self.file_path = file_path
        self.data = data

    def load(self):
        try:
            self.data.to_csv(self.file_path, index=False)
            logging.info(f"File loaded to root with name: {self.file_path}")

        except Exception as e:
            logging.error("Failed to produce CSV file: " + str(e))
            raise
