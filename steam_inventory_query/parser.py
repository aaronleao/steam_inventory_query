import argparse

def get_args():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch Steam inventory.")
    parser.add_argument("--profile-id", type=str, required=True, help="Your 17-digit SteamID.")
    parser.add_argument("--app-id", type=str, default="570", help="The app ID of the game (e.g., 570 for Dota 2).")
    parser.add_argument("--api-key", type=str, help="Your Steam API key (optional for some games).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the inventory file if it already exists.")
    return parser.parse_args()
