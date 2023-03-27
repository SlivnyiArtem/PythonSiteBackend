migrate:
	python src/manage.py migrate $(if $m, api $m,)

migrate3:
	python3 src/manage.py migrate $(if $m, api $m,)

makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

createsuperuser:
	python src/manage.py createsuperuser --settings=config.settings_local

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
	apk add py3-isort
	apk add py3-flake8
	isort --check --diff .
	flake8 --config setup.cfg
	black --check --config pyproject.toml .

run_bot:
	python src/manage.py start_bot --settings=config.settings_local

run_server:
	python src/manage.py runserver --settings=config.settings_local

docker_stop:
	docker-compose down

docker_start:
	docker-compose up

push:
	docker-compose push ${IMAGE_APP}

docker_test:
	echo "There will be tests"