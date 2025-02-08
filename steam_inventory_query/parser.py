""" This module provides the function to parse the command line arguments. """

import argparse
from steam_inventory_query import constants

def check_args(args):
    """ Check the command line arguments for validity. """
    if args.profile_id is None and args.profile_user is None:
        raise SystemExit("Please provide either --profile-id or --profile-user. e.g.: --profile-id XXX YYY ...")
    if args.profile_id and len(args.profile_id) > constants.STEAM_API_KEY_USAGE:
        raise SystemExit(f"Please provide less than {constants.STEAM_API_KEY_USAGE} Steam profile IDs.")

def get_args():
    """ Parse the command line arguments. """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch Steam inventory.")
    parser.add_argument("--profile-id", nargs='+', type=str, help="If you know your 17-digit SteamIDs.")
    parser.add_argument("--profile-user", nargs='+', type=str, help="If you know DON'T your 17-digit SteamIDs.")
    parser.add_argument("--app-id", type=str, default="570", help="The app ID of the game (e.g., 570 for Dota 2).")
    parser.add_argument("--api-key", type=str, help="Your Steam API key (optional for some games).")
    parser.add_argument("--display", action="store_true", help="Dump the inventory on cout.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the inventory files.")

    # Check if the numbers of STEAM_IDs is larger than number of query, which Steam API allows per timeframe
    args = parser.parse_args()
    check_args(args)

    return [args.profile_id, args.profile_user, args.app_id, args.api_key, args.overwrite, args.display]
