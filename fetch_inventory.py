import requests
import json
import os

def get_inventory_from_url(url, params):
    """
    Fetches inventory data from the given URL with pagination.
    """
    all_items = {"assets": [], "descriptions": []}

    while True:
        # Make the API request
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch inventory. Status code: {response.status_code}")
            break

        # Parse the JSON response
        data = response.json()
        if not data or "assets" not in data or "descriptions" not in data:
            print("Error: Invalid inventory data.")
            break

        # Append the items to the result
        all_items["assets"].extend(data["assets"])
        all_items["descriptions"].extend(data["descriptions"])

        # Check if there are more items to fetch
        if data.get("more_items", 0) == 1:
            params["start_assetid"] = data["last_assetid"]
        else:
            break

    return all_items

def fetch_inventory(steam_id, app_id, context_id, api_key=None, overwrite=False):
    """
    Fetches the inventory and saves it to a file.
    """
    # Define the output file name
    output_file = f"{steam_id}_full_inventory_{app_id}.json"

    # Skip download if the file already exists and overwrite is False
    if os.path.exists(output_file) and not overwrite:
        with open(output_file, "r", encoding="utf-8") as file:
            print(f"File '{output_file}' already exists. Skipping download.")
            inventory = json.load(file)
            if not inventory or "assets" not in inventory or "descriptions" not in inventory:
                    raise SystemExit(f"Warning: Invalid inventory data in {output_file}. Run with --overwrite.")
            return inventory

    # Construct the base URL and parameters
    base_url = f"https://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}"
    print(f"Fetching inventory: {base_url}")
    params = {"key": api_key} if api_key else {}

    # Fetch the inventory data
    all_items = get_inventory_from_url(base_url, params)

    # Save the full inventory to a JSON file
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(all_items, file, indent=4)
    print(f"Full inventory saved to '{output_file}'.")

    return all_items