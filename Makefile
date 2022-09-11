init-repo:
	poetry install
	poetry shell

black:
	poetry run black .

pre-commit:
	poetry run pre-commit .