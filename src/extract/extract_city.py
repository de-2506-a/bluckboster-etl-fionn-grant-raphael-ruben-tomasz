import os
import pandas as pd
import timeit
import psycopg2
from config.db_config import load_db_config


def extract_city() -> pd.DataFrame:
    
    start_time = timeit.default_timer()
    
    try:
        # Load config to get connection details
        connection_details = load_db_config()["source_database"]
        # Connect to Database
        connection = psycopg2.connect(
            dbname=connection_details["dbname"],
            user=connection_details["user"],
            password=connection_details["password"],
            host=connection_details["host"],
            port=connection_details["port"]
        )
        # Read SQL query
        EXTRACT_CITY_QUERY_FILE = os.path.join(

            os.path.dirname(__file__),
            '..', '..', 'sql', 'extract_city.sql'

        )
        with open(EXTRACT_CITY_QUERY_FILE, "r") as file:
            query = file.read()
        # Run Query and store into a DataFrame
        city_df = pd.read_sql_query(query,connection)
        connection.close()
        extract_city_execution_time = (
            timeit.default_timer() - start_time
            )
        #Print successful extraction
        print(f"Extracted city table in {extract_city_execution_time} seconds")
        city_df.to_csv(r"data\raw\uncleaned_city.csv", index= False)
        return city_df
    # Print unsuccessful extraction
    except Exception as e:
        print(f"Failed to extract data: {e}")
        raise Exception(f"Failed to extract data: {e}")
        