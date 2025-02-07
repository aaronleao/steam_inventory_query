from steam_inventory_query.inventory_item import inventory_item

def display(inventory):
    """
    Displays all assets with their respective descriptions.
    """

    for description in inventory["descriptions"]:
        item = inventory_item(description)
        item.print()