""" Module providing Constants for the steam_inventory_query package."""
import getpass
from enum import Enum
from platformdirs import PlatformDirs


APP_NAME = "steam_inventory_query"
STEAM_API_KEY_USAGE = 10
APP_ID_map = {570, "Dota 2"}
CACHE_DIR = PlatformDirs(APP_NAME, getpass.getuser()).user_data_dir
CONTEXT_ID = "2"  # Default context ID for most games
INVENTORY_URL_TIMEOUT = 1000000000  # 1 second

class item_type(Enum):
    """ Enum for the item type. """	
    BUNDLE      = "BUNDLE"
    COURIER     = "COURIER"
    HERO_BUNDLE = "HERO_BUNDLE"
    HERO        = "HERO"
    WARD        = "WARD"
    WEATHER     = "WEATHER"
    MISC        = "MISC"
