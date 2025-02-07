from steam_inventory_query.inventory_item import inventory_item

def get_hero(values):
    """
    Returns the hero is it is aplicable.
    Returns None if it is not.
    """
    if not values or not isinstance(values, list):
        return None

    # Iterate through the list to find the first occurrence of 'Used By:'
    for item in values:
        if isinstance(item, str) and item.startswith('Used By:'):
            # Split the string by ':' and get the second part
            return item.split(':')[1].strip()
        
    return None

def display(inventory):
    """
    Displays all assets with their respective descriptions.
    """

    for description in inventory["descriptions"]:
        item = inventory_item(description)
        item.print()