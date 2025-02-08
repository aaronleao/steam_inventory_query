""" This module is responsible for displaying the inventory items. """

from steam_inventory_query.inventory_item import InventoryItem

def display(inventory):
    """
    Displays all assets with their respective descriptions.
    """

    for description in inventory["descriptions"]:
        item = InventoryItem(description)
        item.print()
