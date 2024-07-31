# Final
Работа с базами данных 

1.выведи список логинов курьеров с количеством их заказов в статусе 
 - «В доставке» `(поле inDelivery = true).` 

2 .вывод всех трекеров заказов и их статусы.
 - Если поле `finished == true, то вывести статус 2.`
 - Если поле `canсelled == true, то вывести статус -1.`
 - Если поле `inDelivery == true, то вывести статус 1`.
 - Для остальных случаев вывести `0`

Технические примечания: Доступ к базе осуществляется с помощью команды 
 - `psql -U morty -d scooter_rent. Пароль: smith.` 
 - У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, `select * from “Orders”.`

Автоматизация теста к API

инструменты postman, PyCharm, GitBash, Python
