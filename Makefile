.PHONY: test
test:
	poetry run test

.PHONY: wheel
wheel:
	poetry build -f wheel

.PHONY: install
test:
	poetry install

.PHONY: lint
lint:
	pylint src