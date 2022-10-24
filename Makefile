.PHONY: test
test:
	poetry run pytest

.PHONY: wheel
wheel:
	poetry build -f wheel