from steam_inventory_query import constants
from steam_inventory_query import fs_handler
from steam_inventory_query import inventory_validator
import os
import requests


def fetch_from_url(steam_id=str, app_id=str, context_id=str, api_key=str) -> dict:
    """
    Fetches inventory data from the given URL with pagination.
    """

    inventory = {"assets": [], "descriptions": []}

    # Construct the base URL and parameters
    url = f"https://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}"
    print(f"Fetching inventory: {url}")
    params = {"key": api_key} if api_key else {}

    while True:
        # Make the API request
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch inventory. Status code: {response.status_code}")
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

def fetch(steam_id, app_id, context_id, api_key=None, overwrite=False) -> dict:
    """
    1. Check if the inventory exists in CACHE_DIR
    2. Try to load from disk
    3. Fetch from URL, otherwise
    """

    inventory_file_path =  fs_handler.get_inventory_file_path(steam_id, app_id)

    # Skip download if the file already exists and overwrite is False
    if os.path.exists(inventory_file_path) and not overwrite:
        inventory = fs_handler.read_inventory(inventory_file_path)

        # Validate inventory
        if not inventory_validator.validate_format(inventory):
                raise SystemExit(f"Invalid inventory data in {inventory_file_path}. Run with --overwrite to download again.")
        if not inventory_validator.validate_size(inventory):
                raise SystemExit(f"Empty inventory in {inventory_file_path}. Run with --overwrite to download again.")
        
        # Return a valid inventory
        return inventory
    
    inventory = fetch_from_url(steam_id, app_id, context_id, api_key)
    fs_handler.write_inventory(inventory_file_path, inventory)

    return inventory
