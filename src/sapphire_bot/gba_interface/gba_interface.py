import os
import subprocess

from sapphire_bot.config import MGBA_EXECUTABLE_PATH, SAPPHIRE_ROM_PATH


class GBAInterface:
    """ Provides an Interface to the GBA emulator. """

    def __init__(self):
        """ Constructor. """
        self._process: subprocess.Popen | None = None

    def launch(self) -> bool:
        """ Launch the GBA emulator with the Sapphire rom loaded.

        Returns:
            (bool): Whether the emulator was successfully launched.
        """
        commands = [
            MGBA_EXECUTABLE_PATH,
            # Starts a GDB session.
            "-g",
            SAPPHIRE_ROM_PATH,
        ]
        try:
            self._process = subprocess.Popen(commands)
            print(f"Launched {os.path.basename(MGBA_EXECUTABLE_PATH)} successfully.")
            return True
        except FileNotFoundError:
            if not os.path.isfile(MGBA_EXECUTABLE_PATH):
                print(f"Error: Could not find the mGBA executable at \"{MGBA_EXECUTABLE_PATH}\".")
            if not os.path.isfile(SAPPHIRE_ROM_PATH):
                print(f"Error: Could not find the Sapphire rom file at \"{SAPPHIRE_ROM_PATH}\".")
            return False
