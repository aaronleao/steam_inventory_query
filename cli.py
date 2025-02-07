from steam_inventory_query import constants
from steam_inventory_query import display_inventory
from steam_inventory_query import fetch_inventory
from steam_inventory_query import fs_handler
from steam_inventory_query import parser
from steam_inventory_query import steam_api_handler

def main():
    # Get args
    [STEAM_ID, STEAM_USER, APP_ID, API_KEY, OVERWRITE, DISPLAY] = parser.get_args()

    if STEAM_ID is None and STEAM_USER:
        STEAM_ID = [steam_api_handler.resolve_vanity(API_KEY, user) for user in STEAM_USER]

    # Create cache dir
    fs_handler.create_cache_dir()

    # Fetch the inventory
    inventories = [fetch_inventory.fetch(profile_id, APP_ID, constants.CONTEXT_ID, API_KEY, OVERWRITE) for profile_id in STEAM_ID ]

    # Display inventories
    [display_inventory.display(inventory) for inventory in inventories if DISPLAY]

if __name__ == "__main__":
    main()
