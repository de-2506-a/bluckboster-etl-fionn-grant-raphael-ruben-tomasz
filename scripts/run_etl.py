import os
import sys
from config.env_config import setup_env
from config.db_config import load_db_config


def main():
    try:
        # Setup environment variables to prepare for database connection
        setup_env(sys.argv)
        env = os.getenv("ENV", "unknown")
        print(f"Running in {env} environment")

        # Use environment variables to create connection details
        connection_details = load_db_config()
        print(f"Database connection details: {connection_details}")

    except Exception as e:
        print(f"Error retrieving environment variable: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
