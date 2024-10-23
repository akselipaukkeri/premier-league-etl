import pandas as pd
import logging


class Loader:

    def load(self, data: pd.DataFrame, file_path: str):
        try:
            data.to_csv(file_path, index=False)
            logging.info(f"Data loaded to {file_path}")

        except Exception as e:
            logging.error("Failed to produce CSV file: " + str(e))
