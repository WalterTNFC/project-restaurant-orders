# Initial commit
# Prato mais pedido por maria
# Quantas vezes arnaldo pediu hamburguer
# Quais pratos joao nunca pediu
# dias que joao nunca foi a lanchonete
# salvar em data/mkt_campaign.txt matendo a ordem
from pathlib import Path
import csv


def count_maria_request(maria_orders):
    count = 0
    maria_more_request = None
    for i in maria_orders:
        if maria_orders[i] > count:
            maria_more_request = i
            count = maria_orders[i]

    return maria_more_request


def find_more_requests(data):
    maria_orders = {}

    for customer, order, _ in data:
        if customer == "maria":
            if order not in maria_orders:
                maria_orders[order] = 1
            else:
                maria_orders[order] += 1

    return count_maria_request(maria_orders)


def count_arnaldo_order_hamburguer(data):
    count = 0

    for customer, order, _ in data:
        if customer == "arnaldo" and order == "hamburguer":
            count = count + 1

    return count


def joao_dont_visit(data):
    total_days = set()
    days = set()

    for customer, order, day in data:
        if customer == "joao":
            if day != "domingo":
                days.add(day)

        if day != "domingo":
            total_days.add(day)
        else:
            None

    return total_days.difference(days)


def joao_dont_order(data):
    total_orders = set()
    orders = set()

    for customer, order, day in data:
        if customer == "joao":
            orders.add(order)

        total_orders.add(order)

    return total_orders.difference(orders)


def analyze_log(path_to_file):
    # Verificar se o formato do arquivo é csv [1]
    if Path(path_to_file).suffix != '.csv':
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, encoding="utf-8") as file:
            data = list(csv.reader(file, delimiter=",", quotechar='"'))
            most_maria = find_more_requests(data)
            arnaldo = count_arnaldo_order_hamburguer(data)
            joao_order = joao_dont_order(data)
            joao_visit = joao_dont_visit(data)

            result = f'{most_maria}\n{arnaldo}\n{joao_order}\n{joao_visit}\n'
            print(result)
            with open('data/mkt_campaign.txt', mode='w') as file_txt:
                file_txt.write(result)
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
# Referencias:
# [1]-https://pt.stackoverflow.com/questions/382049


analyze_log('./data/orders_1.csv')
