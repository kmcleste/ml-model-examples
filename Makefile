init-repo:
	poetry install
	poetry shell

black:
	poetry run black .

streamlit:
	poetry run streamlit run src/01_🏠_Home.py

docker-build:
	docker build -t streamlit_demo:latest --no-cache -f build/docker/Dockerfile .

docker-run:
	docker run -p 8501:8501 streamlit_demo:latest

docker-deploy: docker-build docker-run
