import pandas as pd
from src.extract.extract_actor import extract_actor

def extract_data() -> tuple[pd.DataFrame,pd.DataFrame]:
    try:
        actor_table = extract_actor()
        
        print(f"Data Extraction was completed successfully")
        print(f"Actor: {actor_table.shape}")
        return (actor_table)
    except Exception as e:
        print(f"Data extraction has failed: {str(e)}")
        raise