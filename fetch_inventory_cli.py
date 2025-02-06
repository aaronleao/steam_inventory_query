import argparse
from fetch_inventory import fetch_inventory
from display_inventory import display_inventory

appid_map = {570, "Dota 2"}

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch Steam inventory.")
    parser.add_argument("--profile-id", type=str, required=True, help="Your 17-digit SteamID.")
    parser.add_argument("--app-id", type=str, default="570", help="The app ID of the game (e.g., 570 for Dota 2).")
    parser.add_argument("--api-key", type=str, help="Your Steam API key (optional for some games).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the inventory file if it already exists.")
    args = parser.parse_args()
    # parser.print_help()

    # Use the provided arguments
    STEAM_ID = args.profile_id
    APP_ID = args.app_id
    API_KEY = args.api_key
    CONTEXT_ID = "2"  # Default context ID for most games
    OVERWRITE = args.overwrite

    # Fetch the inventory
    try:
        inventory = fetch_inventory(STEAM_ID, APP_ID, CONTEXT_ID, API_KEY, OVERWRITE)
    except AssertionError as err:
        return err

    

    if inventory:
        print("Inventory fetched successfully.")

    display_inventory(inventory)

    ### TODO ###
    #- Add option to list the whole inventory
    #- Add option to filter all Heroes inside inventory
    #- Add option to filter Ward
    #- Add option to filter Courier
    #- Refactor display_inventory function
    
if __name__ == "__main__":
    main()