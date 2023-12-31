migrate:
	python src/manage.py migrate $(if $m, api $m,)

migrate3:
	python3 src/manage.py migrate $(if $m, api $m,)

makemigrations:
	python src/manage.py makemigrations
	sudo chown -R ${USER} src/app/migrations/

makemigrations_local:
	make python src/manage.py makemigrations --settings=config.settings_local

createsuperuser:
	python src/manage.py createsuperuser --settings=config.settings_local

createsuperuserserver:
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
	python src/manage.py start_bot --settings=config.settings_local

run_server:
	python src/manage.py runserver --settings=config.settings_local

all_run:
	python src/manage.py start_bot --settings=config.settings_local
	python src/manage.py runserver --settings=config.settings_local

docker_stop:
	docker-compose down

docker_start:
	docker-compose up

push:
	docker-compose push ${IMAGE_APP}

docker_test:
	echo "There will be tests"

ci_test:
	# docker-compose run app-service pytest --cov-config=.coveragerc --cov=src -v src/app/tests/ --ds=config.settings


ci_build:
	docker-compose build
	docker-compose push

ci_lint:
	apk add --no-cache py3-pip
	pip install flake8 isort black
	make check_lint

ci_deploy:
	docker pull ${CI_REGISTRY_IMAGE}:latest
	docker-compose down
	docker-compose run app-service python src/manage.py migrate
	docker-compose up -d

tank_it:
	docker run --rm -v $(pwd):/var/loadtest -v $SSH_AUTH_SOCK:/ssh-agent -e SSH_AUTH_SOCK=/ssh-agent --net host -it direvius/yandex-tank
