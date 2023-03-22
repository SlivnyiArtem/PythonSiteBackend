migrate:
	python src/manage.py migrate $(if $m, api $m,)

migrate3:
	python3 src/manage.py migrate $(if $m, api $m,)

makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

createsuperuser:
	python src/manage.py createsuperuser

collectstatic:
	python src/manage.py collectstatic --no-input

dev:
	python src/manage.py runserver localhost:8000

command:
	python src/manage.py ${c}

shell:
	python src/manage.py shell

debug:
	python src/manage.py debug

piplock:
	pipenv install
	sudo chown -R ${USER} Pipfile.lock

lint:
	isort .
	flake8 --config setup.cfg
	black --config pyproject.toml .

check_lint:
	isort --check --diff .
	flake8 --config setup.cfg
	black --check --config pyproject.toml .

run_bot:
	python src/manage.py start_bot

run_server:
	python src/manage.py runserver

docker_build:
	docker-compose build

docker_stop:
	docker-compose down

docker_start:
	docker-compose up

docker_test:
	echo "There will be tests"

pull:
	pass

push:
	pass

migrate_new:
	docker-compose run rest python src/manage.py migrate --noinput