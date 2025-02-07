from steam_inventory_query import constants

class inventory_item(object):
    def __init__(self, item_description=dict):
        if not item_description:
            return None

        self.item_type          = constants.item_type.DEFAULT
        self.classid            = item_description['classid']
        self.instanceid         = item_description['instanceid']
        self.name               = item_description['name']
        self.market_name        = item_description['market_name']
        self.marketable         = item_description['marketable']
        self.tradable           = item_description['tradable']
        self.desc_type          = item_description['type']
        # self.description_values = self.get_descriptions_values(item_description)

    def print(self):
        # line = f'{self.desc_type} | {self.classid} | {self.instanceid} | {self.description_values} | {self.desc_type} | {self.name} | {self.market_name} | {self.marketable} | {self.tradable}'
        line = f'{self.desc_type} | {self.classid} | {self.instanceid} | {self.desc_type} | {self.name} | {self.market_name} | {self.marketable} | {self.tradable}'
        print(line)

    def get_descriptions_values(self, item_description=dict):

        print("get_desctr", dir(item_description))

        sub_descriptions = item_description.get("descriptions") # Not all description has sub_descriptions.
        if sub_descriptions is not None:
            values = [d['value'] for d in sub_descriptions if 'value' in d]
            return values
        return None

    # def __call__(self, item_description):
    #     print("inventory_item Dentro do __call__")

# __call__ = inventory_item.__init__
# __call__ = __init__