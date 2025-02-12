"""This module contains functions for fetching inventory data from the Steam API."""

import sys
import logging
import requests
from steam_inventory_query import constants
from steam_inventory_query import inventory_validator

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__package__)


def fetch_inventory(steam_id: str, app_id: str, context_id: str, api_key: str) -> dict:
    """Fetches inventory data from the given URL with pagination."""

    inventory = {"assets": [], "descriptions": []}

    # Construct the base URL and parameters
    url = f"https://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}"
    params = {"key": api_key} if api_key else {}

    while True:
        # Make the API request
        response = requests.get(
            url, params=params, timeout=constants.INVENTORY_URL_TIMEOUT
        )
        if response.status_code != 200:
            raise SystemExit(
                f"Failed to fetch online inventory. Status code: {response.status_code}"
            )

        # Parse the JSON response
        data = response.json()

        if not inventory_validator.validate_format(data):
            raise SystemExit("Invalid online inventory.")

        # Append the items to the result
        inventory["assets"].extend(data["assets"])
        inventory["descriptions"].extend(data["descriptions"])

        # Check if there are more items to fetch
        if data.get("more_items", 0) == 1:
            params["start_assetid"] = data["last_assetid"]
        else:
            break

    return inventory


def resolve_vanity(api_key: str, steam_user: str) -> str:
    """Resolves a Steam username to a Steam ID."""

    url = f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={steam_user}"
    params = {}
    response = requests.get(url, params, timeout=constants.INVENTORY_URL_TIMEOUT)
    data = response.json()
    response = data.get("response")
    success = response.get("success")
    if success != 1:
        raise SystemExit(f"Failed to fetch STEAM_ID for{steam_user}")

    steam_id = response.get("steamid")
    return steam_id


def fetch_player_summaries(api_key, steam_ids):
    """Fetches players data from the Steam API."""

    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {"key": api_key, "steamids": steam_ids}

    response = requests.get(url, params, timeout=constants.INVENTORY_URL_TIMEOUT)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        players = data.get("response", {}).get("players", [])
        if players:
            return players
        logger.error("Error: No player data found.")
    else:
        logger.error("Failed to fetch profile. Status code: %s ", response.status_code)

    return None


def fetch_steam_market_item_price(api_key, app_id, market_hash_name):
    """
    Fetches the current market value of an item using the SteamApis API.

    Args:
        api_key (str): Your SteamApis API key.
        app_id (str): The app ID of the game (e.g., 730 for CS:GO).
        market_hash_name (str): The market hash name of the item.

    Returns:
        str: The current market value of the item or None if the request fails.
    """
    url = f"https://steamcommunity.com/market/priceoverview/"
    # https://steamcommunity.com/market/priceoverview/?appid=570&market_hash_name=Genuine%20Smeevil&currency=1&api_key=API_KEY


    # Parameters
    params = {
        "api_key": api_key,
        "appid": app_id,
        "market_hash_name": market_hash_name,
        "currency": 1
    }

    # Make the request
    response = requests.get(url, params=params, timeout=constants.INVENTORY_URL_TIMEOUT)
    if response.status_code != 200:
        print(f"Failed to fetch market data. Status code: {response.status_code}")
        return None

# https://steamcommunity.com/market/priceoverview/?appid=570&market_hash_name=Genuine%20Smeevil&currency=1
# {
#   "success": true,
#   "lowest_price": "$0.11",
#   "volume": "16",
#   "median_price": "$0.10"
# }
    # Parse the response
    data = response.json()
    for item in data:
        if item["market_hash_name"] == market_hash_name:
            return item["prices"]["safe"]

    print(f"Item '{market_hash_name}' not found.")
    return None