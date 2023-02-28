class InventoryControl:
    inventory = dict

    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.inventory = {
            ingredient: 0
            for ingredient
            in self.MINIMUM_INVENTORY.keys()
        }

    def add_new_order(self, customer, order, day):
        ingredients = self.INGREDIENTS
        inventory = self.inventory
        minimum = self.MINIMUM_INVENTORY

        for i in ingredients[order]:
            if (inventory[i] < minimum[i]):
                inventory[i] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        ingredients = self.INGREDIENTS
        inventory = self.inventory
        minimum = self.MINIMUM_INVENTORY
        dishes = set(ingredients.keys())

        for i in inventory.keys():
            if(inventory[i] == minimum[i]):
                for index, value in ingredients.items():
                    if i in value:
                        dishes.discard(index)

        return dishes
