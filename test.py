# Иванцовская Виктория, 19-я когорта — Финальный проект. Инженер по тестированию плюс
import create_order

# Cоздание заказа
def get_track():
    order = create_order.create_new_order()
    if order.ok:
        return order.json()["track"]

# запрос на получения заказа по треку заказа
def test_get_order_info_by_track():
    # сохранение номера заказа
    new_track = get_track()

    response = create_order.get_order_by_track(new_track)
    assert response.status_code == 200
