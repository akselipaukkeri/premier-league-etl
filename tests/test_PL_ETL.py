import unittest
import sys
import os
import pandas as pd

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PL_ETL.ETL import etl_process


class TestPremierLeagueTransformer(unittest.TestCase):
    # unittest requires setUp function, cannot be renamed
    def setUp(self):

        # Sample correct data
        self.sample_data = [
            {
                "name": "Rasmus Hojlund",
                "position": "Forward",
                "team": "Manchester United",
                "dateOfBirth": "2000-01-01",
                "nationality": "Denmark",
            },
            {
                "name": "Player 2",
                "position": "Midfielder",
                "team": "Team B",
                "dateOfBirth": "1992-02-02",
                "nationality": "Country B",
            },
        ]

        # Example of incorrect data (missing position and nationality)
        self.missing_columns_data = [
            {"name": "Player 3", "team": "Team C", "dateOfBirth": "1993-03-03"}
        ]

    def test_transform_success(self):
        """Test if the transform function works as expected with correct data."""
        self.transformer = etl_process.PremierLeagueTransformer(self.sample_data)
        df = self.transformer.transform()
        self.assertIsInstance(df, pd.DataFrame)

        expected_columns = ["name", "position", "team", "dateOfBirth", "nationality"]
        self.assertListEqual(list(df.columns), expected_columns)

        # Random checks for each row
        self.assertEqual(df.iloc[0]["name"], "Rasmus Hojlund")
        self.assertEqual(df.iloc[1]["position"], "Midfielder")

    def test_transform_key_error(self):
        """Test if missing cols are handled as expected with KeyError."""
        self.transformer = etl_process.PremierLeagueTransformer(
            self.missing_columns_data
        )
        with self.assertLogs(level="INFO") as cm:
            df = self.transformer.transform()

        self.assertTrue(any("KeyError" in message for message in cm.output))

        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue("name" in df.columns)
        self.assertFalse("position" in df.columns)


if __name__ == "__main__":
    unittest.main()
