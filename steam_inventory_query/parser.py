""" This module provides the function to parse the command line arguments. """

import argparse

def check_args(args):
    """ Check the command line arguments for validity. """
    if args.profile_id is None and args.profile_user is None:
        raise SystemExit("Please provide either --profile-id or --profile-user.")

def get_args():
    """ Parse the command line arguments. """
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Fetch Steam inventory.")
    parser.add_argument("--profile-id", nargs='+', type=str, help="17-digit SteamIDs.")
    parser.add_argument("--profile-user", nargs='+', type=str, help="List of users.")
    parser.add_argument("--app-id", type=str, default="570", help="The app ID (Dota 2=570).")
    parser.add_argument("--api-key", type=str, help="Your Steam API key (optional for some games).")
    parser.add_argument("--display", action="store_true", help="Dump the inventory on cout.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the inventory files.")

    args = parser.parse_args()
    check_args(args)

    return [args.profile_id,
            args.profile_user,
            args.app_id,
            args.api_key,
            args.overwrite,
            args.display]
