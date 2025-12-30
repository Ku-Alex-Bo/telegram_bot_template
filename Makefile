.PHONY: setup-env run

setup-env:
	@if [ ! -f .env ]; then \
		cp .env.example .env && echo "✅ .env file created"; \
	else \
		echo "⚠️ .env file already exists"; \
	fi

run:
	uv run python main.py

test:
	uv run pytest
