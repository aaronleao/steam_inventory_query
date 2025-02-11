""" This module contains the class to represent an inventory item. """

from steam_inventory_query import constants

class InventoryItem:
    """
    This class represents an inventory item.
    It provides methods to extract and display relevant information
    from the item description.
    """
    def __init__(self, item_description: dict):
        if not item_description:
            raise SystemExit("Inventory: Invalid item_description")

        self.classid            = item_description['classid']
        self.instanceid         = item_description['instanceid']
        self.name               = item_description['name']
        self.market_name        = item_description['market_name']
        self.marketable         = item_description['marketable'] != 0
        self.tradable           = item_description['tradable'] != 0
        self.desc_type          = item_description['type']
        self.description_values = self.get_descriptions_values(item_description)
        [self.item_desc_type, self.item_desc_name] = self.set_item_type()

    def print(self, display_full_inventory:bool):
        """ Prints the item description. """

        line = f'{self.item_desc_type: <12}|{self.item_desc_name: <30}|{self.desc_type: <30}|{self.name: <60}|{self.marketable: <2}|{self.tradable: <2}|'
        # full_line = f'{self.classid: <10}|{self.instanceid: <10}|{line}'
        if not display_full_inventory and self.item_desc_type != constants.ItemType.HERO.name and self.item_desc_type != constants.ItemType.MISC.name:
            print(line)
        else:
            print(line)

    def get_descriptions_values(self, item_description: dict):
        """ Returns the values of the descriptions. """
        sub_descriptions = item_description.get("descriptions")
        if sub_descriptions is not None:
            values = [d['value'] for d in sub_descriptions if 'value' in d]
            return values
        return None

    def is_hero(self, description_values: list) -> str:
        """ Returns if it is a HERO item """
        if not description_values:
            return None

        return [value.split(':')[1].strip()
                for value in description_values
                if value.startswith('Used By:')]

    def is_weather(self, desc_type: str) -> bool:
        """ Returns if it is a WEATHER item """
        if desc_type and "Weather" in desc_type:
            return True
        return False

    def is_bundle(self, desc_type: str) -> bool:
        """ Returns if it is a BUNDLE item """
        if desc_type and "Bundle" in desc_type:
            return True
        return False

    def is_ward(self, desc_type: str) -> bool:
        """ Returns if it is a WARD item """
        if desc_type and "Ward" in desc_type:
            return True
        return False

    def is_courier(self, desc_type: str) -> bool:
        """ Returns if it is a COURIER item """
        if desc_type and "Courier" in desc_type:
            return True
        return False

    def set_item_type(self):
        """
        Returns the item type based on the description type.
        The sequence of checks is important.
        1. Check if it is a courier
        2. Check if it is a weather effect
        3. Check if it is a ward
        4. Check if it is a hero
        5. Check if it is a hero bundle
        6. Check if it is a bundle
        7. If none of the above, it is a misc item
        """

        if self.is_courier(self.desc_type):
            return [constants.ItemType.COURIER.name, constants.ItemType.COURIER.value]

        if self.is_weather(self.desc_type):
            return [constants.ItemType.WEATHER.name, constants.ItemType.WEATHER.value]

        if self.is_ward(self.desc_type):
            return [constants.ItemType.WARD.name, constants.ItemType.WARD.value]

        hero = self.is_hero(self.description_values)
        if hero:
            if self.is_bundle(self.desc_type):
                return [constants.ItemType.HERO_BUNDLE.name, hero[0]]
            return [constants.ItemType.HERO.name, hero[0]]

        if self.is_bundle(self.desc_type):
            return [constants.ItemType.BUNDLE.name, constants.ItemType.BUNDLE.value]

        return [constants.ItemType.MISC.name, constants.ItemType.MISC.value]
