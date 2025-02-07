def validate_format(inventory=dict) -> bool:
    if not inventory or "assets" not in inventory or "descriptions" not in inventory:
        print("Error: Invalid inventory data.")
        return False
    return True

def validate_size(inventory=dict) -> bool:
    print(f'Assets size {len(inventory["assets"])}')
    print(f'Descriptions size {len(inventory["descriptions"])}')
    if not len(inventory["assets"]):
        return False
    return True
