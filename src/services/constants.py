import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

APP_PASSWORD = os.getenv("APP_PASSWORD")
if not APP_PASSWORD:
    msg = "APP_PASSWORD not set. Put it in .env file or as an environment variable."
    raise ValueError(
        msg,
    )

IS_LOCAL = "local" in sys.argv

DATA_PATH = Path("data")
