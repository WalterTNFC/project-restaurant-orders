# Prato favorito por cliente
# Pratos nunca pedidos por cada cliente
# Dias nunca visitados por cada cliente
# Dia mais movimentado
# Dia menos movimentado


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.data = []
        self.days = {}

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        count = {}
        for name, product, _ in self.data:
            if name == customer:
                if product not in count:
                    count[product] = 1
                else:
                    count[product] += 1
        # Referencia [1]
        return max(count, key=count.get)

    def get_never_ordered_per_customer(self, customer):
        count = {}
        for name, product, _ in self.data:
            if name == customer:
                if product not in count:
                    count[product] = 1
                else:
                    count[product] += 1

        get_product = {index[1] for index in self.data}
        # Referencia [2]
        return get_product.difference(count.keys())

    def get_days_never_visited_per_customer(self, customer):
        total_days = set()
        visited_days = set()

        for i in self.data:
            if i[0] == customer:
                visited_days.add(i[2])
            total_days.add(i[2])

        return total_days.difference(visited_days)

    def get_busiest_day(self):
        busiest_day = None
        count = 0

        for i in self.days:
            if self.days[i] > count:
                count = self.days[i]
                busiest_day = i

        return busiest_day

    def get_least_busy_day(self):
        count = 0
        busy_day = None

        for i in self.days:
            count = self.days[i]
            break

        for i in self.days:
            if self.days[i] <= count:
                count = self.days[i]
                busy_day = i

        return busy_day

# Referencias
# [1]:
#  https://www.programiz.com/python-programming/methods/built-in/max
# [2]:
# https://www.geeksforgeeks.org/python-difference-in-keys-of-two-dictionaries/
