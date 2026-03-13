""" Loads environmental variables. """

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

def get_required_env(key: str) -> str:
    """ Returns the required environmental variable, or raises a KeyError."""
    value = os.getenv(key)
    if value is None:
        raise KeyError(f"Missing required environment variable: {key}")
    return value

MGBA_EXECUTABLE_PATH = get_required_env("MGBA_EXECUTABLE_PATH")
if not os.path.isfile(MGBA_EXECUTABLE_PATH):
    raise FileNotFoundError(f"MGBA executable not found: {MGBA_EXECUTABLE_PATH}")
