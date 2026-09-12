import configparser
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

config = configparser.ConfigParser()
config.read(Path(__file__).with_name("config.ini"), encoding="utf-8")

env = os.getenv("TEST_ENV", "test")
base_url = config[env]["base_url"]

email = os.getenv("TEST_EMAIL")
password = os.getenv("TEST_PASSWORD")

if not email or not password:
    raise RuntimeError("Missing TEST_EMAIL or TEST_PASSWORD in .env")
