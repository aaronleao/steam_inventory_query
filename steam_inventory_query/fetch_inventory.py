import logging
import os

from steam_inventory_query import fs_handler
from steam_inventory_query import inventory_validator
from steam_inventory_query import steam_api_handler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__package__)

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
    else:
        inventory = steam_api_handler.fetch_inventory(steam_id, app_id, context_id, api_key)
        fs_handler.write_inventory(inventory_file_path, inventory)

    log_inventory_details(inventory)

    return inventory

def log_inventory_details(inventory: dict):
    """
    Log details about the inventory.
    """

    logger.info('Assets: %d', len(inventory["assets"]))
    logger.info('Descriptions: %d', len(inventory["descriptions"]))