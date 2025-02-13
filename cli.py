"""Main entry point for the Steam inventory query CLI."""

# Description: Main entry point for the Steam inventory query CLI.
#
# This module is responsible for handling the main entry point for the Steam inventory query CLI.
# It performs the following steps:
# 1. Resolves Steam IDs from Steam usernames if necessary.
# 2. Fetches the inventory for each Steam ID.
# 3. Displays the fetched inventories if the display option is enabled.

from steam_inventory_query import fs_handler
from steam_inventory_query import parser
from steam_inventory_query import steam_api_handler
from steam_inventory_query import steam_players

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

    players = steam_players.fetch_players(
        args.api_key, args.steam_ids, args.steam_users
    )
    for player in players:
        player.load_inventory(args.api_key, args.overwrite)


    for player in players:
        if args.display_player:
            player.print()
        if args.display_inventory:
            player.print_inventory(args.display_inventory_full, args.api_key)
        


    # ## Fetch steam market item price
    # for player in players:
    #     for item in player.inventory:
    #         if item.marketable:
    #             item. .fetch_steam_maket_price(args.api_key, args.app_id, item.market_hash_name)


if __name__ == "__main__":
    # Create cache dir
    fs_handler.create_cache_dir()
    main()
