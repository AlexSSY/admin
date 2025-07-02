import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent

DEBUG = True
STATIC_FILES_DIR = BASE_DIR / "statics"
TEMPLATE_DIRS = [
    BASE_DIR / "templates",
]

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
DB_URL = os.getenv("DB_URL")
