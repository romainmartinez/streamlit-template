import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from rich import (
    # using rich for better print
    traceback,
)

load_dotenv()

# using rich for better traceback
traceback.install(show_locals=True)

RANDOM_SEED = 42
APP_PASSWORD: str = os.getenv("APP_PASSWORD")
if not APP_PASSWORD:
    msg = "APP_PASSWORD not set. Put it in .env file or as an environment variable."
    raise ValueError(msg)

IS_LOCAL = "local" in sys.argv

DATA_PATH = Path("data")
