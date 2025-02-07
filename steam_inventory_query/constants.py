from enum import Enum
from platformdirs import PlatformDirs
import getpass

APP_NAME = "steam_inventory_query"
APP_ID_map = {570, "Dota 2"}
CACHE_DIR = PlatformDirs(APP_NAME, getpass.getuser()).user_data_dir

class item_type(Enum):
    DEFAULT = 0
    BUNDLE  = 1
    HERO    = 2
    WARD    = 3
    WEATHER = 4
