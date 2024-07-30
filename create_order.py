import configuration
import requests
import data


# создание заказа
def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_body)


# получение информации о заказе по номеру
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER + str(track_number))
