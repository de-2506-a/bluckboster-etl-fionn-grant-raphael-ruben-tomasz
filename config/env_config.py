import os
from dotenv import load_dotenv

# Declare acceptable environment variables
ENVS = ["dev", "test"]


def setup_env(args):
    # Load environment variables from a .env file
    if len(args) != 2 or args[1] not in ENVS:
        raise ValueError("Unknown: Acceptable arguments: " + ", ".join(ENVS))

    env = args[1]

    # Clear previous environment details
    remove_prev_env()
    os.environ["ENV"] = env

    env_file = ".env" if env == "prod" else f".env.{env}"

    if not os.path.exists(env_file):
        raise FileNotFoundError(f"Environment file {env_file} does not exist.")

    # Validate the environment
    env = os.getenv("ENV", "unknown")
    if env not in ENVS:
        raise ValueError(f"Invalid environment: {env}. Must be one of {ENVS}")

    print(f"Loading environment variables from: {env_file}")
    load_dotenv(env_file, override=True)
    print(f"Environment set to: {env}")


def remove_prev_env():
    keys_to_clear = [
        "SOURCE_DB_NAME",
        "SOURCE_DB_USER",
        "SOURCE_DB_PASSWORD",
        "SOURCE_DB_HOST",
        "SOURCE_DB_PORT",
        "TARGET_DB_NAME",
        "TARGET_DB_USER",
        "TARGET_DB_PASSWORD",
        "TARGET_DB_HOST",
        "TARGET_DB_PORT",
    ]
    for key in keys_to_clear:
        if key in os.environ:
            del os.environ[key]
