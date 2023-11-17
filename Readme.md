### Общее

- Использовал `Makefile` для основных команд
- Менеджер зависимостей: `poetry`
- Фреймворк: `FastAPI`, сервер: `uvicorn`
- Линтинг: `pylint`, тесты: `pytest`
- Конфигурация в `.env`
- Настроил CI на `pylint`
- Добавил CRUD-эндпоинты для шаблонов форм
- Обычно, пишу комментарии и `Readme` по-английски, здесь
сделал по-русски для удобства проверки
- В клиенте не стал использовать `match` и `case`
чтобы можно было тестировать на хостовой машине с более ранними версиями python

### Сервис

Запуск сервиса:
```shell
make env  # создает .env на основе .env.sample
make run  # вызывает docker-compose
# или
cp .env.sample .env
docker-compose up -d
```
Спецификация Openapi при работающем сервисе будет на:
`http://127.0.0.1/docs`

В `/get_form` решил передавать данные формы через body, так как это более естественно для `POST` - запроса 

Но как мне кажется семантика этого запроса больше походит на `GET`

Исходники:
- `app` - сервис
  - `config` - подтягивание конфигурации из `.env`
  - `db` - функции для работы с БД
  - `dependencies` - зависимости для dependency injection в FastAPI
  - `endpoints` - "ручки" :)
  - `schemas` - перечисления и модели Pydantic
  - `utils` - бизнес логика получения типов полей
- `client` - клиент
- `test` - тесты
  - `fixtures` - фикстуры
  - `test_endpoints` - тесты для ручек
  - `test_utils` - тесты функций бизнес-логики

### Тесты и проверка кода
Для запуска тестов в Docker:
```shell
make test-app
```
Для запуска линтера:
```shell
make lint
```

### Клиент
Перед запуском клиента нужно установить зависимости:
```shell
poetry install  # pwd: корень проекта
```
Клиент реализован в виде CLI-приложения на `argparse`
Примеры запуска
```shell
# Создание шаблона
poetry run python client/main.py create --json='{"name": "form", "fields": {"a": "email", "b": "phone"}}'
# Получение шаблонов
poetry run python client/main.py get
# Шаблон по id
poetry run python client/main.py get --id=65573925ce9676ffd3cb4d0d
# Удаление по id
poetry run python client/main.py delete --id=65573925ce9676ffd3cb4d0d
# Поиск шаблона или типизация формы
poetry run python client/main.py get_form --json='{"a": "example@mail.ru", "b": "01.01.2000"}'
# Задать URL отличный от "http://127.0.0.1:8000"
poetry run python client/main.py --base_url="..." get
```