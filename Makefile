.PHONY: setup-env run fix format test mypy

setup-env:
	@if [ ! -f .env ]; then \
		cp .env.example .env && echo "✅ .env file created"; \
	else \
		echo "⚠️ .env file already exists"; \
	fi

run:
	uv run python main.py

fix:
	uv run ruff check . --fix

format:
	uv run ruff format .

test:
	uv run pytest

mypy:
	uv run mypy .