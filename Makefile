help:
	@echo "Tasks in \033[1;32mrelay42-clickstream\033[0m:"
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

build:
	pip install wheel
	python setup.py bdist_wheel

clean:
	@rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
	@find . -not -path './.venv*' -path '*/__pycache__*' -delete
	@find . -not -path './.venv*' -path '*/*.egg-info*' -delete


dockerize:
	make build
	docker build --rm -f "Dockerfile" -t menziess/training-sklearn:latest .

publish:
	docker push menziess/training-sklearn:latest

run:
	docker run --rm -it \
	-p 8000:8000 \
	menziess/training-sklearn:latest
