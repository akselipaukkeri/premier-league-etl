from dotenv import load_dotenv
from src.PL_ETL.ETL import etl_process
import os
import logging


def main():

    logging.info("Starting ETL process")
    
    load_dotenv()
    api_key = os.getenv("API_KEY")
    teams_url = os.getenv("TEAMS_URL")
    file_name = os.getenv("FILE_NAME")

    # TODO: try-except logic here?
    
    extractor = etl_process.PremierLeagueAPIExtractor(teams_url, api_key)
    data = etl_process.PremierLeagueAPIExtractor.extract(extractor)

    transformer = etl_process.PremierLeagueTransformer(data)
    transformed_data = etl_process.PremierLeagueTransformer.transform(transformer)

    csvloader = etl_process.CSVLoader(file_name, transformed_data)
    etl_process.CSVLoader.load(csvloader)

    logging.info("ETL done!")


if __name__ == "__main__":
    main()
