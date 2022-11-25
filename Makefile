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

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt

.PHONY: executable
executable:
	pyinstaller  --name toolbox --noconfirm --clean --console --copy-metadata pikepdf --copy-metadata ocrmypdf .\src\toolbox\cli.py