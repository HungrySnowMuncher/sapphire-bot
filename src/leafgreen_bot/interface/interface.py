import os
import subprocess

from leafgreen_bot.config import MGBA_EXECUTABLE_PATH, LEAFGREEN_ROM_PATH


class Interface:
    """ Provides an Interface to the GBA emulator. """

    def __init__(self):
        """ Constructor. """
        self._process: subprocess.Popen | None = None

    def launch(self) -> bool:
        """ Launch the GBA emulator with the LeafGreen rom loaded.

        Returns:
            (bool): Whether the emulator was successfully launched.
        """
        commands = [MGBA_EXECUTABLE_PATH, LEAFGREEN_ROM_PATH]
        try:
            self._process = subprocess.Popen(commands)
            print(f"Launched {os.path.basename(MGBA_EXECUTABLE_PATH)} successfully.")
            return True
        except FileNotFoundError:
            if not os.path.isfile(MGBA_EXECUTABLE_PATH):
                print(f"Error: Could not find the mGBA executable at \"{MGBA_EXECUTABLE_PATH}\".")
            if not os.path.isfile(LEAFGREEN_ROM_PATH):
                print(f"Error: Could not find the LeafGreen rom file at \"{LEAFGREEN_ROM_PATH}\".")
            return False
