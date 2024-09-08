from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    secret_key = os.getenv("SECRET_KEY")
    passphrase = os.getenv("PASSPHRASE")
    return api_key, secret_key, passphrase
