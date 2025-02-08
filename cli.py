""" Main entry point for the Steam inventory query CLI. """
# Description: Main entry point for the Steam inventory query CLI.
#
# This module is responsible for handling the main entry point for the Steam inventory query CLI.
# It performs the following steps:
# 1. Resolves Steam IDs from Steam usernames if necessary.
# 2. Fetches the inventory for each Steam ID.
# 3. Displays the fetched inventories if the display option is enabled.

from .steam_inventory_query import constants
from .steam_inventory_query import display_inventory
from .steam_inventory_query import fetch_inventory
from .steam_inventory_query import fs_handler
from .steam_inventory_query import parser
from .steam_inventory_query import steam_api_handler

def main():
    """
    Main function to handle the Steam inventory query process.

    This function performs the following steps:
    1. Resolves Steam IDs from Steam usernames if necessary.
    2. Fetches the inventory for each Steam ID.
    3. Displays the fetched inventories if the display option is enabled.
    """

    # Get args
    [steam_id, steam_user, app_id, api_key, overwrite, display] = parser.get_args()

    if steam_id is None and steam_user:
        steam_id = [steam_api_handler.resolve_vanity(api_key, user) for user in steam_user]


    # Fetch the inventory
    inventories = [fetch_inventory.fetch(profile_id, app_id,
                                        constants.CONTEXT_ID,
                                        api_key, overwrite) for profile_id in steam_id ]

    # Display inventories
    if display:
        for inventory in inventories:
            display_inventory.display(inventory)

if __name__ == "__main__":

    # Create cache dir
    fs_handler.create_cache_dir()
    main()
