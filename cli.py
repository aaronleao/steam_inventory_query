from steam_inventory_query import parser
from steam_inventory_query import fs_handler
from steam_inventory_query import fetch_inventory
from steam_inventory_query import display_inventory

def main():
    # Get args
    args = parser.get_args()
    # Use the provided arguments
    STEAM_ID = args.profile_id
    APP_ID = args.app_id
    API_KEY = args.api_key
    CONTEXT_ID = "2"  # Default context ID for most games
    OVERWRITE = args.overwrite

    # Create cache dir
    fs_handler.create_cache_dir()

    # Fetch the inventory
    inventory = fetch_inventory.fetch(STEAM_ID, APP_ID, CONTEXT_ID, API_KEY, OVERWRITE)

    display_inventory.display(inventory)

if __name__ == "__main__":
    main()
