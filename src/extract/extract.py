import pandas as pd
from src.extract.extract_actor import extract_actor
from src.extract.extract_address import extract_address
from src.extract.extract_category import extract_category

def extract_data() -> tuple[pd.DataFrame,pd.DataFrame, pd.DataFrame]:
    try:
        actor_table = extract_actor()
        address_table = extract_address()
        category_table = extract_category()
        print(f"Data Extraction was completed successfully")
        print(f"Actor: {actor_table.shape}")
        print(f"Address: {address_table.shape}")
        print(f"Category: {category_table.shape}")
        return (actor_table, address_table,category_table)
    except Exception as e:
        print(f"Data extraction has failed: {str(e)}")
        raise