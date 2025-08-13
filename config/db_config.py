import os


# Define the structure of the database configuration and retrieve environment variables
def load_db_config():
    config = {
        "source_database": {
            "dbname": os.getenv("SOURCE_DB_NAME", "error"),
            "user": os.getenv("SOURCE_DB_USER", "error"),
            "password": os.getenv("SOURCE_DB_PASSWORD", ""),
            "host": os.getenv("SOURCE_DB_HOST", "error"),
            "port": os.getenv("SOURCE_DB_PORT", "5432"),
        },
        "target_database": {
            "dbname": os.getenv("TARGET_DB_NAME", "error"),
            "user": os.getenv("TARGET_DB_USER", "error"),
            "password": os.getenv("TARGET_DB_PASSWORD", ""),
            "host": os.getenv("TARGET_DB_HOST", "error"),
            "port": os.getenv("TARGET_DB_PORT", "5432"),
        },
    }

    # Validate the database configuration
    validation_db_config(config)

    return config


def validation_db_config(config):
    # Check for missing environment variables
    for db_key, db_config in config.items():
        for key, value in db_config.items():
            if value == "error":
                raise ValueError(f"Missing environment variable for {db_key} - {key}")