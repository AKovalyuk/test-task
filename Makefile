test-app:
	docker-compose run --rm app poetry run python -m pytest -vv

env:
	cp .env.sample .env

lint:
	poetry run pylint --fail-under=9 app test

run:
	docker-compose up -d