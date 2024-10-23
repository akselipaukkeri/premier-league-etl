import logging
import pandas as pd


class Transformer:
    def __init__(self):
        pass

    def transform(self, data: list) -> pd.DataFrame:
        df = pd.DataFrame(data)

        # Lets take only needed cols, exception in case API has changed
        try:
            df = df[["name", "position", "team", "dateOfBirth", "nationality"]]
        except KeyError as e:
            logging.error("KeyError, not found following: " + str(e))

        return df
