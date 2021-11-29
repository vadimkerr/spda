#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

#* Directories with source code
CODE = src tests
TESTS = tests


#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install:
	poetry install -n
	mypy --install-types --non-interactive $(CODE)

.PHONY: pre-commit-install
pre-commit-install:
	pre-commit install

#* Formatters
.PHONY: codestyle
codestyle:
	pyupgrade --exit-zero-even-if-changed --py39-plus **/*.py
	autoflake --recursive --in-place --remove-all-unused-imports --ignore-init-module-imports $(CODE)
	isort --settings-path pyproject.toml $(CODE)
	black --config pyproject.toml $(CODE)

.PHONY: format
format: codestyle

#* Test
.PHONY: test-unit
test-unit:
	pytest -c pyproject.toml -s tests/unit

.PHONY: test-int
test-int:
	pytest -c pyproject.toml -s tests/integration

.PHONY: test-cov-report
test-cov-report:
	coverage xml

.PHONY: test
test: test-unit test-int

# Validate pyproject.toml
.PHONY: check-poetry
check-poetry:
	poetry check

#* Check code style
.PHONY: check-isort
check-isort:
	isort --diff --check-only --settings-path pyproject.toml $(CODE)

.PHONY: check-black
check-black:
	black --diff --check --config pyproject.toml $(CODE)

.PHONY: check-darglint
check-darglint:
	darglint --verbosity 2 $(CODE)

.PHONY: check-codestyle
check-codestyle: check-isort check-black check-darglint

#* Static linters

.PHONY: check-pylint
check-pylint:
	pylint --rcfile=pyproject.toml $(CODE)

.PHONY: check-mypy
check-mypy:
	mypy --config-file pyproject.toml $(CODE)

.PHONY: static-lint
static-lint: check-pylint check-mypy

#* Check security issues

.PHONY: check-bandit
check-bandit:
	bandit -ll --recursive $(CODE)

.PHONY: check-safety
check-safety:
	safety check --full-report

.PHONY: check-security
check-security:
	safety check --full-report
	bandit -ll --recursive $(CODE)

.PHONY: lint
lint: check-poetry check-codestyle static-lint check-security

#* Docker
# Example: make docker VERSION=latest
# Example: make docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

# Example: make clean_docker VERSION=latest
# Example: make clean_docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

	poetry install -n
.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove docker-remove
