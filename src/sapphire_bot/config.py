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

# mGBA executable file path.
MGBA_EXECUTABLE_PATH = get_required_env("MGBA_EXECUTABLE_PATH")
if not os.path.isfile(MGBA_EXECUTABLE_PATH):
    raise FileNotFoundError(f"MGBA executable not found: {MGBA_EXECUTABLE_PATH}")
# Sapphire file rom path.
SAPPHIRE_ROM_PATH = get_required_env("SAPPHIRE_ROM_PATH")
if not os.path.isfile(SAPPHIRE_ROM_PATH):
    raise FileNotFoundError(f"Sapphire rom not found: {SAPPHIRE_ROM_PATH}")
