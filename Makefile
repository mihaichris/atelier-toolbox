.PHONY: test
test:
	poetry run test

.PHONY: wheel
wheel:
	poetry build -f wheel

.PHONY: install
install:
	poetry install
	pre-commit install

.PHONY: lint
lint:
	pylint src --rcfile=standard.rc

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: executable
executable:
	pyinstaller  --name toolbox --noconfirm --clean --console --copy-metadata pikepdf --copy-metadata ocrmypdf .\src\toolbox\cli.py

.PHONY: pre-commit-run
pre-commit-run:
	pre-commit run --all-files

.PHONY: pre-commit-autoupdate
pre-commit-autoupdate:
	pre-commit autoupdate
