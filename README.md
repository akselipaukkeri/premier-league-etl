# Premier League ETL Project

This project extracts, transforms, and loads data from the Premier League API. The data includes teams and players, and it is saved to a CSV file for further analysis. The project also contains script for
analyzing the data which can be used as a template.

Link to the API: https://www.football-data.org/documentation/quickstart

## Project Overview

This project follows an ETL structure:

- **Extractor**: Fetches team and player data from the Premier League API.
- **Transformer**: Processes and cleans the extracted data.
- **Loader**: Saves the cleaned data into a CSV file.

In addition, it provides sample data analysis for further development.

## Features

- Extracts team and player data from the Premier League API.
- Transforms data to extract useful player information such as names, positions, and nationalities.
- Saves the transformed data to a CSV file.
- Provide a sample data analysis file for further analysis 

## Prerequisites

Make sure you have the following installed:

- Python 3.9+
- virtualenv

### Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/akselipaukkeri/premier-league-etl.git
    cd premier-league-etl
    ```

2. **Create and activate the virtual environment**:

   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **macOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```
    The requirements.txt includes the installation of this project as a package, hence the -e. in the file.

4. **Environment Variables**:

The project requires certain environment variables to be set in a `.env` file for API requests and data output. These variables include:

- **API_KEY**: Your Premier League API key.
- **TEAMS_URL**: The URL endpoint for fetching team data from the Premier League API.
- **FILE_NAME**: The name of the CSV file where the data will be saved.

**Example `.env` file**

Create a `.env` file in the root directory of the project with the following content:

```plaintext
API_KEY=your_api_key
TEAMS_URL='https://api.football-data.org/v4/competitions/PL/teams' 
FILE_NAME=premier_league_data.csv
```

5. **Run unit tests**:

   ```bash
   python -m unittest discover -s tests
   ```

6. **Run ETL pipeline**:

    ```bash
    python main.py
    ```

### Running the Additional Data Analysis

There is simple data analysis script which can be ran by following command.
It produces a .html file with plotly about players in premier league per country.

```bash
python main_analysis.py
