import os
import pandas as pd
import timeit
import psycopg2
from config.db_config import load_db_config


def extract_customer() -> pd.DataFrame:
    
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
        EXTRACT_CUSTOMER_QUERY_FILE = os.path.join(
            os.path.dirname(__file__), r"C:\Users\ruben\OneDrive\Desktop\digitalfutures\bluckboster-etl-fionn-grant-raphael-ruben-tomasz\sql\extract_customer.sql"
        )
        with open(EXTRACT_CUSTOMER_QUERY_FILE, "r") as file:
            query = file.read()
        # Run Query and store into a DataFrame
        customer_df = pd.read_sql_query(query,connection)
        connection.close()
        extract_customer_execution_time = (
            timeit.default_timer() - start_time
            )
        #Print successful extraction
        print(f"Extracted customer table in {extract_customer_execution_time} seconds")
        customer_df.to_csv(r"data\raw\uncleaned_customer.csv", index= False)
        return customer_df
    # Print unsuccessful extraction
    except Exception as e:
        print(f"Failed to extract data: {e}")
        raise Exception(f"Failed to extract data: {e}")
        