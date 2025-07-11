import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file from one level up if needed
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Get environment variables
email = os.getenv("email")
password = os.getenv("passw")
api_key = os.getenv("api_key")

print(email, "is the email of the website")