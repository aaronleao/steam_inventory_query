import argparse
from steam_inventory import fetch_inventory

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch Steam inventory with pagination.")
    parser.add_argument("--profile-id", type=str, required=True, help="Your 17-digit SteamID.")
    parser.add_argument("--app-id", type=str, default="570", help="The app ID of the game (e.g., 570 for Dota 2).")
    parser.add_argument("--api-key", type=str, help="Your Steam API key (optional for some games).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the inventory file if it already exists.")
    args = parser.parse_args()

    # Use the provided arguments
    STEAM_ID = args.profile_id
    APP_ID = args.app_id
    API_KEY = args.api_key
    CONTEXT_ID = "2"  # Default context ID for most games
    OVERWRITE = args.overwrite

    # Fetch the inventory
    inventory = fetch_inventory(STEAM_ID, APP_ID, CONTEXT_ID, API_KEY, OVERWRITE)

    if inventory:
        print("Inventory fetched successfully.")

# Entry point of the script
if __name__ == "__main__":
    main()