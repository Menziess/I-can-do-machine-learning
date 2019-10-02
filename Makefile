help:
	@echo "Tasks in \033[1;32mI-can-do-machine-learning\033[0m:"
	@cat Makefile

install:
	export PIPENV_VENV_IN_PROJECT=1
	pipenv install -d

lint:
	mypy src --ignore-missing-imports
	flake8 src --ignore=$(shell cat flake_ignored)

dev:
	python setup.py develop

test: dev
	pytest tests/ --doctest-modules --junitxml=junit/test-results.xml

build: clean
	pip install wheel
	python setup.py bdist_wheel

clean:
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete

dockerize: build
	docker build --rm -f "Dockerfile" -t \
  menziess/i-can-do-machine-learning:latest .

publish:
	docker push menziess/i-can-do-machine-learning:latest

run:
	docker run --rm -it \
  -e FLASK_ENV=development \
	-p 8000:8000 \
  -v $$(pwd):/app \
	menziess/i-can-do-machine-learning:latest
