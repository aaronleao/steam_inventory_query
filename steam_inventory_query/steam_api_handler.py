import logging
import requests
from steam_inventory_query import inventory_validator
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__package__)

def fetch_inventory(STEAM_ID=str, APP_ID=str, CONTEXT_ID=str, API_KEY=str) -> dict:
    """
    Fetches inventory data from the given URL with pagination.
    """

    inventory = {"assets": [], "descriptions": []}

    # Construct the base URL and parameters
    url = f"https://steamcommunity.com/inventory/{STEAM_ID}/{APP_ID}/{CONTEXT_ID}"
    params = {"key": API_KEY} if API_KEY else {}

    while True:
        # Make the API request
        response = requests.get(url, params=params)
        if response.status_code != 200:
            logger.error(f"Failed to fetch inventory. Status code: {response.status_code}")
            break

        # Parse the JSON response
        data = response.json()
        
        if not inventory_validator.validate_format(data):
            break

        # Append the items to the result
        inventory["assets"].extend(data["assets"])
        inventory["descriptions"].extend(data["descriptions"])

        # Check if there are more items to fetch
        if data.get("more_items", 0) == 1:
            params["start_assetid"] = data["last_assetid"]
        else:
            break

    return inventory

def resolve_vanity(API_KEY, STEAM_USER):

    url = f'http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={API_KEY}&vanityurl={STEAM_USER}'
    params = {}
    response = requests.get(url, params)
    data = response.json()
    response = data.get("response")
    success = response.get("success")
    if success != 1:
        raise SystemExit(f"Failed to fetch STEAM_ID for{STEAM_USER}")

    steam_id = response.get("steamid")
    return steam_id

def fetch_players(API_KEY, STEAM_ID):

    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {"key": API_KEY, "steamids": STEAM_ID}

    response = requests.get(url, params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        players = data.get("response", {}).get("players", [])
        if players:
            return players
        else:
            logger.error("Error: No player data found.")
    else:
        logger.error(f"Failed to fetch profile. Status code: {response.status_code}")

    return None