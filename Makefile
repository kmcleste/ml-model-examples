init-repo:
	poetry install
	poetry shell

black:
	poetry run black .

pre-commit:
	poetry run pre-commit .

streamlit:
	poetry run streamlit run src/01_🏠_Home.py
