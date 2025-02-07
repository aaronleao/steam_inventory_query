from steam_inventory_query import constants

class inventory_item(object):
    def __init__(self, item_description=dict):
        if not item_description:
            return None

        self.classid            = item_description['classid']
        self.instanceid         = item_description['instanceid']
        self.name               = item_description['name']
        self.market_name        = item_description['market_name']
        self.marketable         = item_description['marketable'] != 0
        self.tradable           = item_description['tradable'] != 0
        self.desc_type          = item_description['type']
        self.description_values = self.get_descriptions_values(item_description)
        [self.item_desc_type, self.item_desc_name] = self.set_item_type(self.description_values)

    def print(self):
        line = f'{self.item_desc_type: <7}|{self.item_desc_name: <24}|{self.desc_type: <20}|{self.name: <20}|{self.market_name: <20}|{self.marketable: <2}|{self.tradable: <2}|'
        full_line = f'{self.classid: <10}|{self.instanceid: <10}|{line}'
        print(line)

    def get_descriptions_values(self, item_description=dict):

        sub_descriptions = item_description.get("descriptions") # Not all description has sub_descriptions.
        if sub_descriptions is not None:
            values = [d['value'] for d in sub_descriptions if 'value' in d]
            return values
        return None

    def get_hero(self, value=str):
        """
        Returns the hero is it is aplicable.
        Returns None if it is not.
        """
        if not value:
            return None

        # Iterate through the list to find the first occurrence of 'Used By:'
        if value.startswith('Used By:'):
                # Split the string by ':' and get the second part
            aux = value.split(':')[1].strip()
            return aux
        return None

    def set_item_type(self, description_values):
        # description_values could be None
        if description_values:
            for value in description_values:
                hero = self.get_hero(value)
                if hero:
                    return [constants.item_type.HERO.name, hero]
                
            return [constants.item_type.DEFAULT.name, ""]
        else:
            return [constants.item_type.DEFAULT.name, ""]