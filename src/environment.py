import os
from dotenv import load_dotenv


def get_api_key():
    load_dotenv()
    return os.getenv("API_KEY")
