""" This module is responsible for displaying the inventory items. """

from steam_inventory_query.inventory_item import constants
from steam_inventory_query.inventory_item import InventoryItem

def display(inventory: dict, inventory_full: bool):
    """
    Displays all assets with their respective descriptions.
    """

    for description in inventory["descriptions"]:
        item = InventoryItem(description)
        if not inventory_full and item.item_desc_type != constants.ItemType.HERO.name and item.item_desc_type != constants.ItemType.MISC.name:
            item.print()
        else:
           item.print()
