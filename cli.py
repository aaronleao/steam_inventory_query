""" Main entry point for the Steam inventory query CLI. """
# Description: Main entry point for the Steam inventory query CLI.
#
# This module is responsible for handling the main entry point for the Steam inventory query CLI.
# It performs the following steps:
# 1. Resolves Steam IDs from Steam usernames if necessary.
# 2. Fetches the inventory for each Steam ID.
# 3. Displays the fetched inventories if the display option is enabled.

from steam_inventory_query import constants
from steam_inventory_query import display_inventory
from steam_inventory_query import fetch_inventory
from steam_inventory_query import fs_handler
from steam_inventory_query import parser
from steam_inventory_query import steam_players
from steam_inventory_query import steam_api_handler

def main():
    """
    Main function to handle the Steam inventory query process.

    This function performs the following steps:
    1. Resolves Steam IDs from Steam usernames if necessary.
    2. Fetches the inventory for each Steam ID.
    3. Displays the fetched inventories if the display option is enabled.
    """

    # Get args
    args = parser.get_args()
    [steam_ids, steam_users, app_id, api_key, overwrite, display_inventory_flag, display_player_flag] = [args.profile_id, args.profile_user, args.app_id, args.api_key, args.overwrite, args.display_inventory, args.display_player]

    players = steam_players.fetch_players(api_key, steam_ids, steam_users)
    steam_players.set_players_inventory(api_key, players, app_id, overwrite)
    
    if display_player_flag:
        for player in players:
            player.print()
            if display_inventory_flag:
                display_inventory.display(player.inventory)

if __name__ == "__main__":

    # Create cache dir
    fs_handler.create_cache_dir()
    main()
