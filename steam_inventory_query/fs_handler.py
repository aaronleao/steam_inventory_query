### File system handler
from steam_inventory_query import constants
import os
import json

def create_cache_dir():
    if not os.path.exists(constants.CACHE_DIR):
        os.makedirs(constants.CACHE_DIR)

def get_inventory_file_path(steam_id=str, app_id=str):
    inventory_file_name = f"{steam_id}_full_inventory_{app_id}.json"
    inventory_file_path = f'{constants.CACHE_DIR}/{inventory_file_name}'
    return inventory_file_path

def read_inventory(inventory_file_path=str) -> dict:
    with open(inventory_file_path, "r", encoding="utf-8") as file:
        print(f"Reading '{inventory_file_path}'.")
        inventory = json.load(file)
        return inventory

def write_inventory(inventory_file_path=str, inventory=dict):
    # Save the full inventory to a JSON file
    with open(inventory_file_path, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)
    print(f"Inventory saved in: '{inventory_file_path}'.")