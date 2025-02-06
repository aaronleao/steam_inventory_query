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

def display_inventory(inventory):
    """
    Displays all assets with their respective descriptions.
    """

    print(f'Assets size {len(inventory["assets"])}')
    print(f'Descriptions size {len(inventory["descriptions"])}')

    for description in inventory["descriptions"]:
        classid = description["classid"]
        instanceid = description["instanceid"]
        name = description["name"]
        market_name = description["market_name"]
        marketable = description["marketable"]
        tradable = description["tradable"]
        desc_type = description["type"]        
        sub_descriptions = description.get("descriptions") # Not all description has descriptions.
        
        hero = ""
        if sub_descriptions is not None:
            values = [d['value'] for d in sub_descriptions if 'value' in d]
            hero = get_hero(values)

        line = f'{classid} | {instanceid} | {hero} | {desc_type} | {name} | {market_name} | {marketable} | {tradable}'
        print(line)
