# Запуск тестов
test-app:
	docker-compose run --rm app poetry run python -m pytest -vv

# Создание .env на основе .env.sample
env:
	cp .env.sample .env

# Проверка качества кода
lint:
	poetry run pylint --fail-under=9 app test

# Запуск сервиса и БД
run:
	docker-compose up -d