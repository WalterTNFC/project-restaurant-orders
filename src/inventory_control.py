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
        for i in self.INGREDIENTS[order]:
            if (self.inventory[i]
                    < self.MINIMUM_INVENTORY[i]):
                self.inventory[i] += 1
            else:
                return False

    def get_quantities_to_buy(self):
        return self.inventory
