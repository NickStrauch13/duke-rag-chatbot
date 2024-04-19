install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=scripts

format:	
	black scripts/*.py

lint:
	ruff check scripts/*.py

all: install lint format test
