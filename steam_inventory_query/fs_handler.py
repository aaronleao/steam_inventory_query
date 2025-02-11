""" File system handler for the Steam Inventory Query package. """

import json
import logging
import os
import sys

from steam_inventory_query import constants

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__package__)

def create_cache_dir():
    """ Create the cache directory if it does not exist. """	
    if not os.path.exists(constants.CACHE_DIR):
        os.makedirs(constants.CACHE_DIR)

def get_inventory_file_path(steam_id: str, app_id: str):
    """ Returns the file path for the inventory file. """	
    inventory_file_name = f"{steam_id}_full_inventory_{app_id}.json"
    inventory_file_path = f'{constants.CACHE_DIR}/{inventory_file_name}'
    return inventory_file_path

def read_inventory(inventory_file_path: str) -> dict:
    """ Read the inventory from the given file path. """	
    with open(inventory_file_path, "r", encoding="utf-8") as file:
        logger.info("Reading '%s'.", inventory_file_path)
        inventory = json.load(file)
        return inventory

def write_inventory(inventory_file_path: str, inventory: dict):
    """ Write the inventory to the given file path. """
    with open(inventory_file_path, "w", encoding="utf-8") as file:
        json.dump(inventory, file, indent=4)
    logger.info("Inventory saved in: '%s'.", inventory_file_path)

def get_player_summaries_path(steam_id: str):
    """ Returns the file path for the inventory file. """	
    player_file = f"{steam_id}_summaries.json"
    player_path = f'{constants.CACHE_DIR}/{player_file}'
    return player_path
