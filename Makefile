.PHONY: install setup-env run

install:
	pip install .

setup-env:
	cp .env.example .env

run:
	python main.py

